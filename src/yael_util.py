
## Originally written as ``y_util.py``

from __future__ import print_function
from pprint import pprint
import sys

from header_common import *
from header_operations import *

from yael_util_named_ints import *


_TRY_FORMS = set((
    try_begin,
    try_for_range,
    try_for_range_backwards,
    try_for_parties,
    try_for_prop_instances,
    try_for_players))


class y_symbol(str):
    '''
    A string that has itself as repr.
    Useful for debug output.
    '''
    def __repr__(self):
        return self


y_deflocal = y_symbol('y_deflocal')
y_store_params = y_symbol('y_store_params')
y_progn = y_symbol('y_progn')

def y_script(*body):
    '''
    A wrapper for creating module system scripts.

    - Allows calling scripts by name, 

          ('eqmgr_do')
      
      instead of
      
          (call_script, 'script_eqmgr_do')
    
    - For try-forms, provides alternative indentation-friendly syntax,
    
      [OPCODE, ARGS..., [
        BODY
      ],[
        ELSE BODY
      ],[
      ...
      ]]
    
    - Single-line definition of script paramters as
    
          (y_store_params, ":local1", ":local2", ...)

    - Allows defining macros inside a script. These act as 
      locally defined subscripts with the same variable space.
      
          (y_deflocal, "NAME", [ARGLIST], [BODY ...])
      
      ARGLIST defines a list of placeholders, format "::NAME".
      Whenever NAME is uses as an operation, BODY is
      inserted with the ARGLIST place-holders put inside recursively.
      
      In the body, local variables of the form ":_VARNAME" are 
      replaced by ":NAME_VARNAME".
      
      This allows passing operations as arguments.

    - A form
    
          [y_progn, [BODY1...], [BODY2...], ...]
      
      is equivalent to just chaining
      
          BODY1...
          BODY2...
          ...
      
      and is useful for inline-generated code. It is essentially a
      workaround for Python2's lack of generalized star-expansion
      of lists compare to Python3.

    '''
    local_scripts = {} # y_script scoped!

    def _(*items):
        for item, next_item in zip(items, list(items[1:]) + [None]):

            if isinstance(item, str):
                item = (item,)

            if isinstance(item,list): ## [try, ... [BODY...] , [BODY...] ... ] forms.
                assert len(item) > 0, 'zero-item list form not allowed'
                form = item[0]
                if form in _TRY_FORMS:
                    args_begin = 1
                    args_end = len(item)
                    for idx, subitem in enumerate(item[1:],1):
                        if isinstance(subitem, list):
                            args_end = idx
                            break
                    arglist = item[args_begin:args_end]
                    body_lists = item[args_end:]
                    for subitem in body_lists:
                        assert isinstance(subitem, list), 'invalid body item in try form ' + repr(subitem)
                    yield tuple([form] + list(arglist))
                    for body_list in body_lists[:-1]:
                        for subitem in _(*body_list):
                            yield subitem
                        yield (else_try,)
                    for subitem in _(*body_lists[-1]):
                        yield subitem
                    yield (try_end,)
                elif form == y_progn:
                    for body in item[1:]:
                        assert isinstance(body,list), "non-list BODY item in y_progn form, " + repr(item)
                        for form in _(*body):
                            yield form
                else:
                    assert False, "Invalid list form, " + repr(item)
                        

            elif not isinstance(item, tuple):
                yield item
                    
            else: # tuple
                assert len(item) > 0, 'zero-length tuple is not a valid operation'
                
                #### deflocal
                if item[0] == y_deflocal: 
                    assert len(item) == 4, 'y_deflocal form expects 4 arguments, got ' + repr(item)
                    _deflocal, name, arglist, body = item
                    assert isinstance(body, list), 'non-list BODY in y_deflocal form ' + repr(item)
                    assert isinstance(arglist,list), 'non-list ARGLIST in y_deflocal form ' + repr(item)
                    assert all(isinstance(arg,str) and arg.startswith("::") for arg in arglist),\
                        'Non-::placeholder in argument list ' + repr(arglist) + ' for ' + name
                    local_scripts[name] = (arglist, body)

                elif item[0] == y_store_params:
                    for idx, form in enumerate(item[1:],1):
                        yield (store_script_param, form, idx)

                elif isinstance(item[0], str):

                    #### macro expansion
                    if item[0] in local_scripts:
                        name = item[0]
                        arglist, body = local_scripts[name]
                        arglist = tuple(arglist)
                        actual_arglist = tuple(item[1:])

                        assert len(arglist) == len(actual_arglist), \
                            'Mismatched argument list for ' + name + ', ' \
                            + '\n\t'+repr(arglist) + ',\n\t' + repr(actual_arglist)

                        ## expand recursively
                        replacemap = { k:v for (k,v) in zip(arglist,actual_arglist) }
                        last = body
                        while True:
                            def _expand(obj):
                                if isinstance(obj, str):
                                    if obj in replacemap:
                                        return replacemap[obj]
                                    elif obj.startswith('::'):
                                        pprint(replacemap)
                                        assert False, 'Undefined placeholder ' + repr(obj) + ' in ' + name
                                    elif obj.startswith(':_'):
                                        return ":" + name + obj[1:]
                                    else:
                                        return obj
                                elif isinstance(obj,tuple):
                                    return tuple(_expand(o) for o in obj)
                                elif isinstance(obj,list):
                                    return list(_expand(o) for o in obj)
                                else:
                                    return obj

                            body = list(_expand(body))
                            if last == body:
                                break
                            else:
                                last = body
                        for subitem in _(*body):
                            yield subitem

                    else:
                        yield tuple([call_script, 'script_' + item[0]] + list(item[1:]))

                else:
                    yield item

    return list(_(*body))


def y_insert(tree, where, path, new_item):
    '''
    Given a warband TREE, insert a new item.
    
    TREE
       Tree-like nested lists and tuples, as by the module system.
       These generally consist of lists of tuples, where the first
       element of a tuple is normally a case-insensitive ID string.
       
       Typically obtained from a pattern like
       
           def modmerge(var_set):
               game_menus = var_set(game_menus)
               ...
       
    WHERE
       Specifies how the new value should be inserted. Can be:

       'before'
       'after'
       'replace'
          Last item identifies if PATH identifies ID relative to which
          insertion should take place.
          
          If the ID isn't found a warning is emitted and NEW_ITEM is
          placed at the beginning or the end of the parent list.
          
       'beginning'
       'end'
          Add at beginning/end of list identified by PATH.
          
       If the last element of PATH is an integer denoting a tuple index, 
       only 'replace' can be used.

    PATH
       A tuple of ID strings and index integers.
       
       Identifies the parent item, where the item should be inserted.
       
       See ``y_get_path``
       
    NEW_ITEM
       The new tuple to be inserted.
       
       Refer to the corresponding ``module_*.py`` file of the
       original module system for the required format.
       
       
    Examples:

        y_insert(game_menus,'before',('cattle_herd',5,'cattle_drive_away'),('cattle_abc',...))
        y_insert(game_menus,'replace',('cattle_herd',5,'cattle_drive_away'),('cattle_abc',...))
        y_insert(game_menus,'end',('cattle_herd',5),('cattle_abc',...))

    '''
    try:
        parent = y_get_path(tree,path)
    except KeyError:
        raise KeyError('No item', path)

    if isinstance(path[-1],int) and where == 'replace':
        where = 'replace_tuple'

    elif where in ('replace','before','after'):
        parent = y_get_path(tree,path[:-1])
        ref_id = path[-1]
        ref_index, ref_item = y_get(parent, ref_id, True)
        if not ref_item:
            print('Warning: No item', repr(ref_id), 'in', repr(path))
            if where == 'before':
                where = 'beginning'
            elif where == 'after':
                where = 'end'
            elif where == 'replace':
                where = 'beginning'

    if where == 'beginning':
        parent.insert(0, new_item)
    elif where == 'end':
        parent.append(new_item)
    elif where == 'before':
        parent.insert(ref_index, new_item)
    elif where == 'after':
        parent.insert(ref_index+1, new_item)
    elif where == 'replace':
        parent[ref_index] = new_item
    elif where == 'replace_tuple':
        parent2 = y_get_path(tree,path[:-2])
        parent1_idx, parent1 = y_get(parent2,path[-2])
        parent1list = list(parent1)
        parent1list[path[-1]] = new_item
        parent2[parent1_idx] = tuple(parent1list)
    else:
        raise ValueError('Invalid WHERE argument', where)


def y_pprint(treeish):
    '''
    Pretty-print compact.
    '''
    def _short(obj, maxlen=50):
        r = repr(obj)
        return y_symbol(
            r if len(r) <= maxlen else
            r[0:maxlen-3] + '...')

    types = (list, tuple)
    pprint(
        _short(treeish) if not type(treeish) in types else
        type(treeish)((
            _short(item) if not type(item) in types else
            type(item)((
                _short(subitem) for subitem in item))
            for item in treeish)))


def y_pprint_script(script, lindent='    '):
    '''
    Display a script, pretty printing the operations.
    
    SCRIPT
       A list of tuples, representing a script sequence in
       the module system's scripting language.
    '''
    import header_operations
    import header_common
    op_to_name = {}
    reg_to_name = {}
    indent = ' '
    for key,value in vars(header_operations).items():
        if isinstance(value,int):
            op_to_name[value] = key
            op_to_name[neg|value] = 'neg|' + key
            op_to_name[this_or_next|value] = 'this_or_next|' + key
            op_to_name[this_or_next|neg|value] = 'this_or_next|neg|' + key
            
    for key,value in vars(header_common).items():
        if isinstance(value,int) and value & opmask_register != 0:
            reg_to_name[value] = key

    print(indent + '[')
    for line, tup in enumerate(script,0):
        if isinstance(tup,int):
            tup = (tup,)
        
        if isinstance(tup,tuple) and len(tup) >= 1 and isinstance(tup[0],int):
            op = tup[0]
            opname = (
                y_symbol(op_to_name[op]) if op in op_to_name 
                else y_symbol('unknownop_'+str(op)))
            tail = [
                y_symbol(reg_to_name[arg]) if arg in reg_to_name else arg
                for arg in tup[1:] ]

            pretty_tuple = tuple([opname] + tail)
            string = "(" + ', '.join(map(repr,pretty_tuple)) + ")"
        else:
            string = repr(tup)
            if len(string) > 50:
                string = string[:47] + '...'

        if op in (try_end, else_try):
            indent = indent[:-2]

        print(lindent + "%4d:"%line + indent + '  ' + string + ',')

        if (op != try_end and (
                op == else_try or
                op in _TRY_FORMS)):
            indent = indent + '  '

    print(indent + ']')


def y_dump_tree(tree, write=sys.stdout.write):
    '''
    Dump simplified version of TREE, outlining the IDs found inside.

    Output should be valid paths for ``y_get_path``.
    '''

    def _recur(parents,subtree):

        if ((isinstance(subtree,tuple) 
             and len(subtree) > 0 
             and isinstance(subtree[0],str))):
            id = subtree[0]
            print(tuple(parents+[id]))
            for idx,itm in enumerate(subtree[1:],1):
                _recur(parents + [id,idx], itm)
        
        elif isinstance(subtree,list):
            for idx,itm in enumerate(subtree,0):
                _recur(parents, itm)

        else:
            pass

    _recur([],tree)



def y_eq(a,b):
    '''
    Compares two items.
    Case-insensitive if possible.
    '''
    try:
        return a.lower() == b.lower()
    except:
        return a == b


def y_get_path(tree, path):
    '''
    Return item by path, where path is a list of indices (for access
    in tuples) and ids (for access in lists), e.g.
    
        y_get_path(game_menus, ('cattle_herd',5,'cattle_drive_away'))
    '''
    used_ids = []
    rest = tree
    for id in path:
        used_ids.append(id)
        if isinstance(id, int):
            try:
                rest = rest[id]
            except IndexError:
                raise KeyError('No item matching', used_ids)
        elif isinstance(id, str):
            try:
                _, rest = y_get(rest,id)
            except KeyError:
                raise KeyError('No item matching', used_ids)
        else:
            raise ValueError('Invalid PATH', path)
    
    return rest


def y_get(tree, id, noerror=False):
    '''
    Return first item in **tree** which equals **ID** as pair
    **(index, item)**.

    If a string, comparison is not case-sensitive.
    
    With flag NOERROR, returns (None,None) instead of raising an error.
    '''
    for idx, item in enumerate(tree):
        if (isinstance(item,(list,tuple))
            and len(item) >= 1
            and y_eq(item[0], id) ):
            return idx, item
    if noerror:
        return None,None
    else:
        raise KeyError('No item matching', id)
                

def y_find_sequence(tree,sequence,offset=0):
    '''
    Finds start-index of exact occurrence of SEQUENCE in TREE.
    
    OFFSET items at the beginning are skipped (default 0).
    '''
    sequence = tuple(sequence)
    for idx in range(offset, len(tree)-len(sequence)+1):
        tree_sequence = tuple(tree[idx:idx+len(sequence)])
        if tree_sequence == sequence:
            return idx
    raise KeyError('Sequence not in tree', sequence)

def y_find_sequence_range(tree,pattern):
    '''
    Returns (CONTENT,STARTINDEX,ENDINDEX) corresponding to PATTERN.

    PATTERN may contain '*' items, which delimit sequences to look
    for, e.g.
    
        ((try_begin),
         (do_stuff),
         '*',
         (something),
         '*',
         (try_end))
    '''
    parts = [[]]
    for item in pattern:
        if item == '*':
            parts.append([])
        else:
            parts[-1].append(item)
    start = y_find_sequence(tree,parts[0])
    end = start + len(parts[0])
    for part in parts[1:]:
        part_start = y_find_sequence(tree, part, end)
        end = part_start + len(part)
    content = tree[start:end]
    return content,start,end

def y_replace_sequence_range(tree,pattern,replacement,verbose=False):
    '''
    Replaces the region found with ``y_find_sequence_range(TREE,PATTERN)`` with REPLACEMENT.
    '''
    content,start,end = y_find_sequence_range(tree,pattern)
    tree[start:end]= replacement
    if verbose:
        print('========== y_replace_sequence_range ==========')
        print('---------- PATTERN ----------')
        pprint(pattern)
        print('---------- BEFORE ----------')
        pprint(content, indent=2)
        print('---------- AFTER ----------')
        pprint(replacement, indent=2)
        print('==========================================')
    


def y_interact(globals,locals):
    '''
    Start interactive shell during processing, for debugging
    '''
    import code
    var_dict = globals
    var_dict.update(locals)
    code.InteractiveConsole(var_dict).y_interact()

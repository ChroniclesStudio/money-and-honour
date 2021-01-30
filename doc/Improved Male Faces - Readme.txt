Enhanced Male Faces by Iboltax
------------------------------------------

Extract all files into the Warband module directory. So M&B warband Directy/Modules/(Native or whatever)/ , the files in textures go in textures and resources go in resources. 

Its probably a good idea to backup skins.txt in your module, especially if you are installing it in something other than native. 

These lines need to be changed in module.ini to load as mod resources.

Find and Change 

load_resource = textures_face_gen
load_resource = materials_face_gen
load_resource = meshes_face_gen
load_resource = beards
load_resource = hair

to

load_mod_resource = textures_face_gen
load_mod_resource = materials_face_gen
load_mod_resource = meshes_face_gen
load_mod_resource = beards
load_mod_resource = hair


The module_skins.py file is only for people using the module system. You don't need it if you don't know what its for.

If you want to install this into a mod that in some way changes any head related files you might run into issues but it should be fairly easy if you are experienced with the way the modules work.
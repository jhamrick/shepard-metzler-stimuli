import bpy
import utils

# delete everything
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# create the shepard stimulus
stim_id = "x_3_y_2_z_3_x_2"
stim = utils.new_stimulus(stim_id)

# export to .obj
path = "stimuli/obj/{}.obj".format(stim_id)
bpy.ops.export_scene.obj(filepath=path, use_materials=False)

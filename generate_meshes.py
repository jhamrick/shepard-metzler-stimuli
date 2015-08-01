import bpy
import os
import blender_utils as utils

stim_ids = [
    "x_3_y_2_z_3_x_2",
    "x_3_y_2_z_3_x_-2",
    "x_3_y_2_z_2_x_3",
    "x_3_y_2_z_2_x_-3",
    "x_2_y_3_z_3_x_2",
    "x_2_y_3_z_3_x_-2",
    "x_2_y_3_z_2_x_3",
    "x_2_y_3_z_2_x_-3",
    "x_3_y_2_z_3_y_2",
    "x_3_y_2_z_3_y_-2",
    "x_3_y_2_z_2_y_3",
    "x_3_y_2_z_2_y_-3",
    "x_2_y_3_z_3_y_2",
    "x_2_y_3_z_3_y_-2",
    "x_2_y_3_z_2_y_3",
    "x_2_y_3_z_2_y_-3"
]

if not os.path.exists("stimuli"):
    os.mkdir("stimuli")
if not os.path.exists(os.path.join("stimuli", "mesh")):
    os.mkdir(os.path.join("stimuli", "mesh"))

for stim_id in stim_ids:
    for reflect in [True, False]:
        # delete everything
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()

        # create the shepard stimulus
        final_stim_id = "{}_{}".format("A" if not reflect else "B", stim_id)
        stim = utils.new_stimulus(final_stim_id)

        # export to .obj
        path = os.path.join("stimuli", "mesh", "{}.obj".format(final_stim_id))
        bpy.ops.export_scene.obj(filepath=path, use_materials=False)

import bpy
import blender_utils as utils

# delete everything
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# create and position the camera
camera = utils.new_camera("Camera", (-20, -20, 12), (70.5, 0, -45))

# create and position the lights:
#    1. same position as the camera
#    2. above, behind, and to the left of the object
#    3. low and to the right of the object
light1 = utils.new_point_lamp('Lamp1', 1, camera.location)
light2 = utils.new_point_lamp('Lamp2', 2, (1.75, -4, 11.5))
light3 = utils.new_point_lamp('Lamp3', 0.5, (-8, 0, 5))

# add environment lighting
world = bpy.data.worlds["World"]
world.light_settings.use_environment_light = True
world.use_sky_blend = True
world.use_sky_real = True
world.horizon_color = (0.5, 0.5, 0.5)
world.zenith_color = (1, 1, 1)
world.ambient_color = (0, 0, 0)

# create the shepard stimulus
stim_id = "A_x_2_y_3_z_2_x_-3"
bpy.ops.import_scene.obj(filepath="stimuli/mesh/{}.obj".format(stim_id))
stim = bpy.data.objects[stim_id]

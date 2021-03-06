import bpy
import numpy as np
import utils


def new_stimulus(stim_id):
    scene = bpy.data.scenes["Scene"]

    # create the first cube
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.data.objects["Cube"]

    # add a bevel to the cube object
    cube.select = True
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.bevel(offset_type='PERCENT', offset=3, segments=15)
    bpy.ops.object.editmode_toggle()
    cube.select = False

    # parse the stim id into block locations
    block_locs = utils.parse_stim_id(stim_id)
    cube.location = block_locs[0]

    # create copies of the cube to form the full stimulus
    blocks = [cube]
    for i in range(1, len(block_locs)):
        name = "block_{:02d}".format(i)
        mesh = bpy.data.meshes.new(name)
        ob_new = bpy.data.objects.new(name, mesh)
        ob_new.data = cube.data.copy()
        ob_new.data.name = "{}_data".format(name)
        ob_new.scale = cube.scale
        ob_new.location = block_locs[i]
        scene.objects.link(ob_new)
        blocks.append(ob_new)

    # join the blocks together
    bpy.ops.object.select_all(action='DESELECT')
    for block in blocks:
        block.select = True
    bpy.context.scene.objects.active = blocks[-1]
    bpy.ops.object.join()

    # remove double vertices
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.remove_doubles()
    bpy.ops.object.editmode_toggle()

    # reset the center to center of mass, and move to the origin
    stim = bpy.context.scene.objects.active
    bpy.context.scene.cursor_location = (0, 0, 0)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    assert list(stim.location) == [0, 0, 0]

    # set the new name
    stim.name = stim_id
    stim.data.name = stim_id

    # add it to the scene
    scene = bpy.data.scenes["Scene"]
    scene.objects.active = stim
    stim.select = True

    return stim


def new_material(name, stim):
    # set the material properties to something plastic-y
    material = bpy.data.materials.new(name=name)
    material.diffuse_color = (0, 0.3, 0.8)
    material.diffuse_intensity = 0.8
    material.specular_color = (1, 1, 1)
    material.specular_intensity = 0.25
    material.specular_shader = 'WARDISO'
    stim.data.materials.append(material)
    return material


def new_camera(name, location, rotation):
    # create the camera
    data = bpy.data.cameras.new(name=name)
    camera = bpy.data.objects.new(name=name, object_data=data)

    # position the camera
    camera.location = location
    camera.rotation_mode = 'XYZ'
    camera.rotation_euler = np.radians(rotation)

    # add it to the scene
    scene = bpy.data.scenes["Scene"]
    scene.objects.link(camera)
    scene.objects.active = camera
    camera.select = True

    return camera


def new_point_lamp(name, energy, location):
    data = bpy.data.lamps.new(name=name, type='POINT')
    lamp = bpy.data.objects.new(name=name, object_data=data)
    data.energy = energy
    lamp.location = location

    # add it to the scene
    scene = bpy.data.scenes["Scene"]
    scene.objects.link(lamp)
    scene.objects.active = lamp
    lamp.select = True

    return lamp

import numpy as np
import os
import utils
import itertools

from glob import glob
from jinja2 import Template
from colorsys import hls_to_rgb

def rotate_xyz(M, x, y, z):
    sinx = np.sin(np.radians(x))
    cosx = np.cos(np.radians(x))
    Rx = np.array([
        [1, 0, 0],
        [0, cosx, -sinx],
        [0, sinx, cosx]
    ])

    siny = np.sin(np.radians(y))
    cosy = np.cos(np.radians(y))
    Ry = np.array([
        [cosy, 0, siny],
        [0, 1, 0],
        [-siny, 0, cosy]
    ])

    sinz = np.sin(np.radians(z))
    cosz = np.cos(np.radians(z))
    Rz = np.array([
        [cosz, -sinz, 0],
        [sinz, cosz, 0],
        [0, 0, 1]
    ])

    return np.dot(Rz, np.dot(Ry, np.dot(Rx, M.T))).T


if not os.path.exists(os.path.join("stimuli", "scene")):
    os.mkdir(os.path.join("stimuli", "scene"))

with open("resources/scene.xml.j2", "r") as fh:
    template = Template(fh.read())

meshes = sorted(glob("stimuli/mesh/*.obj"))
for mesh in meshes:

    # parse the stim id
    stim_id = os.path.splitext(os.path.basename(mesh))[0]

    # create the directory if it doesn't exist
    if not os.path.exists(os.path.join("stimuli", "scene", stim_id)):
        os.mkdir(os.path.join("stimuli", "scene", stim_id))

    sides = [[0, 0], [0, 90], [0, 180], [0, 270], [90, 0], [270, 0]]
    rots = itertools.product(sides, range(0, 360, 20))
    for (x_rot, z_rot), y_rot in rots:

        # create a seed based on the stimulus id, so we will always pick the same
        # color for a given stimulus
        seed = int(str(np.abs(hash(stim_id[2:])))[:9])
        np.random.seed(seed)

        # generate the color
        rgb = [int(x * 255) for x in hls_to_rgb(np.random.rand(), 0.5, 0.6)]
        color = "#{:02x}{:02x}{:02x}".format(*rgb)

        # figure out the camera position
        block_locs = utils.parse_stim_id(stim_id)
        new_block_locs = rotate_xyz(block_locs, x_rot, z_rot, y_rot)
        z_locs = new_block_locs[:, 2]
        y_trans = cam_look = ((np.max(z_locs) - np.min(z_locs)) / 2.0) + 10

        # render the template
        scene = template.render(
            stim_id=stim_id, color=color, cam_look=cam_look,
            x_rot=x_rot, y_rot=y_rot, z_rot=z_rot, y_trans=y_trans)

        # save it out to file
        scene_name = "{}_xrot_{:03d}_zrot_{:03d}_yrot_{:03d}.xml".format(stim_id, x_rot, z_rot, y_rot)
        scene_path = os.path.join("stimuli", "scene", stim_id, scene_name)
        print(scene_path)
        with open(scene_path, "w") as fh:
            fh.write(scene)

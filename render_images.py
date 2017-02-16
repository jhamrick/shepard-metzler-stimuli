import subprocess as sp
import os
import sys

from glob import glob

extra_args = sys.argv[1:]

if not os.path.exists(os.path.join("stimuli", "image")):
    os.mkdir(os.path.join("stimuli", "image"))

scenes = glob("stimuli/scene/*.xml")
for stim_id in sorted(os.listdir(os.path.join("stimuli", "scene"))):
    if not os.path.exists(os.path.join("stimuli", "image", stim_id)):
        os.mkdir(os.path.join("stimuli", "image", stim_id))

    for scene in sorted(glob(os.path.join("stimuli", "scene", stim_id, "*.xml"))):
        filename = "{}.png".format(os.path.splitext(os.path.basename(scene))[0])
        result = os.path.join("stimuli", "image", stim_id, filename)
        if os.path.exits(filename):
            print("Already exists: {}".format(filename))
            continue

        cmd = ["mitsuba", "-x"] + extra_args + ["-o", result, scene]
        sp.check_call(cmd)

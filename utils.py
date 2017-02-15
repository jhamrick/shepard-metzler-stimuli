import numpy as np


def parse_stim_id(stim_id):
    parts = stim_id.split("_")
    if parts[0] == "A":
        reflect = False
    elif parts[0] == "B":
        reflect = True
    else:
        raise ValueError(stim_id)
    parts = parts[1:]
    block_locs = [(0, 0, 0)]

    for i in range(0, len(parts), 2):
        coord = parts[i]
        num = int(parts[i + 1])
        if num < 0:
            direction = -1
        else:
            direction = 1
        scale = 2 * direction
        for _ in range(np.abs(num)):
            x, y, z = block_locs[-1]
            if coord == 'x':
                x += scale
            elif coord == 'y':
                y += scale
            elif coord == 'z':
                z += scale
            block_locs.append((x, y, z))

    # we actually have one block too many, so get rid of the first block and
    # then adjust the rest of the blocks
    block_locs = np.array(block_locs[1:], dtype=float)
    block_locs -= block_locs[0]

    # now center the block locations
    center = (block_locs.min(axis=0) + block_locs.max(axis=0)) / 2.0
    block_locs -= center

    # reflect across the y-axis
    if reflect:
        block_locs[:, 1] *= -1

    return block_locs

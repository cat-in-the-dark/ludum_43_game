import random

import jvcr

colors = [
    (130, 231, 127, 0),
    (0, 1, 0, 0xFF),
    (28, 17, 44, 0xFF),
    (49, 18, 22, 0xFF),
    (29, 24, 85, 0xFF),
    (144, 19, 102, 0xFF),
    (181, 34, 14, 0xFF),
    (113, 85, 46, 0xFF),
    (64, 87, 222, 0xFF),
    (174, 93, 36, 0xFF),
    (185, 110, 40, 0xFF),
    (246, 101, 13, 0xFF),
    (246, 92, 144, 0xFF),
    (16, 193, 244, 0xFF),
    (81, 197, 38, 0xFF),
    (239, 186, 68, 0xFF),
    (255, 180, 137, 0xFF),
    (255, 253, 238, 0xFF),
]


def setup_palette():
    for i, rgb in enumerate(colors):
        jvcr.set_pallet(i, *rgb)


def suffle_palette():
    random.shuffle(colors)
    setup_palette()


def setup_sprites():
    jvcr.import_sprites("assets/atlas.png", 0)

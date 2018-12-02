import random

import jvcr

colors = [
    (241, 52, 146, 0),
    (0, 0, 0, 0xFF),
    (40, 11, 38, 0xFF),
    (26, 17, 46, 0xFF),
    (47, 19, 22, 0xFF),
    (27, 24, 83, 0xFF),
    (143, 23, 103, 0xFF),
    (180, 35, 19, 0xFF),
    (70, 91, 231, 0xFF),
    (175, 93, 35, 0xFF),
    (244, 104, 11, 0xFF),
    (244, 93, 146, 0xFF),
    (42, 192, 242, 0xFF),
    (87, 197, 43, 0xFF),
    (254, 181, 139, 0xFF),
    (244, 192, 71, 0xFF),
    (255, 253, 240, 0xFF)
]


def setup_palette():
    for i, rgb in enumerate(colors):
        jvcr.set_pallet(i, *rgb)


def suffle_palette():
    random.shuffle(colors)
    setup_palette()


def setup_sprites():
    jvcr.import_sprites("assets/atlas0.png", 0)

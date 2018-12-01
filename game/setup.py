import jvcr


def setup_palette():
    jvcr.set_pallet(0, 21, 10, 31)
    jvcr.set_pallet(1, 0, 0, 0)
    jvcr.set_pallet(2, 244, 104, 11)
    jvcr.set_pallet(3, 180, 35, 19)
    jvcr.set_pallet(4, 244, 192, 71)
    jvcr.set_pallet(5, 42, 192, 242)
    jvcr.set_pallet(6, 40, 11, 38)
    jvcr.set_pallet(7, 244, 93, 146)
    jvcr.set_pallet(8, 175, 93, 35)
    jvcr.set_pallet(9, 143, 23, 103)
    jvcr.set_pallet(10, 70, 91, 231)
    jvcr.set_pallet(11, 40, 11, 38)
    jvcr.set_pallet(12, 26, 17, 46)
    jvcr.set_pallet(13, 47, 19, 22)
    jvcr.set_pallet(14, 254, 181, 139)
    jvcr.set_pallet(15, 87, 197, 43)
    jvcr.set_pallet(16, 255, 253, 240)


def setup_sprites():
    jvcr.import_sprites("assets/background1.png", 0)

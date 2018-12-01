import jvcr


def init():
    jvcr.import_sprites("man.png", 0)


def update(dt):
    jvcr.cls(1)

    jvcr.spr(0, 0, 0, 0, 256, 144, 0, 0, 0)

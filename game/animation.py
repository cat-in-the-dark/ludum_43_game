import jvcr


class Animation:
    """
    anim = Animation(sprites=((0, 64), (16, 64), (32, 64), (48, 64)), width=16, height=16)

    def init():
        jvcr.import_sprites("sprites.png", 0)

    def update(dt):
        anim.draw(dt=dt, x=0, y=0)
    """

    def __init__(self, sprites, width, height, cycle=True, speed=10) -> None:
        self.width = width
        self.height = height
        self.speed = speed
        self.cycle = cycle
        self._sprites = sprites
        self._time = 0
        self.full_cycle = False

    def draw(self, dt, x, y, flip=0, rotate=0, scale=1):
        self._time += dt
        index = -1
        if not self.full_cycle:
            index = int(self._time * self.speed) % len(self._sprites)
            if index == len(self._sprites) - 1 and not self.cycle:
                self.full_cycle = True
        sprite = self._sprites[index]
        jvcr.spr(x, y, sprite[0], sprite[1], self.width, self.height, flip, rotate, scale)

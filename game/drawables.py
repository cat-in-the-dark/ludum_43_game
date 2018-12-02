from abc import abstractmethod
from jvcr import spr

from animation import Animation


class Drawable:
    def __init__(self) -> None:
        self.width = 16
        self.height = 16

    @abstractmethod
    def draw(self, x, y, dt):
        pass


class BatteryBarDrawable(Drawable):
    def draw(self, x, y, dt):
        spr(x, y, 0, 41 * 16, 32, 48, 0, 0, 0)


class SelectBarDrawable(Drawable):
    def draw(self, x, y, dt):
        spr(x, y, 28 * 16, 0, 32, 16 * 6, 0, 0, 0)


class LoseDrawable(Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.animation = Animation(sprites=(
            (448, 288),
            (0, 27 * 16),
            (1 * 40, 27 * 16),
            (2 * 40, 27 * 16),
            (3 * 40, 27 * 16),
            (4 * 40, 27 * 16),
            (5 * 40, 27 * 16),
            (6 * 40, 27 * 16),
            (7 * 40, 27 * 16),
            (8 * 40, 27 * 16),
            (9 * 40, 27 * 16),
            (10 * 40, 27 * 16),
            (11 * 40, 27 * 16)
        ), width=40, height=56, speed=10, cycle=False)

    def draw(self, x, y, dt):
        self.animation.draw(dt, x, y)

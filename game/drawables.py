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


class Table(Drawable):
    def draw(self, x, y, dt):
        spr(x, y, 4 * 16, 46 * 16, 16, 16, 0, 0, 0)


class Sofa(Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.width = 32

    def draw(self, x, y, dt):
        spr(x, y, 5 * 16, 46 * 16, 32, 16, 0, 0, 0)


class WeightBell(Drawable):
    def draw(self, x, y, dt):
        spr(x, y, 7 * 16, 46 * 16, 16, 16, 0, 0, 0)


class Cupboard(Drawable):
    def draw(self, x, y, dt):
        spr(x, y, 8 * 16, 46 * 16, 16, 16, 0, 0, 0)


class Gnome(Drawable):
    def draw(self, x, y, dt):
        spr(x, y, 9 * 16, 46 * 16, 16, 16, 0, 0, 0)


class PS4(Drawable):
    def draw(self, x, y, dt):
        spr(x, y, 10 * 16, 46 * 16, 16, 16, 0, 0, 0)


class Wakuum(Drawable):
    def draw(self, x, y, dt):
        spr(x, y, 11 * 16, 46 * 16, 16, 16, 0, 0, 0)


class Cat(Drawable):
    def draw(self, x, y, dt):
        spr(x, y, 12 * 16, 46 * 16, 16, 16, 0, 0, 0)


class LongBoard(Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.width = 32

    def draw(self, x, y, dt):
        spr(x, y, 13 * 16, 46 * 16, 32, 16, 0, 0, 0)


class CompTable(Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.height = 32

    def draw(self, x, y, dt):
        spr(x, y, 15 * 16, 46 * 16, 16, 32, 0, 0, 0)


class PlayerGoLeft(Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.animation = Animation(sprites=(
            (20 * 16, 36 * 16),
            (21 * 16, 36 * 16),
            (22 * 16, 36 * 16),
            (23 * 16, 36 * 16),
            (24 * 16, 36 * 16),
            (24 * 16, 36 * 16),
            (26 * 16, 36 * 16),
            (27 * 16, 36 * 16),
            (28 * 16, 36 * 16),
            (29 * 16, 36 * 16),
            (30 * 16, 36 * 16),
            (31 * 16, 36 * 16),
        ), width=16, height=32, speed=12, cycle=True)

    def draw(self, x, y, dt):
        self.animation.draw(dt, x, y)


class PlayerGoRight(Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.animation = Animation(sprites=(
            (20 * 16, 38 * 16),
            (21 * 16, 38 * 16),
            (22 * 16, 38 * 16),
            (23 * 16, 38 * 16),
            (24 * 16, 38 * 16),
            (24 * 16, 38 * 16),
            (26 * 16, 38 * 16),
            (27 * 16, 38 * 16),
            (28 * 16, 38 * 16),
            (29 * 16, 38 * 16),
            (30 * 16, 38 * 16),
            (31 * 16, 38 * 16),
        ), width=16, height=32, speed=12, cycle=True)

    def draw(self, x, y, dt):
        self.animation.draw(dt, x, y)

class PlayerGoUp(Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.animation = Animation(sprites=(
            (20 * 16, 40 * 16),
            (21 * 16, 40 * 16),
            (22 * 16, 40 * 16),
            (23 * 16, 40 * 16),
            (24 * 16, 40 * 16),
        ), width=16, height=32, speed=8, cycle=True)

    def draw(self, x, y, dt):
        self.animation.draw(dt, x, y)

class PlayerGoDown(Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.animation = Animation(sprites=(
            (20 * 16, 42 * 16),
            (21 * 16, 42 * 16),
            (22 * 16, 42 * 16),
            (26 * 16, 40 * 16),
        ), width=16, height=32, speed=6, cycle=True)

    def draw(self, x, y, dt):
        self.animation.draw(dt, x, y)
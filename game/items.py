import jvcr

from animation import Animation
from item import ItemType


class Item:
    def __init__(self) -> None:
        self.width = 16
        self.height = 16
        self._color = 0
        self.type = -1

    def draw(self, x, y, dt):
        jvcr.rectfill(x, y, self.width, self.height, self._color)

    def __repr__(self) -> str:
        return self.__class__.__name__


class FloorItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self.type = ItemType.FLOOR

    def draw(self, x, y, dt):
        # nothing to do
        pass


class ExitItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self.type = ItemType.EXIT_POINT
        self.animation = Animation(sprites=(
            (0, 46 * 16),
            (1 * 16, 46 * 16),
            (2 * 16, 46 * 16),
            (3 * 16, 46 * 16)
        ), width=16, height=16, speed=10)

    def draw(self, x, y, dt):
        self.animation.draw(dt, x, y)


class BlockItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self._color = 4
        self.type = ItemType.BLOCK

    def draw(self, x, y, dt):
        jvcr.spr(x, y, 4*16, 46 * 16, 16, 16, 0, 0, 0)


class ReverseItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self._color = 5
        self.type = ItemType.REVERSE

    def draw(self, x, y, dt):
        jvcr.spr(x, y, 20 * 16, 47 * 16, 16, 16, 0, 0, 0)


class RandTurnItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self._color = 7
        self.type = ItemType.RND_TURN

    def draw(self, x, y, dt):
        jvcr.spr(x, y, 18 * 16, 47 * 16, 16, 16, 0, 0, 0)


ITEMS_MAPPING = {
    ItemType.FLOOR: FloorItem,
    ItemType.BLOCK: BlockItem,
    ItemType.REVERSE: ReverseItem,
    ItemType.RND_TURN: RandTurnItem,
    ItemType.EXIT_POINT: ExitItem
}

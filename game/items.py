import jvcr

from animation import Animation

import drawables as dw
from item_type import ItemType
import random

_BLOCK_ITEM_DRAWABLES = [dw.Table, dw.WeightBell, dw.Cupboard, dw.Gnome, dw.PS4, dw.Wakuum, dw.Cat]


class Item:
    def __init__(self) -> None:
        self.width = 16
        self.height = 16
        self.type = -1

    def draw(self, x, y, dt):
        pass

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
        self.type = ItemType.BLOCK
        i = random.randint(0, len(_BLOCK_ITEM_DRAWABLES) -1)
        self.drawable = _BLOCK_ITEM_DRAWABLES[i]()

    def draw(self, x, y, dt):
        self.drawable.draw(x, y, dt)


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

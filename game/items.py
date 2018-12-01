import jvcr

from item import ItemType


class Item:
    def __init__(self) -> None:
        self.width = 16
        self.height = 16
        self._color = 0
        self.type = -1

    def draw(self, x, y):
        jvcr.rectfill(x, y, self.width, self.height, self._color)


class BlockItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self._color = 4
        self.type = ItemType.BLOCK


class ReverseItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self._color = 5
        self.type = ItemType.REVERSE


class RandTurnItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self._color = 7
        self.type = ItemType.RND_TURN

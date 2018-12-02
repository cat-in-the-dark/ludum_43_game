from drawables import SelectBarDrawable
from items import Item, ITEMS_MAPPING
from levels import LEVELS


class ItemsStack:
    def __init__(self, level):
        items = LEVELS[level]['stack']
        self._items = [ITEMS_MAPPING[t]() for t in items]
        self.draw_limit = 3
        self.sbar_draw = SelectBarDrawable()

    def update(self, dt):
        self.sbar_draw.draw(0, 16 * 3, dt)
        for pos, i in enumerate(self._items):
            if pos < self.draw_limit:
                i.draw(8, 48 +8 + pos * (i.height +16), dt)

    def top(self):
        return self._items[0]

    def is_empty(self):
        return len(self._items) < 1

    def pop(self) -> Item:
        if not self.is_empty():
            return self._items.pop(0)

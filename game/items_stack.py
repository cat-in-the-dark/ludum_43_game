class ItemsStack:
    def __init__(self, items):
        self._items = [i() for i in items]
        self.draw_limit = 5

    def update(self, dt):
        for pos, i in enumerate(self._items):
            if pos < self.draw_limit:
                i.draw(16, 48 + pos * i.height)

    def top(self):
        return self._items[0]

    def isEmpty(self):
        return len(self._items) < 1

    def pop(self):
        if not self.isEmpty():
            return self._items.pop(0)
        else:
            return None
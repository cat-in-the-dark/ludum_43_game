import jvcr

from inputs import InputEx
from items_stack import ItemsStack
from levels import LEVELS, store_tile, setup_tiles, get_tiles
from pointer import Pointer
from route_machine import Scene


class BuildScene(Scene):
    def __init__(self, storage) -> None:
        self.storage = storage
        self.pointer = Pointer(x=48, y=16)
        self.inp = InputEx()
        self.finish = False
        self.level = 0
        self.stack: ItemsStack = None
        self.MIN_LEFT = 48
        self.MIN_TOP = 16

    def on_activate(self):
        if self.level >= len(LEVELS):
            print("Rest levels")
            self.level = 0
        print("LEVEL {}".format(self.level))
        self.stack = ItemsStack(LEVELS[self.level]['stack'])
        setup_tiles(self.storage, self.level)

    def update(self, dt):
        jvcr.spr(32, 0, 0, 0, 240, 144, 0, 0, 0)
        self.pointer.update(dt)
        self.inp.update(dt)
        self.stack.update(dt)

        for i, line in enumerate(get_tiles(self.storage)):
            for j, tile in enumerate(line):
                x = i * tile.width + self.MIN_LEFT
                y = j * tile.height + self.MIN_TOP
                tile.draw(x, y, dt)

        if self.inp.btnp(jvcr.BTN_UP, 0):
            self.pointer.move_up()
        if self.inp.btnp(jvcr.BTN_DOWN, 0):
            self.pointer.move_down()
        if self.inp.btnp(jvcr.BTN_LEFT, 0):
            self.pointer.move_left()
        if self.inp.btnp(jvcr.BTN_RIGHT, 0):
            self.pointer.move_right()
        if self.inp.btnp(jvcr.BTN_A, 0):
            return self._put_item()

    def on_exit(self):
        self.level += 1

    def _put_item(self):
        item = self.stack.pop()
        if item is not None:
            store_tile(self.storage, item.type, self.pointer.get_x(), self.pointer.get_y())
            return None
        else:
            return "next"

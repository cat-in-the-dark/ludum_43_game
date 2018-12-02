import jvcr

from inputs import InputEx
from items_stack import ItemsStack
from levels import LEVELS
from pointer import Pointer
from route_machine import Scene


class BuildScene(Scene):
    def __init__(self, save_tile) -> None:
        self.pointer = Pointer(x=48, y=16)
        self.inp = InputEx()
        self.save_tile = save_tile
        self.finish = False
        self.level = 0
        self.stack: ItemsStack = None

    def on_activate(self):
        if self.level >= len(LEVELS):
            print("Rest levels")
            self.level = 0
        print("LEVEL {}".format(self.level))
        self.stack = ItemsStack(LEVELS[self.level]['stack'])

    def update(self, dt):
        jvcr.spr(32, 0, 0, 0, 240, 144, 0, 0, 0)
        self.pointer.update(dt)
        self.inp.update(dt)
        self.stack.update(dt)

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
            self.save_tile(item.type, self.pointer.x, self.pointer.y)
            return None
        else:
            return "next"

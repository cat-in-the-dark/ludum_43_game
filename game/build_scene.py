import jvcr

from build_scene import ItemsStack
from inputs import InputEx
from levels import LEVELS
from pointer import Pointer


class BuildScene:
    def __init__(self, save_tile) -> None:
        self.pointer = Pointer(x=48, y=16)
        self.inp = InputEx()
        self.stack = ItemsStack(LEVELS[0]['stack'])
        self.save_tile = save_tile
        self.finish = False

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
            self._put_item()

    def _put_item(self):
        item = self.stack.pop()
        if item is not None:
            self.save_tile(item.type, self.pointer.x, self.pointer.y)
        else:
            print("Nothing to put")
            self.finish = True

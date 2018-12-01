from pointer import Pointer
from jvcr import btn
import jvcr
from inputs import InputEx


class BuildScene:
    def __init__(self) -> None:
        self.pointer = Pointer(x=48, y=16)
        self.inp = InputEx()

    def update(self, dt):
        jvcr.spr(32, 0, 0, 0, 240, 144, 0, 0, 0)
        self.pointer.update(dt)
        self.inp.update(dt)

        if self.inp.btnp(jvcr.BTN_UP, 0):
            self.pointer.move_up()
        if self.inp.btnp(jvcr.BTN_DOWN, 0):
            self.pointer.move_down()
        if self.inp.btnp(jvcr.BTN_LEFT, 0):
            self.pointer.move_left()
        if self.inp.btnp(jvcr.BTN_RIGHT, 0):
            self.pointer.move_right()

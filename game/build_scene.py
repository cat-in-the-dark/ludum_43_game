import jvcr

from drawables import BatteryBarDrawable
from inputs import InputEx
from items_stack import ItemsStack
from levels import LEVELS, store_tile, setup_tiles, get_tiles, can_store_tile
from pointer import Pointer
from route_machine import Scene
from setup import suffle_palette


class BuildScene(Scene):
    def __init__(self, storage) -> None:
        self.storage = storage
        self.pointer = Pointer(x=48, y=16)
        self.inp = InputEx()
        self.finish = False
        self.stack: ItemsStack = None
        self.MIN_LEFT = 48
        self.MIN_TOP = 16

        self.bar_draw = BatteryBarDrawable()

    def on_activate(self):
        if self.storage['level'] >= len(LEVELS):
            print("Reset levels")
            self.storage['level'] = 0
        print("LEVEL {}".format(self.storage['level']))
        self.stack = ItemsStack(self.storage['level'])
        setup_tiles(self.storage, self.storage['level'])

    def update(self, dt):
        self.draw_back(dt)
        self.inp.update(dt)
        self.stack.update(dt)
        self.draw_tiles(dt)
        self.pointer.update(dt)
        self.bar_draw.draw(0, 0, dt)

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
        if self.inp.btnp(jvcr.BTN_X, 0):
            suffle_palette()

    def draw_tiles(self, dt):
        for j, line in enumerate(get_tiles(self.storage)):
            for i, tile in enumerate(line):
                x = i * tile.width + self.MIN_LEFT
                y = j * tile.height + self.MIN_TOP
                tile.draw(x, y, dt)

    def draw_back(self, dt):
        px, py = LEVELS[self.storage['level']]['spr']
        jvcr.spr(32, 0, px, py, 240, 144, 0, 0, 0)

    def _put_item(self):
        if can_store_tile(self.storage, self.pointer.get_x(), self.pointer.get_y()):
            print("PUT ITEM")
            item = self.stack.pop()
            if item is not None:
                store_tile(self.storage, item, self.pointer.get_x(), self.pointer.get_y())
            else:
                return "next"
        else:
            print("Can't put item at [{}, {}]".format(self.pointer.get_x(), self.pointer.get_y()))
        return None

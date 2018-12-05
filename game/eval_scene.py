from drawables import PlayerGoLeft, PlayerGoRight, PlayerGoUp, PlayerGoDown, BatteryBarDrawable
from levels import get_tiles, LEVELS
from main import Ctx, Player, Direction
from route_machine import Scene
import jvcr


class EvalScene(Scene):
    def __init__(self, storage) -> None:
        self.storage = storage
        self.player_left = PlayerGoLeft()
        self.player_right = PlayerGoRight()
        self.player_up = PlayerGoUp()
        self.player_down = PlayerGoDown()

        self.bar_draw = BatteryBarDrawable()
        self.MIN_LEFT = 48
        self.MIN_TOP = 16

    def on_activate(self):
        pass

    def update(self, dt) -> str:
        jvcr.cls(5)
        self.player_left.draw(0, 0, dt)
        self.player_right.draw(16, 0, dt)
        self.player_up.draw(32, 0, dt)
        self.player_down.draw(48, 0, dt)

        self.draw_back(dt)
        self.draw_tiles(dt)
        self.bar_draw.draw(0, 0, dt)

    def draw_back(self, dt):
        px, py = LEVELS[self.storage['level']]['spr']
        jvcr.spr(32, 0, px, py, 240, 144, 0, 0, 0)

    def draw_tiles(self, dt):
        for j, line in enumerate(get_tiles(self.storage)):
            for i, tile in enumerate(line):
                x = i * tile.width + self.MIN_LEFT
                y = j * tile.height + self.MIN_TOP
                tile.draw(x, y, dt)

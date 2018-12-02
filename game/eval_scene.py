from drawables import PlayerGoLeft, PlayerGoRight, PlayerGoUp, PlayerGoDown
from levels import get_tiles
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

    def on_activate(self):
        pass

    def update(self, dt) -> str:
        jvcr.cls(5)
        self.player_left.draw(0, 0, dt)
        self.player_right.draw(16, 0, dt)
        self.player_up.draw(32, 0, dt)
        self.player_down.draw(48, 0, dt)

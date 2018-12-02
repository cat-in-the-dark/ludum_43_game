from levels import get_tiles
from main import Ctx, Player, Direction
from route_machine import Scene


class EvalScene(Scene):
    def __init__(self, storage) -> None:
        self.ctx: Ctx = None
        self.storage = storage

    def on_activate(self):
        player = Player(x=0, y=0, dir=Direction.UP)
        room = get_tiles(self.storage)
        self.ctx = Ctx(room, player)

    def update(self, dt) -> str:
        # jvcr.print("GAME", 1, 1, 8)
        #
        # if jvcr.btn(jvcr.BTN_UP, 0):
        #     return "win"
        # if jvcr.btn(jvcr.BTN_DOWN, 0):
        #     return "lose"
        self.ctx.render()

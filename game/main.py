import jvcr
from item import ItemType


UNIVERSE_HEIGHT = 7
UNIVERSE_WIDTH  = 12


class Direction:
    UP    = 0
    DOWN  = 1
    LEFT  = 2
    RIGTH = 3


def render_item(x, y, it):
    jvcr.rectfill(x, y, 16, 16, it + 3) # tmp hack
    

class Player:
    def __init__(self, x, y, dir):
        self.x   = x
        self.y   = y
        self.dir = dir

    def render(self):
        jvcr.rectfill(self.x, self.y, 16, 16, 15)


class Ctx:
    def __init__(self, player):
        self.universe = [[ItemType.rnd() for _ in range(UNIVERSE_WIDTH)] for _ in range(UNIVERSE_HEIGHT)]
        self.player = player
    
    def render(self):
        self.player.render()

        for i, line in enumerate(self.universe):
            for j, item in enumerate(line):
                render_item((j + 3) * 16, (i + 1) * 16, item)

    def step(self):
        if self.player.dir == Direction.UP:
            pass

    def is_game_end(self):
        return False


ctx = Ctx(Player(x=0, y=0, dir=Direction.UP))


def update(dt):
    jvcr.cls(1)

    if not ctx.is_game_end():
        ctx.render()
        ctx.step()


    # jvcr.print("Hello World!", 1 , 1, 8)
    # jvcr.print("JVCR_ECM_01\nLOL\nWAT\rOMG", 1, 10, 10)

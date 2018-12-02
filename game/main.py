import jvcr

from item_type import ItemType

UNIVERSE_HEIGHT = 7
UNIVERSE_WIDTH  = 12
START_OFFSET = 7 * 16


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
        jvcr.rectfill(self.x, START_OFFSET - self.y * 16, 16, 16, 15)


class Ctx:
    def __init__(self, universe, player):
        self.universe = universe
        self.player = player
    
    def render(self):
        self.player.render()

        for i, line in enumerate(self.universe):
            for j, item in enumerate(line):
                render_item((j + 3) * 16, START_OFFSET - i * 16, item)

    def next_pos(self):
        x, y, dir = (self.player.x, self.player.y, self.player.dir)

        if dir   == Direction.UP:
            return x, y + 1 if y + 1 < UNIVERSE_HEIGHT else y
        elif dir == Direction.DOWN:
            return x, y - 1
        elif dir == Direction.LEFT:
            return x - 1, y
        elif dir == Direction.RIGTH:
            return x + 1, y

    def step(self):
        nx, ny = self.next_pos()
        n_item = universe[nx][ny]

        if n_item == ItemType.FLOOR:
            self.player.x = nx
            self.player.y = ny

    def is_game_end(self):
        return False


#universe = [[ItemType.rnd() for _ in range(UNIVERSE_WIDTH)] for _ in range(UNIVERSE_HEIGHT)]
universe = [[0] * 12] * 7
player = Player(x=0, y=0, dir=Direction.UP)
ctx = Ctx(universe, player)


def update(dt):
    jvcr.cls(1)

    if not ctx.is_game_end():
        ctx.render()
        ctx.step()


    # jvcr.print("Hello World!", 1 , 1, 8)
    # jvcr.print("JVCR_ECM_01\nLOL\nWAT\rOMG", 1, 10, 10)

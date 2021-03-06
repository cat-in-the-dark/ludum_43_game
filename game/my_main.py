import jvcr

import setup
from build_scene import BuildScene
from eval_scene import EvalScene
from game_over_scene import GameOverScene
from game_win_scene import GameWinScene
from route_machine import RouteMachine
from title_scene import TitleScene

rm = RouteMachine()


def init():
    setup.setup_palette()
    setup.setup_sprites()

    storage = {
        'level': 0
    }

    title = TitleScene()
    build = BuildScene(storage)
    eval_ = EvalScene(storage)
    over = GameOverScene(storage)
    win = GameWinScene(storage)

    rm.add_route(title, build, "next")
    rm.add_route(build, eval_, "next")
    rm.add_route(eval_, over, "lose")
    rm.add_route(eval_, win, "win")
    rm.add_route(over, title, "next")
    rm.add_route(win, title, "next")

    # FOR TESTING
    # rm.add_route(build, build, "next")

    rm.start(title)


def update(dt):
    jvcr.cls(1)
    rm.update(dt)

import jvcr

from route_machine import Scene


class EvalScene(Scene):
    def update(self, dt) -> str:
        jvcr.print("GAME", 1, 1, 8)

        if jvcr.btn(jvcr.BTN_UP, 0):
            return "win"
        if jvcr.btn(jvcr.BTN_DOWN, 0):
            return "lose"

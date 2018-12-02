import jvcr

from route_machine import Scene


class GameWinScene(Scene):
    def __init__(self, storage) -> None:
        self.storage = storage

    def update(self, dt) -> str:
        jvcr.print("You WON!", 1, 1, 8)
        jvcr.print("press Z", 10, 10, 5)
        if jvcr.btn(jvcr.BTN_A, 0):
            return "next"

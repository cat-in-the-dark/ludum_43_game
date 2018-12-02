import jvcr

from route_machine import Scene


class TitleScene(Scene):
    def __init__(self) -> None:
        self.timer = 0

    def on_activate(self):
        self.timer = 0

    def update(self, dt) -> str:
        self.timer += dt
        jvcr.print("CAT_IN_THE_DARK", 1, 1, 8)

        if self.timer > 2:
            return "next"
        if self.timer > 0.5 and jvcr.btn(jvcr.BTN_B, 0):
            return "next"

import jvcr

from drawables import LoseDrawable
from route_machine import Scene


class GameOverScene(Scene):
    def __init__(self, storage) -> None:
        self.storage = storage
        self.lose_draw = LoseDrawable()

    def update(self, dt) -> str:
        x = (jvcr.DISPLAY_WIDTH - self.lose_draw.width) // 2
        y = (jvcr.DISPLAY_HEIGHT - self.lose_draw.height) // 2
        self.lose_draw.draw(x, y - 32, dt)
        jvcr.print("press Z", x - 8, y + 32, 5)
        if jvcr.btn(jvcr.BTN_A, 0):
            return "next"

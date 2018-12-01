import jvcr


class Pointer:
    def __init__(self, x=0, y=0, color=16) -> None:
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.min_width = 4
        self.min_height = 4
        self.width_grows = 12
        self.height_grows = 12
        self.color = color

        self.timer = 0.0
        self.timer_dir = 1

        self.MIN_LEFT = 48
        self.MAX_RIGHT = jvcr.DISPLAY_WIDTH - self.width - 16
        self.MIN_TOP = 16
        self.MAX_BOTTOM = jvcr.DISPLAY_HEIGHT - self.height - 16

    def update(self, dt):
        self.timer += dt * self.timer_dir
        if self.timer > 0.5:
            self.timer_dir = -1
        if self.timer < 0:
            self.timer_dir = 1
        width = self.min_width + ((self.width_grows * self.timer) // 2) * 2
        height = self.min_height + ((self.height_grows * self.timer) // 2) * 2
        x = self.x + (self.width - width) // 2
        y = self.y + (self.height - height) // 2
        jvcr.line(x, y, x + width, y + height, self.color)
        jvcr.line(x + width, y, x, y + height, self.color)

    def move_up(self):
        if self.y > self.MIN_TOP:
            self.y -= self.height

    def move_down(self):
        if self.y < self.MAX_BOTTOM:
            self.y += self.height

    def move_left(self):
        if self.x > self.MIN_LEFT:
            self.x -= self.width

    def move_right(self):
        if self.x < self.MAX_RIGHT:
            self.x += self.width

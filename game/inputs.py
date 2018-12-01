import jvcr


class InputEx:
    def __init__(self, release_time=0.2) -> None:
        self.release_time = release_time
        self._history = {}

    def btnp(self, id, player_id=0):
        if jvcr.btn(id, player_id):
            time_not_pressed = self._history.get(id, self.release_time + 0.1)
            if time_not_pressed >= self.release_time:
                self._history[id] = 0
                return True
        return False

    def update(self, dt):
        for key in self._history:
            self._history[key] += dt

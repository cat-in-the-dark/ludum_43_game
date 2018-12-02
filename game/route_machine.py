class Scene:
    def update(self, dt) -> str:
        pass

    def on_exit(self):
        pass

    def on_activate(self):
        pass


class RouteMachine:
    def __init__(self) -> None:
        self.routes = {}
        self.current: Scene = None

    def add_route(self, from_: Scene, to: Scene, action: str):
        self.routes[from_] = self.routes.get(from_, {})
        self.routes[from_][action] = to

    def start(self, from_: Scene):
        self.current = from_
        self.current.on_activate()

    def on_exit(self):
        self.current.on_exit()

    def update(self, dt):
        action = self.current.update(dt)
        if action is not None:
            self._do_route(action)

    def _do_route(self, action):
        to = self.routes.get(self.current, {}).get(action, None)
        if to is None:
            print("WARNING. No transition from {} with action {}".format(self.current, action))
            return
        print("Transit from {} to {} with action {}".format(self.current, to, action))
        self.current.on_exit()
        self.current = to
        self.current.on_activate()

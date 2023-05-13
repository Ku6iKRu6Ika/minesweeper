from .abc import Entity


class Panel(Entity):
    def __init__(self, height):
        self.height = height

    def draw(self, display):
        pass

class Screen:
    _game = None

    @property
    def game(self):
        return self._game

    def set_controller(self, game):
        self._game = game

    def start(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

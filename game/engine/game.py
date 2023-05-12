import pygame

from .const import *


class Game:
    _screen = None

    def __init__(
            self,
            width,
            height,
            caption,
            fps
    ):
        pygame.display.set_caption(caption)

        self._width = width
        self._height = height
        self._display = pygame.display.set_mode((width, height))

        self._fps = fps
        self._clock = pygame.time.Clock()
        self._running = False

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def display(self):
        return self._display

    @property
    def screen(self):
        return self._screen

    @property
    def fps(self):
        return self._fps

    @property
    def running(self):
        return self._running

    def set_screen(self, screen):
        self._screen = screen
        self.screen.set_controller(self)

    @staticmethod
    def set_music(music):
        music.play()

    @staticmethod
    def stop_music():
        pygame.mixer.music.pause()

    @staticmethod
    def set_caption(caption):
        pygame.display.set_caption(caption)

    @staticmethod
    def set_icon(image):
        pygame.display.set_icon(image)

    def set_fps(self, fps):
        self._fps = fps

    def start(self, screen):
        self._running = True

        self.set_screen(screen)
        self.screen.start()

        while self._running:
            self._clock.tick(self.fps)
            self.display.fill(BLACK)
            self.screen.update()
            pygame.display.flip()

        self.screen.destroy()

        pygame.quit()

    def stop(self):
        self._running = False

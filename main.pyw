import pygame

pygame.mixer.init()
pygame.init()

from game import config
from game import assests

from game.engine import Game
from game.screens import Minesweeper


def main():
    game = Game(config.WIDTH, config.HEIGHT, config.CAPTION, config.FPS)
    game.set_icon(assests.icon)

    menu = Minesweeper(config.WIDTH_FIELD, config.HEIGHT_FIELD, config.SIZE_CELL, config.MINES)
    game.start(menu)


if __name__ == '__main__':
    main()

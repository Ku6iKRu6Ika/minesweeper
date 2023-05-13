import pygame
from game import assests

from .abc import Entity


class Cell(Entity):
    def __init__(self, x, y, size, field, is_mine=False):
        self.is_mine = is_mine
        self.opened = False
        self.clicked = False
        self.flag = False
        self.exploded = False

        self.field = field
        self.size = size

        self.x, self.y = x, y
        self.rect = pygame.Rect((self.x * size, self.y * size, size, size))

    def click(self):
        self.clicked = True
        self.field.clicked_cell = self

    def boom(self):
        self.exploded = True

    def change_flag(self):
        self.flag = not self.flag

    def open(self):
        count_mines = self.field.get_count_mines(self.x, self.y)
        self.opened = True

        if count_mines == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if self.field.check_cell(self.x + i, self.y + j):
                        cell = self.field.cells[self.y + j][self.x + i]

                        if not cell.opened:
                            cell.open()

    def draw(self, display):
        if self.opened:
            count_mines = self.field.get_count_mines(self.x, self.y)

            if count_mines == 0:
                image = assests.opened_img
            else:
                image = assests.mines[count_mines]
        elif self.flag:
            image = assests.flag_img
        elif self.clicked:
            image = assests.opened_img
        else:
            image = assests.closed_img

        display.blit(image, self.rect)

    def draw_mine(self, display):
        if self.exploded:
            image = assests.red_mine_img
        else:
            image = assests.mine_img

        display.blit(image, self.rect)

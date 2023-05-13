import random

from .abc import Entity
from .cell import Cell


class Field(Entity):
    cells = []
    clicked_cell = None

    def __init__(self, width, height, size_cell):
        self.width = width
        self.height = height
        self.size_cell = size_cell

        self.reset()

    def reset(self):
        self.cells = []

        for y in range(self.height):
            row = []

            for x in range(self.width):
                row.append(Cell(x, y, self.size_cell, self))

            self.cells.append(row)

    def generate_mines(self, mines, start_x, start_y):
        self.reset()

        cells = []

        for y in range(self.height):
            row = []

            for x in range(self.width):
                if y != start_y or x != start_x:
                    row.append((x, y))

            cells.append(row)

        for i in range(mines):
            x, y = random.choice(random.choice(cells))
            self.cells[y][x].is_mine = True
            cells[y].remove((x, y))

    def remove_clicked(self):
        if self.clicked_cell is not None:
            self.clicked_cell.clicked = False

        self.clicked_cell = None

    def draw(self, display, game_over=False):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[y][x]

                if game_over and cell.is_mine:
                    cell.draw_mine(display)
                else:
                    cell.draw(display)

    def get_cell_from_pos(self, pos):
        x, y = map(lambda k: k // self.size_cell, pos)
        return self.cells[y][x]

    def get_count_mines(self, x, y):
        mines = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.check_cell(x + i, y + j) and self.cells[y + j][x + i].is_mine:
                    mines += 1

        return mines

    def get_count_flags(self, on_mine=False):
        count = 0

        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[y][x]

                if cell.flag:
                    if on_mine and not cell.is_mine:
                        continue

                    count += 1

        return count

    def check_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return True

        return False

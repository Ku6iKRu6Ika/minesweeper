import pygame

from game.engine import Screen
from game.entities import Field

from game import assests


class Minesweeper(Screen):
    def __init__(self, width, height, size_cell, count_mines):
        self.width = width
        self.height = height

        self.field = Field(width, height, size_cell, count_mines)

        self.running = False

    def start(self):
        assests.start_audio.play()

    def update(self):
        cell = None

        for event in pygame.event.get():
            if hasattr(event, 'pos'):
                cell = self.field.get_cell_from_pos(event.pos)

            match event.type:
                case pygame.QUIT:
                    self.game.stop()
                case pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            if not self.running:
                                self.field.generate_mines(cell.x, cell.y)
                                self.running = True

                            if not cell.opened and not cell.flag:
                                cell.click()
                        case 3:
                            if not cell.opened:
                                cell.change_flag()
                                assests.flag_audio.play()
                case pygame.MOUSEBUTTONUP:
                    match event.button:
                        case 1:
                            if cell.clicked:
                                if cell.is_mine:
                                    cell.boom()
                                    assests.lose_audio.play()
                                    self.running = False
                                else:
                                    cell.open()

                            self.field.remove_clicked()

        if self.running:
            flags_on_mine = self.field.get_count_flags(True)
            flags = self.field.get_count_flags()

            if flags_on_mine == self.field.count_mines and flags_on_mine == flags:
                self.running = False
                self.field.reset()

            self.field.draw(self.game.display)
        else:
            self.field.draw(self.game.display, True)

    def destroy(self):
        pass

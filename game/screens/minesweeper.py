import pygame

from game.engine import Screen
from game.entities import Field, Panel

from game import assests


class Minesweeper(Screen):
    def __init__(self, width, height, size_cell, count_mines):
        self.width = width
        self.height = height

        panel_height = 100

        self.rect_panel = pygame.Rect((0, 0, width * size_cell, panel_height))
        self.rect_field = pygame.Rect((0, panel_height, width * size_cell, height * size_cell))

        self.surface_panel = pygame.Surface((width * size_cell, panel_height))
        self.surface_field = pygame.Surface((width * size_cell, height * size_cell))

        self.panel = Panel(panel_height)
        self.field = Field(width, height, size_cell, count_mines)

        self.running = False

    def start(self):
        assests.start_audio.play()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
            elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
                if self.rect_field.collidepoint(*event.pos):
                    cell = self.field.get_cell_from_pos((event.pos[0], event.pos[1] - self.rect_field.y))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if not self.running:
                                self.field.generate_mines(cell.x, cell.y)
                                self.field.cells[cell.y][cell.x].open()

                                self.running = True

                            if not cell.opened and not cell.flag:
                                cell.click()
                        elif event.button == 3 and not cell.opened:
                            cell.change_flag()
                            assests.flag_audio.play()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            if cell.clicked:
                                if cell.is_mine:
                                    cell.boom()
                                    assests.lose_audio.play()
                                    self.running = False
                                else:
                                    cell.open()

                            self.field.remove_clicked()
                elif self.rect_panel.collidepoint(*event.pos):
                    pass

        self._draw()

    def _draw(self):
        if self.running:
            flags_on_mine = self.field.get_count_flags(on_mine=True)
            flags = self.field.get_count_flags()

            if flags_on_mine == self.field.count_mines and flags_on_mine == flags:
                self.running = False
                self.field.reset()

            self.field.draw(self.surface_field)
        else:
            self.field.draw(self.surface_field, True)

        self.game.display.blit(self.surface_panel, self.rect_panel)
        self.game.display.blit(self.surface_field, self.rect_field)

    def destroy(self):
        pass

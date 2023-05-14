import pygame

from game.engine import Screen
from game.entities import Field
from game.entities import Panel
from game.entities import Wrapper

from game import assests


class Minesweeper(Screen):
    def __init__(self, width, height, size_cell, mines, height_panel, margin, margin_width):
        self.width = width
        self.height = height
        self.mines = mines

        self.wrapper = Wrapper(
            width * size_cell,
            height * size_cell,
            height_panel,
            margin,
            margin_width
        )

        self.panel = Panel(width * size_cell, height_panel)
        self.field = Field(width, height, size_cell)

        self.running = False

    def start(self):
        assests.start_audio.play()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
            elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
                if self.wrapper.collide_field(event.pos):
                    self.click_field(event)
                elif self.wrapper.collide_panel(event.pos):
                    self.click_panel(event)

        self.draw()

    def click_field(self, event):
        cell = self.field.get_cell_from_pos(self.wrapper.get_field_pos(event.pos))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if not self.running:
                    self.field.generate_mines(self.mines, cell.x, cell.y)
                    self.field.cells[cell.y][cell.x].open()

                    self.running = True

                if not cell.opened and not cell.flag:
                    cell.click()
            elif event.button == pygame.BUTTON_RIGHT and not cell.opened:
                cell.change_flag()
                assests.flag_audio.play()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                if cell.clicked:
                    if cell.is_mine:
                        cell.boom()
                        assests.lose_audio.play()

                        self.running = False
                    else:
                        cell.open()

                self.field.remove_clicked()

    def click_panel(self, event):
        pass

    def draw(self):
        flags = self.field.get_count_flags()
        self.panel.draw(self.wrapper.sf_panel, self.mines - flags)

        if self.running:
            flags_on_mine = self.field.get_count_flags(on_mine=True)

            if flags_on_mine == self.mines and flags_on_mine == flags:
                self.running = False
                self.field.reset()

            self.field.draw(self.wrapper.sf_field)
        else:
            self.field.draw(self.wrapper.sf_field, True)

        self.wrapper.draw(self.game.display)
        self.game.display.blit(self.wrapper.sf_panel, self.wrapper.rect_panel)
        self.game.display.blit(self.wrapper.sf_field, self.wrapper.rect_field)

    def destroy(self):
        pass

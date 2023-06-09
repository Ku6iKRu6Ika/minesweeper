import pygame
import time

from game.engine import Screen
from game.entities import Field
from game.entities import Panel
from game.entities import Wrapper

from game.const import GameStates
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

        self.start_time = time.time()
        self.current_time = time.time()

        self.running = False
        self.reset_game = True
        self.winner = False

    def start(self):
        assests.start_audio.play()

    def update(self):
        if self.running:
            self.current_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
            elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
                if self.wrapper.collide_field(event.pos):
                    self.click_field(event)
                elif self.wrapper.collide_panel(event.pos):
                    self.click_panel(event)

        self.draw()

    def game_start(self, x, y):
        self.field.generate_mines(self.mines, x, y)
        self.field.cells[y][x].open()

        self.running = True
        self.start_time = time.time()
        self.panel.start_game()

    def game_restart(self):
        self.field.reset()
        self.running = False
        self.reset_game = True
        self.winner = False

        self.start_time = time.time()
        self.current_time = time.time()

    def game_win(self):
        self.running = False
        self.reset_game = False
        self.winner = True

    def game_over(self):
        self.running = False
        self.reset_game = False

    def click_field(self, event):
        cell = self.field.get_cell_from_pos(self.wrapper.get_field_pos(event.pos))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if self.reset_game:
                    if not self.running:
                        self.game_start(cell.x, cell.y)

                    if self.running and not cell.opened and not cell.flag:
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

                        self.game_over()
                    else:
                        cell.open()

                self.field.remove_clicked()

    def click_panel(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.panel.collide_emoji(self.wrapper.get_panel_pos(event.pos)):
                self.panel.click_emoji()
                self.game_restart()

    def draw(self):
        flags = self.field.get_count_flags()

        if self.running:
            flags_mine = self.field.get_count_flags(on_mine=True)

            if flags_mine == self.mines and self.mines == flags and self.field.get_count_closed_cell() == 0:
                self.game_win()
                assests.win_audio.play()
                state = GameStates.WINNER
            else:
                state = GameStates.GOING
        elif self.winner:
            state = GameStates.WINNER
        else:
            state = GameStates.GAME_OVER if not self.reset_game else GameStates.GOING

        self.field.draw(self.wrapper.sf_field, state)
        self.panel.draw(
            self.wrapper.sf_panel,
            self.mines - flags,
            int(self.current_time - self.start_time),
            state
        )

        self.wrapper.draw(self.game.display)

    def destroy(self):
        pass

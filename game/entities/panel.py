import pygame

from game import assests
from game.const import GameStates


LIGHT_GREY = (189, 189, 189)


class Panel:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        size = assests.emoji1.get_width()
        y = (self.height - size) / 2
        x = self.width / 2 - size / 2

        self.rect_emoji = pygame.Rect((x, y, size, size))
        self.reaction = False
        self.clicked = False

    def start_game(self):
        self.reaction = True

    def click_emoji(self):
        self.clicked = True

    def collide_emoji(self, pos):
        return self.rect_emoji.collidepoint(*pos)

    def draw_counters(self, display, flags, time):
        height = assests.digits[0].get_height()
        width = assests.digits[0].get_width()
        y = (self.height - height) / 2

        display.fill(LIGHT_GREY)

        if flags >= 0:
            digits = [
                assests.digits[flags // 10 // 10 % 10],
                assests.digits[flags // 10 % 10],
                assests.digits[flags % 10]
            ]
        else:
            if flags >= -99:
                digits = [
                    assests.digits[10],
                    assests.digits[-flags // 10 % 10],
                    assests.digits[-flags % 10]
                ]
            else:
                digits = [
                    assests.digits[10],
                    assests.digits[9],
                    assests.digits[9]
                ]

        digits_time = [
            assests.digits[time // 10 // 10 % 10],
            assests.digits[time // 10 % 10],
            assests.digits[time % 10]
        ]

        for i in range(3):
            display.blit(digits[i], (y + width * i, y))
            display.blit(digits_time[i], (self.width - y - width * (3 - i), y))

    def draw_emoji(self, display, state):
        size = assests.emoji1.get_width()
        y = (self.height - size) / 2
        x = self.width / 2 - size / 2

        if state == GameStates.WINNER:
            emoji = assests.emoji[3]
        elif state == GameStates.GAME_OVER:
            emoji = assests.emoji[1]
        elif self.reaction:
            emoji = assests.emoji[2]
            self.reaction = False
        elif self.clicked:
            emoji = assests.emoji[4]
            self.clicked = False
        else:
            emoji = assests.emoji[0]

        display.blit(emoji, (x, y))

    def draw(self, display, flags, time, state):
        self.draw_counters(display, flags, time)
        self.draw_emoji(display, state)



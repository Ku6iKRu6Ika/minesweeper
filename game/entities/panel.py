import pygame
from game import assests


LIGHT_GREY = (189, 189, 189)


class Panel:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, display, flags):
        margin_cf = 20
        height_d = assests.digits[0].get_height()
        width_d = assests.digits[0].get_width()
        y = (self.height - height_d) / 2

        display.fill(LIGHT_GREY)

        if flags >= 0:
            digits = [
                assests.digits[flags // 10 // 10 % 10],
                assests.digits[flags // 10 % 10],
                assests.digits[flags % 10]
            ]
        else:
            display.blit(assests.digits[-1], (margin_cf, y))
            if flags >= -99:
                digits = [
                    assests.digits[-1],
                    assests.digits[-flags // 10 % 10],
                    assests.digits[-flags % 10]
                ]
            else:
                digits = [
                    assests.digits[-1],
                    assests.digits[9],
                    assests.digits[9]
                ]

        for i in range(3):
            display.blit(digits[i], (margin_cf + width_d * i, y))

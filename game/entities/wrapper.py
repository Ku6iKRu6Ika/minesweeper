import pygame


GREY = (123, 123, 123)
LIGHT_GREY = (189, 189, 189)
WHITE = (255, 255, 255)


class Wrapper:
    def __init__(self, width_field, height_field, height_panel, margin, margin_width):
        self.width_window = width_field + 2 * margin + 2 * margin_width
        self.height_window = height_field + height_panel + 3 * margin + 4 * margin_width

        self.margin = margin
        self.margin_width = margin_width

        self.sf_panel = pygame.Surface((width_field, height_panel))
        self.rect_panel = pygame.Rect(
            (margin + margin_width, margin + margin_width, width_field, height_panel)
        )

        self.sf_field = pygame.Surface((width_field, height_field))
        self.rect_field = pygame.Rect(
            (margin + margin_width, 2 * margin + 3 * margin_width + height_panel, width_field, height_field)
        )

    def collide_field(self, pos):
        return self.rect_field.collidepoint(*pos)

    def collide_panel(self, pos):
        return self.rect_panel.collidepoint(*pos)

    def get_field_pos(self, pos):
        return (
            pos[0] - self.rect_field.x,
            pos[1] - self.rect_field.y
        )

    def get_panel_pos(self, pos):
        return (
            pos[0] - self.rect_panel.x,
            pos[1] - self.rect_panel.y
        )

    def draw_border(self, display, rect):
        margin_width = self.margin_width

        pygame.draw.line(
            display,
            GREY,
            (rect.x - margin_width, rect.y - margin_width / 2),
            (rect.x + rect.width + margin_width - 1, rect.y - margin_width / 2),
            margin_width
        )

        pygame.draw.line(
            display,
            GREY,
            (rect.x - margin_width / 2, rect.y),
            (rect.x - margin_width / 2, rect.y + margin_width + rect.height - 1),
            margin_width
        )

        pygame.draw.line(
            display,
            WHITE,
            (rect.x, rect.y + rect.height + margin_width / 2),
            (rect.x + rect.width, rect.y + rect.height + margin_width / 2),
            margin_width
        )

        pygame.draw.line(
            display,
            WHITE,
            (rect.x + rect.width + margin_width / 2, rect.y),
            (rect.x + rect.width + margin_width / 2, rect.y + rect.height + margin_width - 1),
            margin_width
        )

        pygame.draw.polygon(
            display,
            WHITE,
            [
                [rect.x + rect.width + margin_width - 1, rect.y - margin_width],
                [rect.x + rect.width + margin_width - 1, rect.y],
                [rect.x + rect.width, rect.y]
            ]
        )

        pygame.draw.polygon(
            display,
            WHITE,
            [
                [rect.x, rect.y + rect.height],
                [rect.x, rect.y + margin_width + rect.height - 1],
                [rect.x - margin_width, rect.y + margin_width + rect.height - 1]
            ]
        )

    def draw(self, display):
        display.fill(LIGHT_GREY)
        self.draw_border(display, self.rect_panel)
        self.draw_border(display, self.rect_field)

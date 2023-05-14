import os
import pygame

from game import config


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
audio_folder = os.path.join(game_folder, 'audio')


def get_img(filename):
    return pygame.image.load(os.path.join(img_folder, filename))


def get_audio(filename):
    return pygame.mixer.Sound(os.path.join(audio_folder, filename))


def get_music(filename):
    return pygame.mixer.music.load(os.path.join(audio_folder, filename))


def scale_cell(image, size):
    return pygame.transform.scale(image, (size, size))


def scale_factor(image, factor):
    size = image.get_size()

    return pygame.transform.scale(image, (size[0] * factor, size[1] * factor))


icon = get_img('icon.ico')

closed_img = scale_cell(get_img('closed.png'), config.SIZE_CELL)
opened_img = scale_cell(get_img('opened.png'), config.SIZE_CELL)
flag_img = scale_cell(get_img('flag.png'), config.SIZE_CELL)
mine_img = scale_cell(get_img('mine.png'), config.SIZE_CELL)
red_mine_img = scale_cell(get_img('red_mine.png'), config.SIZE_CELL)

lose_audio = get_audio('lose.mp3')
flag_audio = get_audio('flag.mp3')
start_audio = get_audio('start.mp3')

mines = {
    1: scale_cell(get_img('t1.png'), config.SIZE_CELL),
    2: scale_cell(get_img('t2.png'), config.SIZE_CELL),
    3: scale_cell(get_img('t3.png'), config.SIZE_CELL),
    4: scale_cell(get_img('t4.png'), config.SIZE_CELL),
    5: scale_cell(get_img('t5.png'), config.SIZE_CELL),
    6: scale_cell(get_img('t6.png'), config.SIZE_CELL),
    7: scale_cell(get_img('t7.png'), config.SIZE_CELL),
    8: scale_cell(get_img('t8.png'), config.SIZE_CELL)
}

digits = {
    -1: scale_factor(get_img('d-1.png'), 2),
    0: scale_factor(get_img('d0.png'), 2),
    1: scale_factor(get_img('d1.png'), 2),
    2: scale_factor(get_img('d2.png'), 2),
    3: scale_factor(get_img('d3.png'), 2),
    4: scale_factor(get_img('d4.png'), 2),
    5: scale_factor(get_img('d5.png'), 2),
    6: scale_factor(get_img('d6.png'), 2),
    7: scale_factor(get_img('d7.png'), 2),
    8: scale_factor(get_img('d8.png'), 2),
    9: scale_factor(get_img('d9.png'), 2),
}

import pygame as py
from player import Player
import sys
from colors import green1, green2
import numpy as np
from Enviroment.background import BackParallax
from Assets.test_background import test_back
from Functions.read_map_data import read_map_data
from Assets.UI.UI_Assets import health_bar, cursor
from Assets.Animations.Test_Animations.animation_test import slime_animations
from Enemies.gen_enemy import GenEnemy


def main():
    screen_pos = np.array([0, 0])
    py.init()
    initiate()
    rune_select_index_x = 0
    rune_select_key_down = False
    while running:
        rune_select_index_x, rune_select_key_down = update(screen_pos, rune_select_index_x, rune_select_key_down)
        print(rune_select_key_down)


def initiate():
    global player, tile_obs, clock, running, window, x_width, y_width, player_init_pos, scroll_vec, background_obs, mouse_pos, enemies
    mouse_pos = py.mouse.get_pos()
    y_width = 800
    x_width = int((16/9) * y_width)
    tile_obs = []
    background_obs = []
    enemies = []
    clock = py.time.Clock()
    running = True
    enviro_shift = load_environment()
    player_init_pos = np.array([x_width / 2 - 25, (2 / 3) * y_width - 25])
    player = Player(player_init_pos[0], player_init_pos[1], 50, 50)
    py.mouse.set_visible(False)
    scroll_vec = np.array([1, 0])

    for i in range(-16000, 16000, 800):
        background_obs.append(
            BackParallax(
                x=i, y=0, height=800, width=800, depth=5, color=green1, sprite=test_back))
        background_obs.append(
            BackParallax(
                x=i, y=-800, height=800, width=800, depth=5, color=green1, sprite=test_back))

    window = py.display.set_mode((x_width, y_width))
    enemies.append(GenEnemy(x=200, y=200, height=50, width=50, animation_dict=slime_animations, health=10))
    init_adjust(enviro_shift)


def update(screen_pos, rune_select_index_x, rune_select_key_down):
    clock.tick(60)
    mouse_pos = py.mouse.get_pos()

    if abs(player.x - player_init_pos[0]) >= 50:
        scroll_vec[0] = (player.x - scroll_vec[0] - player_init_pos[0])/25
    else:
        scroll_vec[0] = 0
    if player_init_pos[1] - player.y >= 200:
        scroll_vec[1] = (player.y - scroll_vec[1] - player_init_pos[1])/25
    elif player_init_pos[1] - player.y <= -75:
        scroll_vec[1] = (player.y - scroll_vec[1] - player_init_pos[1])/10
    else:
        scroll_vec[1] = 0

    screen_pos += scroll_vec

    window.fill(green2)
    for bck in background_obs:
        bck.x -= (1/bck.depth)*scroll_vec[0]
        bck.y -= (1/bck.depth)*scroll_vec[1]
        if -1*x_width <= bck.x <= x_width:
            bck.update(window)
    rune_select_index_x, rune_select_key_down = take_input(rune_select_index_x, rune_select_key_down)
    player.update(window=window, tiles=tile_obs, scroll_vec=scroll_vec, mouse_pos=mouse_pos)
    for ob in tile_obs:
        ob.x -= scroll_vec[0]
        ob.y -= scroll_vec[1]
        if -1*x_width <= ob.x <= x_width:
            ob.update(window)
    for enem in enemies:
        enem.collide_rect.x -= scroll_vec[0]
        enem.collide_rect.y -= scroll_vec[1]
        enem.update(window=window, tiles=tile_obs)
    display_ui(rune_select_index_x)
    py.display.update()

    return rune_select_index_x, rune_select_key_down


def take_input(rune_select_index_x, rune_select_key_down):
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()

    clicks = py.mouse.get_pressed(3)
    keys = py.key.get_pressed()
    if keys[py.K_e] and not rune_select_key_down:
        rune_select_key_down = True
        if rune_select_index_x < 1:
            rune_select_index_x += 1
        elif rune_select_index_x >= 1:
            rune_select_index_x -= rune_select_index_x
    if not keys[py.K_e]:
        rune_select_key_down = False
    player.assign_accel(keys)

    return rune_select_index_x, rune_select_key_down


def load_environment():
    player_init_pos = [0, 0]
    test_envo = read_map_data('level_editor/maps/test.txt', 8)
    for key in test_envo.keys():
        for tile in test_envo[key].tiles:
            tile_obs.append(tile)
        if test_envo[key].player_init[0] != 0 and test_envo[key].player_init[1] != 0:
            player_init_pos = test_envo[key].player_init

    return player_init_pos


def init_adjust(enviro_shift):
    scroll_vec[0] = (player.x - enviro_shift[0])
    scroll_vec[1] = (player.y - enviro_shift[1])

    for ob in tile_obs:
        ob.x += scroll_vec[0]
        ob.y += scroll_vec[1]


def display_ui(rune_select_index_x):
    health_bar_i = health_bar[rune_select_index_x]
    window.blit(health_bar_i.convert_alpha(), (0, 20))
    window.blit(cursor.convert_alpha(), (py.mouse.get_pos()[0]-25, py.mouse.get_pos()[1]-25))


if __name__ == '__main__':
    main()

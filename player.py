import pygame as py
from colors import gold
import numpy as np
import Functions.movement_collision as move
from Functions.animation import animation
from Assets.Animations.Test_Animations.animation_test import test_animations


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collide_rect = py.rect.Rect(self.x, self.y, self.width, self.height)
        self.velocity = np.array([0, 0])
        self.accel = np.array([0, 0])
        self.accel_speed = 1
        self.decel_speed = 2
        self.fall_speed = 1
        self.left_collision = False
        self.right_collision = False
        self.top_collision = False
        self.bottom_collision = False
        self.has_jumped = False
        self.state = 'idle'
        self.previous_state = 'idle'
        self.animation_clock = 0
        self.frame_durations = 0
        self.invert = False

    def update(self, window, tiles, scroll_vec, mouse_pos):
        self.pos_change(tiles)
        self.display(window, scroll_vec, mouse_pos)

    def display(self, window, scroll_vec, mouse_pos):
        self.collide_rect.x -= scroll_vec[0]
        self.collide_rect.y -= scroll_vec[1]
        # py.draw.rect(surface=window, color=gold, rect=self.collide_rect)
        self.x, self.y = self.collide_rect.x, self.collide_rect.y
        if mouse_pos[0] <= self.x:
            self.invert = True
        elif mouse_pos[0] > self.x:
            self.invert = False
        self.previous_state, self.frame_durations, self.animation_clock = animation(
            image_list=test_animations[self.state], x=self.x - 50, y=self.y - 50, invert=self.invert, hit=False,
            mac_clock=self.animation_clock, mic_clock=self.frame_durations, window=window,
            prev_animation=self.previous_state, cur_animation=self.state)

    def pos_change(self, tiles):
        max_x = 4
        max_fall = 12

        if abs(self.velocity[0]) <= max_x:
            self.velocity[0] += self.accel[0]
            self.velocity[0] = int(self.velocity[0])
        else:
            self.velocity[0] = (np.sign(self.velocity[0]) * max_x)

        if self.velocity[1] <= max_fall:
            self.velocity[1] += self.accel[1]
        else:
            self.velocity[1] = max_fall

        self.collide_rect = move.move(self, tiles, self.velocity)

    def assign_accel(self, keys):
        if keys[py.K_d]:
            self.accel[0] = self.accel_speed
            self.state = 'run'
        elif keys[py.K_a]:
            self.accel[0] = -1 * self.accel_speed
            self.state = 'run'
        else:
            self.state = 'idle'
            if np.sign(self.velocity[0]) == 1:
                if np.sign(self.velocity[0] + self.accel[0]) == 1:
                    self.accel[0] = -1 * self.decel_speed
                else:
                    self.accel[0] = 0
                    self.velocity[0] = 0
            elif np.sign(self.velocity[0]) == -1:
                if np.sign(self.velocity[0] + self.accel[0]) == -1:
                    self.accel[0] = self.decel_speed
                else:
                    self.accel[0] = 0
                    self.velocity[0] = 0

        if self.velocity[1] < 0:
            self.state = 'jump'
        if self.velocity[1] > 0 and self.bottom_collision is False:
            self.state = 'fall'

        self.accel[1] = self.fall_speed
        if keys[py.K_SPACE] and self.has_jumped is False:
            self.velocity[1] = -17
            self.has_jumped = True

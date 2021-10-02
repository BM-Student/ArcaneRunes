import numpy as np
import pygame as py
from Functions.animation import animation
import Functions.movement_collision as move


class GenEnemy:
    def __init__(self, x, y, height, width, health, animation_dict):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health
        self.animation_dict = animation_dict
        self.previous_state = 'idle'
        self.state = 'idle'
        self.animation_clock = 0
        self.frame_durations = 0
        self.invert = False
        self.velocity = [0, 0]
        self.collide_rect = py.rect.Rect(self.x, self.y, self.width, self.height)
        self.accel = [0, 12]

    def update(self, window, tiles):
        self.accel = [0, 1]
        self.velocity[0] += self.accel[0]
        self.velocity[1] += self.accel[1]
        self.collide_rect = move.move(self, tiles, self.velocity)
        self.x, self.y = self.collide_rect.x, self.collide_rect.y
        self.display(window)

    def display(self, window):
        self.previous_state, self.frame_durations, self.animation_clock = animation(
            image_list=self.animation_dict[self.state], x=self.x - 50, y=self.y - 50, invert=self.invert, hit=False,
            mac_clock=self.animation_clock, mic_clock=self.frame_durations, window=window,
            prev_animation=self.previous_state, cur_animation=self.state)

    def check_hit(self):
        pass

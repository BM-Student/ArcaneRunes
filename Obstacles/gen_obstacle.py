import pygame as py
from colors import grey


class Obstacle:
    def __init__(self, x, y, width, height, sprite):
        self.x = x
        self.y = y
        self. width = width
        self.height = height
        self.color = grey
        self.sprite = sprite
        self.collide_rect = py.rect.Rect(self.x, self.y, self.width, self.height)

    def update(self, window):
        self.display(window)

    def display(self, window):
        self.collide_rect = py.rect.Rect(self.x, self.y, self.width, self.height)
        window.blit(self.sprite.convert_alpha(), (self.x, self.y))
        # py.draw.rect(surface=window, color=self.color, rect=self.collide_rect)

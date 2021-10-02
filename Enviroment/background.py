import numpy as np


class BackParallax:
    def __init__(self, x, y, height, width, depth, color, sprite):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.depth = depth
        self.color = color
        #self.collide_rect = py.rect.Rect(self.x, self.y, self.width, self.height)
        self.sprite = sprite
        self.true_pos = np.array([x, y])

    def update(self, window):
        self.display(window)

    def display(self, window):
        #self.collide_rect = py.rect.Rect(self.x, self.y, self.width, self.height)
        # py.draw.rect(surface=window, color=self.color, rect=self.collide_rect)
        window.blit(self.sprite.convert(), (self.x, self.y))

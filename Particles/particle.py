import pygame as py
import random


class Particle:
    def __init__(self, x, y, vel, size, color, particles, rate_of_decay=1):
        self.x = x
        self.y = y
        self.color = color
        self.rate_of_decay = rate_of_decay
        self.vel = [random.randint(-1, 1), random.randint(-1, 1)]
        self.size = size
        particles.append(self)

    def display(self, particles, window):
        self.update(particles)

        if self.size <= 0:
            particles.remove(self)
        rect = py.Rect(self.x, self.y, self.size, self.size)
        py.draw.rect(window, self.color, rect)

    def update(self, particles):
        self.x += self.vel[0]
        self.y += self.vel[1]

        self.size -= self.rate_of_decay

        if self.size <= 0:
            particles.remove(self)

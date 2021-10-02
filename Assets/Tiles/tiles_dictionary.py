import pygame as py
import os

tile_dict = {}

for i in range(3):
    for j in range(3):
        file = f'/Users/brendon/PycharmProjects/CoxVsCrendor/Assets/Tiles/Brick_Tile{i}{j}.png'
        tile_dict[f'{i}{j}'] = py.transform.scale(py.image.load(file), (50, 50))

pass

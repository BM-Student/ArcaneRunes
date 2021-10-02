import pygame as py

health_bar = []
for i in range(2):
    health_bar.append(py.transform.scale(py.image.load(f'Assets/UI/Player_Health{i}.png'), (300, 150)))
cursor = py.transform.scale(py.image.load('Assets/UI/Cursor.png'), (50, 50))

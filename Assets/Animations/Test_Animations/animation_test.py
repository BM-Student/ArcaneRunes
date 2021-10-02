import pygame as py

idle_animation = []
run_animation = []
jump_animation = []
fall_animation = []
for i in range(5):
    idle_animation.append((8, py.transform.scale(
        py.image.load(f'Assets/Animations/Test_Animations/MageIdle_{i}.png'), (150, 150))))


for i in range(8):
    run_animation.append((5, py.transform.scale(
        py.image.load(f'Assets/Animations/Test_Animations/MageRun{i}.png'), (150, 150))))

jump_animation.append(
    (1, py.transform.scale(py.image.load(f'Assets/Animations/Test_Animations/MageJump0.png'), (150, 150))))

fall_animation.append((
    1, py.transform.scale(py.image.load(f'Assets/Animations/Test_Animations/MageJump1.png'), (150, 150))))


test_animations = {'idle': idle_animation,
                   'run': run_animation,
                   'jump': jump_animation,
                   'fall': fall_animation}

test_enemy = []
for i in range(6):
    test_enemy.append((7, py.transform.scale(py.image.load(f'Assets/Animations/Test_Animations/Slime{i}.png'), (150, 150))))

slime_animations = {'idle': test_enemy}

import pygame as py
import sys
import level_editor.classes as cl
import level_editor.function_library as fl
import time
import level_editor.values as vals


def main():
    py.init()
    initiate()
    index = 0
    key_down = False
    while running:
        index, key_down = update(index, key_down)


def initiate():
    global window, clock, running, font_24, num_chunks_x, header, increase_x, decrease_x, tiles, x_width, y_width
    y_width = 600
    running = True
    x_width = int((16 / 9) * y_width - y_width*(2/15))
    window = py.display.set_mode((x_width, int(y_width + (y_width/10 + 65))))
    clock = py.time.Clock()
    font_24 = py.font.SysFont(None, 50)
    header = py.rect.Rect(0, 0, x_width, (y_width/10 + 25))
    increase_x = cl.Box(x=x_width/20 + 50, y=y_width/20-5, height=(y_width/10 - 45), width=(y_width/10 - 25),
                        center_color='#FF9F2D', border_color='#262833', border_thickness=5)
    decrease_x = cl.Box(x=x_width / 20 + 50, y=y_width / 20 + (y_width/10 - 45) + 10,
                        height=(y_width / 10 - 45), width=(y_width / 10 - 25),
                        center_color='#FF9F2D', border_color='#262833', border_thickness=5)
    num_chunks_x = cl.Text(x=x_width/20, y=y_width/20, size=50, color='#FF9F2D', font=font_24, text='5')
    tiles = []
    gen_grid()


def update(index, key_down):
    clock.tick(60)
    window.fill(color='#262833')
    py.draw.rect(window, color='#2D2D44', rect=header)
    index = take_input(index, key_down)
    num_chunks_x.display(window=window)

    py.display.update()
    return index


def take_input(index, key_down):
    values = vals.values
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()

    x_chunks = int(num_chunks_x.text)

    keys = py.mouse.get_pressed(5)
    inputs = py.key.get_pressed()
    if inputs[py.K_k] and key_down is False:
        inp = 'down'
        key_down = True
    elif inputs[py.K_l] and key_down is False:
        inp = 'up'
        key_down = True
    elif inputs[py.K_l] or inputs[py.K_k]:
        inp = 'no change'
    else:
        inp = 'no change'
        key_down = False
    if inputs[py.K_p]:
        fl.save_data(tiles=tiles)
        time.sleep(1)

    index, values = fl.change_tile(index=index, inp=inp, value_list=values)
    brush = cl.Text(x=x_width / 2, y=y_width / 20, size=50, color='#FF9F2D', font=font_24, text=values[0])
    brush.display(window)

    mouse_pos = py.mouse.get_pos()
    mouse_rect = py.rect.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
    py.draw.rect(window, color='#d4ce46', rect=mouse_rect)
    x_chunks += increase_x.update(window, delta=1, mouse=mouse_rect, press=keys)
    x_chunks += decrease_x.update(window, delta=-1, mouse=mouse_rect, press=keys)
    num_chunks_x.text = str(x_chunks)
    for tile_list in tiles:
        for tile in tile_list:
            tile.update(window=window, mouse=mouse_rect, key=keys, set_value=values[0], new_color=values[1],
                        movement=inputs, y_width=y_width)

    return index, key_down


def gen_grid():
    chunks_x = int(num_chunks_x.text)*8
    size = x_width*(6/8)/chunks_x - 2
    for i in range(chunks_x):
        blank_list = []
        for j in range(chunks_x):
            #blank_list.append(cl.TileBox(i*17 + int((1/7)*x_width), j*17 + (y_width/10 + 35), size))
            blank_list.append(cl.TileBox(j, i, size))
        tiles.append(blank_list)


if __name__ == '__main__':
    main()

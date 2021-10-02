import os
import tqdm


def save_data(tiles):
    tiles_copy = tiles.copy()
    save_test = open(f'{os.getcwd()}/maps/save_test.txt', 'w')
    tile_count = 0
    #map_data = []
    #for row in range(chunks*8):
        #filled_row = [0 for i in range(chunks*8)]
        #map_data.append(filled_row)
    for y in tqdm.tqdm(range(len(tiles_copy)), total=len(tiles_copy)):
        for x in range(y):
            tile_count += 1
            new_tile = tiles_copy[y][x]
            print(new_tile.value)
            if new_tile.value == 'tile':
                new_tile.value = tile_adjust(tiles_copy, new_tile)
            elif new_tile.value == 'player':
                new_tile.value = 'pl'
            else:
                new_tile.value = '0'

            #map_data[int((tiles[y][x].y - 95)/17)][int((tiles[y][x].x - 140)/17)] = tiles[y][x].value
            tiles_copy[y][x] = new_tile.value
    print(f'tiles read: {tile_count}')

    map_text = ''
    #for r in map_data:
    for r in tiles_copy:
        print(r)
        map_text += f'{str(r)};'.replace(' ', '').replace('[', '').replace(']', '')

    save_test.write(map_text.replace("'", '').replace('\n', '').replace(';', ';\n'))

    save_test.close()


def load_data():
    pass


def tile_adjust(tiles, tile):
    # get number of touching tiles
    index = (tile.index_x, tile.index_y)
    print(f'looking here: {index}')
    number_touching = 0
    spots_to_check = {'spot1': (index[0]-1, index[1]),
                      'spot2': (index[0]+1, index[1]),
                      'spot3': (index[0], index[1]-1),
                      'spot4': (index[0], index[1]+1)}
    for key in spots_to_check.keys():
        new_index = spots_to_check[key]
        try:
            if tiles[new_index[0]][new_index[1]].value != '0' and tiles[new_index[0]][new_index[1]].value != 'pl':
                number_touching += 1
        except IndexError:
            number_touching += 1

    # checks if center piece
    if number_touching == 4:
        return '11'
    # checks for flats
    elif number_touching == 3:
        if tiles[index[0] - 1][index[1]].value == '0' or tiles[index[0] - 1][index[1]].value == 'pl':
            return '10'
        elif tiles[index[0] + 1][index[1]].value == '0' or tiles[index[0] + 1][index[1]].value == 'pl':
            return '12'
        elif tiles[index[0]][index[1] - 1].value == '0' or tiles[index[0]][index[1] - 1].value == 'pl':
            return '01'
        elif tiles[index[0]][index[1] + 1].value == '0' or tiles[index[0]][index[1] + 1].value == 'pl':
            return '21'
    # checks for corners
    elif number_touching == 2:
        if (tiles[index[0] - 1][index[1]].value == '0' or tiles[index[0] - 1][index[1]].value == 'pl') and\
           (tiles[index[0]][index[1] - 1].value == '0' or tiles[index[0]][index[1] - 1].value == 'pl'):
            return '00'
        elif (tiles[index[0] - 1][index[1]].value == '0' or tiles[index[0] - 1][index[1]].value == 'pl') and\
             (tiles[index[0]][index[1] + 1].value == '0' or tiles[index[0]][index[1] + 1].value == 'pl'):
            return '20'
        elif (tiles[index[0] + 1][index[1]].value == '0' or tiles[index[0] + 1][index[1]].value == 'pl') and\
             (tiles[index[0]][index[1] - 1].value == '0' or tiles[index[0]][index[1] - 1].value == 'pl'):
            return '02'
        elif (tiles[index[0] + 1][index[1]].value == '0' or tiles[index[0] + 1][index[1]].value == '0') and\
             (tiles[index[0]][index[1] + 1].value == '0' or tiles[index[0]][index[1] + 1].value == 'pl'):
            return '22'
    else:
        return '11'


def change_tile(inp, index, value_list):
    if inp == 'up':
        index += 1
        if index < len(value_list):
            return index, value_list[index]
        else:
            index = 0
            return index, value_list[index]

    elif inp == 'down':
        index -= 1
        if index < 0:
            index = len(value_list) - 1
            return index, value_list[index]
        else:
            return index, value_list[index]

    else:
        return index, value_list[index]

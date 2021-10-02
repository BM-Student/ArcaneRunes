from Obstacles.gen_obstacle import Obstacle
from Assets.Tiles.tiles_dictionary import tile_dict


class Chunk:
    def __init__(self, x, y, size, data):
        self.x = x
        self.y = y
        self.size = size
        self.data = data
        self.x_bound = x + size
        self.y_bound = y + size
        self.tiles = []
        self.player_init = [0, 0]
        self.translate_data(50)

    def translate_data(self, tile_size):
        for row_num in range(self.size):
            y = self.y + tile_size*row_num
            for col_num in range(self.size):
                x = self.x + tile_size*col_num
                try:
                    self.tiles.append(Obstacle(x=x, y=y, width=tile_size, height=tile_size,
                                               sprite=tile_dict[self.data[row_num, col_num]]))
                except KeyError:
                    if self.data[row_num, col_num] == 'pl':
                        self.player_init = [x, y]
                    pass

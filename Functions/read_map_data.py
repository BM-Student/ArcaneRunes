import numpy as np
from Enviroment.chunk import Chunk


def read_map_data(map_file, chunk_size):
    # row, column
    map = open(map_file, 'r')
    map_data = map.read()
    map.close()
    rows = map_data.replace('\n', '').split(';')
    cleaned_rows = [row.split(',') for row in rows if len(row) > 0]

    map_matrix = np.matrix(cleaned_rows, dtype=str)
    matrix_dim = map_matrix.shape

    chunk_dict = {}
    for r in range(int(matrix_dim[0]/chunk_size)):
        for c in range(int(matrix_dim[1]/chunk_size)):
            chunk_dict[f'{r*chunk_size*50},{c*chunk_size*50}'] =\
                Chunk(
                      data=map_matrix[chunk_size*r:chunk_size*(r+1), chunk_size*c:chunk_size*(c+1)],
                      y=r*chunk_size*50,
                      x=c*chunk_size*50,
                      size=chunk_size
                )

    return chunk_dict


if __name__ == '__main__':
    read_map_data('save_test.csv', 8)

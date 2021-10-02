import numpy as np


def scroll(init_pos, player_pos, x_width):
    direct_vec = player_pos - init_pos
    norm_check = np.linalg.norm(direct_vec)
    if norm_check >= (1/5)*x_width:
        scroll_vec = -1*direct_vec
    else:
        scroll_vec = np.array([0, 0])

    return scroll_vec

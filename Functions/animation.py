import pygame as py


def animation(image_list, x, y, invert, hit, mac_clock, mic_clock, window, prev_animation, cur_animation, scale=1):
    if cur_animation != prev_animation:
        mic_clock = 0
        mac_clock = 0

    frame = image_list[mac_clock]
    frame_duration = frame[0]
    if invert is False:
        window.blit(frame[1].convert_alpha(), (x, y))
    elif invert is True:
        window.blit(py.transform.flip(frame[1].convert_alpha(), True, False), (x, y))

    mic_clock += 1
    if mic_clock >= frame_duration:
        mic_clock = 0
        mac_clock += 1
    if mac_clock >= len(image_list):
        mac_clock = 0

    return cur_animation, mic_clock, mac_clock


def hit_alteration():
    pass

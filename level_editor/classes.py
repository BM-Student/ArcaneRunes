import pygame as py


class Text:
    def __init__(self, x, y, size, color, font, text):
        self.x = x
        self.y = y
        self.font = font
        self.size = size
        self.color = color
        self.text = text

    def display(self, window):
        disp_text = self.font.render(self.text, True, self.color)
        window.blit(disp_text, (self.x, self.y))


class Box:
    def __init__(self, x, y, height, width, center_color, border_thickness, border_color):
        self.center_color = center_color
        self.center_reserve = center_color
        self.center = py.rect.Rect(x, y, width, height)
        self.border_color = border_color
        self.border = py.rect.Rect(x-border_thickness, y-border_thickness,
                                   width + 2*border_thickness, height + 2*border_thickness)
        self.being_clicked = False

    def update(self, window, delta, mouse, press):
        if self.center.colliderect(mouse) and press[0] and not self.being_clicked:
            self.being_clicked = True
            self.center_color = self.border_color
            self.display(window)
            return delta
        elif press[0] and self.center.colliderect(mouse):
            self.being_clicked = True
            self.center_color = self.center_reserve
            return 0
        else:
            self.being_clicked = False
            self.center_color = self.center_reserve
            self.display(window)
            return 0

    def display(self, window):
        py.draw.rect(window, color=self.border_color, rect=self.border)
        py.draw.rect(window, color=self.center_color, rect=self.center)


class TileBox:
    def __init__(self, index_x, index_y, size):
        self.index_x = index_x
        self.index_y = index_y
        self.x = index_x * size + 1
        self.y = index_y * size + 1
        self.size = size
        self.rect = py.rect.Rect(self.x, self.y, size, size)
        self.border = py.rect.Rect(self.x-1, self.y-1, size+2, size+2)
        self.color = '#262833'
        self.color_reserve = self.color
        self.border_color = '#F1F1E8'
        self.being_clicked = False
        self.value = '0'

    def update(self, window, mouse, key, set_value, new_color, movement, y_width):
        if self.rect.colliderect(mouse) and key[0] and self.being_clicked is False:
            self.being_clicked = True
            self.value = set_value
            self.color = new_color
            print(self.value)
        elif not key[0] and self.being_clicked:
            self.being_clicked = False

        self.move(movement)

        if 100 < self.rect.x < int((16 / 9) * y_width - y_width*(2/15)) - (100+self.size) and \
                y_width > self.rect.y > (y_width/10 + 35):
            self.display(window)

    def display(self, window):
        py.draw.rect(window, color=self.border_color, rect=self.border)
        py.draw.rect(window, color=self.color, rect=self.rect)

    def move(self, directions):
        if directions[py.K_w]:
            self.rect.y -= 1
            self.border.y -= 1
        elif directions[py.K_s]:
            self.rect.y += 1
            self.border.y += 1

        if directions[py.K_a]:
            self.rect.x -= 1
            self.border.x -= 1
        elif directions[py.K_d]:
            self.rect.x += 1
            self.border.x += 1

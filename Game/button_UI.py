import pygame

class Button():
    def __init__(self, input_screen, input_image, x_pos, y_pos, image_width, image_height, input_image_act, act_x_pos, act_y_pos, action = None):
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        if x_pos + image_width > mouse_pos[0] > x_pos and y_pos + image_height > mouse_pos[1] > y_pos:
            input_screen.blit(input_image_act,(act_x_pos, act_y_pos))
            if mouse_press[0] and action is not None:
                action()
        else:
            input_screen.blit(input_image, (x_pos, y_pos))
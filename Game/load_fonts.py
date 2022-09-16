import pygame

def pixel_font(input_screen, input_text, font_color, x_pos, y_pos, text_size):
    font = pygame.font.Font("fonts/Fixel.ttf", text_size)
    set_headline = font.render(input_text, True, font_color)
    input_screen.blit(set_headline, (x_pos, y_pos))

def handwriting_font(input_screen, input_text, font_color, x_pos, y_pos, text_size):
    font = pygame.font.Font("fonts/Hhandwriting.ttf", text_size)
    set_headline = font.render(input_text, True, font_color)
    input_screen.blit(set_headline, (x_pos, y_pos))


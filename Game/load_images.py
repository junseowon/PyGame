import pygame


def background(input_screen, x_pos, y_pos):
    background_robby = pygame.image.load("images/backgrounds/Robby.png")
    input_screen.blit(background_robby,(x_pos, y_pos))

def use_dung_geun_font(input_screen, input_text, font_color, x_pos, y_pos, text_size):
    font = pygame.font.Font("fonts/DungGeunMo.ttf", text_size)
    set_headline = font.render(input_text, True, font_color)
    input_screen.blit(set_headline, (x_pos, y_pos))
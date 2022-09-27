import pygame
from load_fonts import *

def Park_Jin_cheol_dialog():
    pass

def hamzzizzi_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)

    if input_line == 1:
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "해바라기씨를 잃어버렸어요...", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "동생 생일선물이었는데...ㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "혹시 찾아주시는 걸 도와주실 수 있나요?", font_color, 200, 550, 30)
    elif input_line == 5:
        pixel_font(input_screen, "햄찌찌씨를 도와 잃어버린 선물을 찾아주세요.", font_color, 200, 550, 30)
            
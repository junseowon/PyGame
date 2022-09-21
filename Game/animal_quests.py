import pygame
from load_fonts import *

def hamzzizzi_quest(input_screen, font_color, input_line):
    dialog = pygame.image.load("images/characters/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        handwriting_font(input_screen, "해바라기씨를 잃어버렸어요..", font_color, 200, 550, 50)
    elif input_line == 2:
        handwriting_font(input_screen, "동생 생일선물이였는데..!", font_color, 200, 550, 50)
    elif input_line == 3:
        handwriting_font(input_screen, "우와.. 찾아주신다구요?", font_color, 200, 550, 50)
    elif input_line == 4:
        handwriting_font(input_screen, "감사합니다!!", font_color, 200, 550, 50)
    elif input_line == 5:
        handwriting_font(input_screen, "햄찌찌씨의 잃어버린 동생 선물을 찾아주세요.", font_color, 200, 550, 45)
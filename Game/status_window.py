import pygame
from load_fonts import *

def hamzzizzi_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "해바라기씨를 잃어버렸어요...", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "동생 생일선물이었는데...ㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "혹시 찾아주시는 걸 도와주실 수 있나요?", font_color, 200, 550, 30)
    elif input_line == 5:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "햄찌찌씨를 도와 잃어버린 선물을 찾아주세요.", font_color, 200, 550, 30)

def hamzzizzi_dialog_clear(input_screen, font_color, input_line):
    dialog = pygame.image.load("images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "ㅠㅠ 다시 오셨네요...ㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "아직도 못 찾았어요....ㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "뭐 말 하고 싶은거 있으신가요....?", font_color, 200, 550, 30)
    elif input_line == 5:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "여기....", font_color, 200, 550, 30)
    elif input_line == 6:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "와! 이거 제가 잃어버렸던 씨앗 맞아요!", font_color, 200, 550, 30)
    elif input_line == 7:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "정말 감사합니다!!!", font_color, 200, 550, 30)
    elif input_line == 8:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "아 혹시 이름이 뭐에요?", font_color, 200, 550, 30)
    elif input_line == 9:
        pixel_font(input_screen, "나", font_color, 295, 490, 30)
        pixel_font(input_screen, "박진철...", font_color, 200, 550, 30)
    elif input_line == 10:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "진철님 정말 감사합니다!!!", font_color, 200, 550, 30)
    elif input_line == 11:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "덕분에 동생 선물을 줄 수 있을 것 같아요!!", font_color, 200, 550, 30)
    elif input_line == 12:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "당신은 행복한 모습으로 가는 햄찌찌씨의 모습을 보며 약간의", font_color, 200, 550, 30)
        pixel_font(input_screen, "따스함을 느꼈습니다...", font_color, 200, 580, 30)
    elif input_line == 13:
        pixel_font(input_screen, "햄찌", font_color, 295, 490, 30)
        pixel_font(input_screen, "찾아주셔서 감사합니다!! 그럼 저는 선물을 주러갈게요!!~~", font_color, 200, 550, 30)

def seed_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "씨앗이 떨어져 있습니다. 이 씨앗의 주인은 누굴까요?", font_color, 200, 550, 30) 
        pixel_font(input_screen, "씨앗을 주으려면 E를 눌러주세요.", font_color, 200, 600, 30)

def pengiun_dialog(input_screen, font_color, input_line):
    dialog = pygame.image.load("images/UIs/Dialog.png")
    input_screen.blit(dialog, (0, 0))

    if input_line == 1:
        pixel_font(input_screen, "???", font_color, 295, 490, 30)
        pixel_font(input_screen, "동물 친구와 멀어져서 대화를 종료하거나 SPACE를 누르면 말을", font_color, 200, 550, 30)
        pixel_font(input_screen, " 걸 수 있습니다.", font_color, 200, 580, 30) 
    elif input_line == 2:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "후에에에엥ㅠㅠㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 3:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "아저씨 저 좀 도와주세요ㅠㅠㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 4:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "엄마가 어디가셨는지 모르겠어요ㅠㅠㅠㅠㅠ", font_color, 200, 550, 30)
    elif input_line == 5:
        pixel_font(input_screen, "팽돌이", font_color, 295, 490, 30)
        pixel_font(input_screen, "팽돌이를 도와 팽돌이 어머니를 찾아주세요.", font_color, 200, 550, 30)
            
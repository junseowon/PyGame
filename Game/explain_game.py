import pygame
from load_sounds import *

def explain_game(input_screen, screen_color, input_font, font_color):
    input_screen.fill(screen_color)
    input_font(input_screen, "당신은 도움의 요정 '박진철'씨가 되어", font_color, 0, 0, 60)
    input_font(input_screen, "동물의 마을로 떠납니다.", font_color, 0, 60, 60)
    input_font(input_screen, "동물의 마을은 친절하고 다양한", font_color, 0, 120, 60)
    input_font(input_screen, "동물 친구들이 살아가는 곳입니다.", font_color, 0, 180, 60)
    input_font(input_screen, "그곳엔 당신의 도움을 필요로", font_color, 0, 240, 60)
    input_font(input_screen, "하는 동물들이 꽤 보이는군요!", font_color, 0, 300, 60)
    input_font(input_screen, "한.. 5마리 정도?", font_color, 0, 360, 60)
    input_font(input_screen, "더 있을 수도 있구요!", font_color, 0, 420, 60)
    input_font(input_screen, "어서 그들에게 다가가주세요.", font_color, 0, 480, 60)
    input_font(input_screen, "보상은.. 저희가 드리는 보수,", font_color, 0, 560, 60)
    input_font(input_screen, "그리고 뿌듯함을 얻으실겁니다!", font_color, 0, 630, 60)
    menu_music(-1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
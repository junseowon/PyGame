import pygame
import time
from load_images import *
from button_UI import *
from load_sounds import *

pygame.init()

#간단한 색상 정의(상수)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#게임 창 크기(상수)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fps = pygame.time.Clock()

howtoplay_button = pygame.image.load("image/buttons_UI/howtoplay_button.png")
howtoplay_button_act = pygame.image.load("image/buttons_UI/howtoplay_button_act.png")

def menu():
    pygame.display.set_caption("menu")
    background(screen, 0, 0)
    use_dung_geun_font(screen, "휴식이 없는 나에게", BLACK, 0, 0, 80)
    use_dung_geun_font(screen, "진정한 휴식이 뭔지 알려주는", BLACK, 0, 80, 80)
    use_dung_geun_font(screen, "감동 깊은 게임", BLACK, 0, 160, 80)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Button(screen, howtoplay_button, 512, 420, 256, 144, howtoplay_button_act, 512,420, Explain_game)

        pygame.display.update()
        fps.tick(60)

def Explain_game():
    screen.fill(BLACK)
    use_dung_geun_font(screen, "당신은 도움의 요정 '박진철'씨가 되어", RED, 0, 0, 60)
    use_dung_geun_font(screen, "동물의 마을로 떠납니다.", RED, 0, 60, 60)
    use_dung_geun_font(screen, "동물의 마을은 친절하고 다양한", RED, 0, 120, 60)
    use_dung_geun_font(screen, "동물 친구들이 살아가는 곳입니다.", RED, 0, 180, 60)
    use_dung_geun_font(screen, "하는 동물들이 꽤 보이는군요!", RED, 0, 240, 60)
    use_dung_geun_font(screen, "한.. 5마리 정도?", RED, 0, 300, 60)
    use_dung_geun_font(screen, "어서 그들에게 다가가주세요.", RED, 0, 360, 60)
    use_dung_geun_font(screen, "보상은.. 저희가 드리는 보수,", RED, 0, 420, 60)
    use_dung_geun_font(screen, "그리고 뿌듯함을 얻으실겁니다!", RED, 0, 480, 60)
    menu_music(-1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
import pygame
import time
from load_images import *
from button_UI import *
from load_sounds import *
from explain_game import explain_game

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

        Button(screen, howtoplay_button, 512, 520, 256, 144, howtoplay_button_act, 512, 520, call_explain_game)

        pygame.display.update()
        fps.tick(60)

def call_explain_game():
    explain_game(screen, BLACK, use_dung_geun_font, RED)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Button(screen, howtoplay_button, 950, 520, 256, 144, howtoplay_button_act, 950, 520, call_explain_game)

        pygame.display.update()
        fps.tick(60)

        
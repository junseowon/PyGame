import pygame
from load_images import *
from button_UI import *

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

def main_menu():
    pygame.display.set_caption("menu")
    background(screen, 0, 0)
    headline(screen, "휴식이 없는 나에게", BLACK, 0, 0, 80)
    headline(screen, "진정한 휴식이 뭔지 알려주는", BLACK, 0, 80, 80)
    headline(screen, "감동 깊은 게임", BLACK, 0, 160, 80)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Button(screen, howtoplay_button, 512, 420, 256, 144, howtoplay_button_act, 512,420, Explain_game)

        pygame.display.update()
        fps.tick(60)

def Explain_game():
    screen.fill(BLACK)
    headline(screen, "나가", RED, 0, 0, 680)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

main_menu()
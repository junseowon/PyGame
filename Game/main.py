import pygame
from load_fonts import *
from button_UI import *
from load_sounds import *
from game import *
from player import *
from animal_quests import *

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

howtoplay_button = pygame.image.load("images/buttons_UI/howtoplay_button.png")
howtoplay_button_act = pygame.image.load("images/buttons_UI/howtoplay_button_act.png")

def play():
    menu(screen, BLACK)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Button(screen, howtoplay_button, 512, 520, 256, 144, howtoplay_button_act, 512, 520, call_explain_game)

        pygame.display.update()
        fps.tick(30)

def call_explain_game():
    explain_game(screen, BLACK, RED)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Button(screen, howtoplay_button, 950, 520, 256, 144, howtoplay_button_act, 950, 520, game)

        pygame.display.update()
        fps.tick(30)

def game():
    screen.fill((0, 255, 0))
    newline = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    newline += 1
                    hamzzizzi_quest(screen, BLACK, newline)
                    
                    if newline > 5:
                        game()
                    
        pygame.display.update()
        fps.tick(30)

play()
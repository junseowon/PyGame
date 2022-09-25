from enum import Flag
import pygame
from load_fonts import *
from button_UI import *
from load_sounds import *
from game import *
from player import *
from animal_quests import *
from player import *

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

def play():
    menu(screen, BLACK)

    howtoplay_button = pygame.image.load("images/UIs/howtoplay_button.png")
    howtoplay_button_act = pygame.image.load("images/UIs/howtoplay_button_act.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Button(screen, howtoplay_button, 512, 520, 256, 144, howtoplay_button_act, 512, 520, call_explain_game)

        pygame.display.update()
        fps.tick(30)

def call_explain_game():
    explain_game(screen, BLACK, RED)

    howtoplay_button = pygame.image.load("images/UIs/howtoplay_button.png")
    howtoplay_button_act = pygame.image.load("images/UIs/howtoplay_button_act.png")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Button(screen, howtoplay_button, 950, 520, 256, 144, howtoplay_button_act, 950, 520, game)

        pygame.display.update()
        fps.tick(30)


player_posX = 0
player_posY = 0

is_up = False
is_down = False
is_right = False
is_left = False

walkCount = 0

def player_move():
    global player_posX, player_posY, walkCount, is_up, is_down, is_right, is_left

    screen.fill((0, 0, 0))

    down_walk = [pygame.image.load("images/player/Player_Down_1.png"), pygame.image.load("images/player/Player_Down_1.png"), 
                    pygame.image.load("images/player/Player_Down_1.png"), pygame.image.load("images/player/Player_Down_2.png"),
                    pygame.image.load("images/player/Player_Down_2.png"), pygame.image.load("images/player/Player_Down_2.png")]

    up_walk = [pygame.image.load("images/player/Player_Up_1.png"), pygame.image.load("images/player/Player_Up_1.png"), 
                    pygame.image.load("images/player/Player_Up_1.png"), pygame.image.load("images/player/Player_Up_2.png"),
                    pygame.image.load("images/player/Player_Up_2.png"), pygame.image.load("images/player/Player_Up_2.png")]

    right_walk = [pygame.image.load("images/player/Player_Right_1.png"), pygame.image.load("images/player/Player_Right_1.png"), 
                    pygame.image.load("images/player/Player_Right_2.png"), pygame.image.load("images/player/Player_Right_3.png"),
                    pygame.image.load("images/player/Player_Right_3.png"), pygame.image.load("images/player/Player_Right_4.png")]

    left_walk = [pygame.image.load("images/player/Player_Left_1.png"), pygame.image.load("images/player/Player_Left_1.png"), 
                    pygame.image.load("images/player/Player_Left_2.png"), pygame.image.load("images/player/Player_Left_3.png"),
                    pygame.image.load("images/player/Player_Left_3.png"), pygame.image.load("images/player/Player_Left_4.png")]

    idle = pygame.image.load("images/player/Player_Idle_1.png")

    if walkCount > 5:
        walkCount = 0

    if is_down == True:
        screen.blit(down_walk[walkCount], (player_posX, player_posY))
        walkCount += 1
    elif is_up == True:
        screen.blit(up_walk[walkCount], (player_posX, player_posY))
        walkCount += 1
    elif is_right == True:
        screen.blit(right_walk[walkCount], (player_posX, player_posY))
        walkCount += 1
    elif is_left == True:
        screen.blit(left_walk[walkCount], (player_posX, player_posY))
        walkCount += 1
    else:
        screen.blit(idle, ( player_posX, player_posY))



def game():
    
    newline = 0
    global player_posX, player_posY, walkCount, is_up, is_down, is_right, is_left

    while True:
        fps.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    newline += 1
                    hamzzizzi_quest(screen, BLACK, newline)
                   
                    if newline > 5:
                        game()

                if event.key == pygame.K_w:
                    is_up = True
                    is_down = False
                    is_right = False
                    is_left = False
                if event.key == pygame.K_s:
                    is_down = True
                    is_up = False
                    is_right = False
                    is_left = False
                if event.key == pygame.K_d:
                    is_right = True
                    is_down = False
                    is_up = False
                    is_left = False
                if event.key == pygame.K_a:
                    is_left = True
                    is_right = False
                    is_down = False
                    is_up = False
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    is_up = False
                    is_down = False
                    is_right = False
                    is_left = False
                if event.key == pygame.K_s:
                    is_up = False
                    is_down = False
                    is_right = False
                    is_left = False
                if event.key == pygame.K_d:
                    is_up = False
                    is_down = False
                    is_right = False
                    is_left = False
                if event.key == pygame.K_a:
                    is_up = False
                    is_down = False
                    is_right = False
                    is_left = False
       
        if is_down == True:
            player_posY += 10
        elif is_up == True:
            player_posY -= 10
        elif is_right == True:
            player_posX += 10
        elif is_left == True:
            player_posX -= 10
        else:
            walkCount = 0
        
        player_move()
        pygame.display.update()
           
play()
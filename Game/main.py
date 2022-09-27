import pygame
from load_fonts import *
from button_UI import *
from load_sounds import *
from game import *
from player import *
from status_window import *
from player import *

pygame.init()

#간단한 색상
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#게임 창 크기
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fps = pygame.time.Clock()

#시작하면 메뉴창에서 시작, 메뉴함수는 game모듈에서 확인 가능!!
def start_game():
    menu(screen, BLACK)
    #버튼 이미지 불러오기
    howtoplay_button = pygame.image.load("images/UIs/howtoplay_button.png")
    howtoplay_button_act = pygame.image.load("images/UIs/howtoplay_button_act.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #버튼 누르면 게임 설명(call_explain_game)으로 넘어감 버튼 클래스는 buttton_UI모듈에서 확인 가능!!
        Button(screen, howtoplay_button, 512, 520, 256, 144, howtoplay_button_act, 512, 520, call_explain_game)

        pygame.display.update()
        fps.tick(30)

#시작하면 설명창에서 시작, 게임설명함수는 game모듈에서 확인 가능!!
def call_explain_game():
    explain_game(screen, (255, 192, 203), BLACK)
    #버튼 이미지 불러오기
    howtoplay_button = pygame.image.load("images/UIs/start_button.png")
    howtoplay_button_act = pygame.image.load("images/UIs/start_button_act.png")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #버튼 누르면 게임 플레이(main_game)로 넘어감 버튼 클래스는 buttton_UI모듈에서 확인 가능!!
        Button(screen, howtoplay_button, 950, 520, 256, 144, howtoplay_button_act, 950, 520, main_game)

        pygame.display.update()
        fps.tick(30)

#플레이어 기본 위치
player_posX = 0
player_posY = 0

#플레이어 걷기 횟수 감지 변수
walkCount = 0

#키보드 키 누르는 상태
is_up = False
is_down = False
is_right = False
is_left = False

#플레이어 움직임 애니메이션과 그리기함수!
def player_load():

    global player_posX, player_posY, is_up, is_down, is_right, is_left, walkCount
    #아래로 걷는 프레임!
    down_walk = [pygame.image.load("images/player/Player_Down_1.png"), pygame.image.load("images/player/Player_Down_1.png"), 
                    pygame.image.load("images/player/Player_Down_1.png"), pygame.image.load("images/player/Player_Down_2.png"),
                    pygame.image.load("images/player/Player_Down_2.png"), pygame.image.load("images/player/Player_Down_2.png")]
    #위로 걷는 프레임!
    up_walk = [pygame.image.load("images/player/Player_Up_1.png"), pygame.image.load("images/player/Player_Up_1.png"), 
                    pygame.image.load("images/player/Player_Up_1.png"), pygame.image.load("images/player/Player_Up_2.png"),
                    pygame.image.load("images/player/Player_Up_2.png"), pygame.image.load("images/player/Player_Up_2.png")]
    #오른쪽으로 걷는 프레임!
    right_walk = [pygame.image.load("images/player/Player_Right_1.png"), pygame.image.load("images/player/Player_Right_1.png"), 
                    pygame.image.load("images/player/Player_Right_2.png"), pygame.image.load("images/player/Player_Right_3.png"),
                    pygame.image.load("images/player/Player_Right_3.png"), pygame.image.load("images/player/Player_Right_4.png")]
    #왼쪽으로 걷는 프레임!
    left_walk = [pygame.image.load("images/player/Player_Left_1.png"), pygame.image.load("images/player/Player_Left_1.png"), 
                    pygame.image.load("images/player/Player_Left_2.png"), pygame.image.load("images/player/Player_Left_3.png"),
                    pygame.image.load("images/player/Player_Left_3.png"), pygame.image.load("images/player/Player_Left_4.png")]
    #가만히 있는 프레임!
    idle = pygame.image.load("images/player/Player_Idle_1.png")
    #걷기횟수가 5초과면 0으로!
    if walkCount > 5:
        walkCount = 0

    if is_down == True:
        screen.blit(down_walk[walkCount], (player_posX, player_posY))       #프레임 값을 가져와서 x, y위치에 그리기!
        walkCount += 1
    elif is_up == True:
        screen.blit(up_walk[walkCount], (player_posX, player_posY))         #프레임 값을 가져와서 x, y위치에 그리기!
        walkCount += 1
    elif is_right == True:
        screen.blit(right_walk[walkCount], (player_posX, player_posY))      #프레임 값을 가져와서 x, y위치에 그리기!
        walkCount += 1
    elif is_left == True:
        screen.blit(left_walk[walkCount], (player_posX, player_posY))       #프레임 값을 가져와서 x, y위치에 그리기!
        walkCount += 1
    else:
        screen.blit(idle, ( player_posX, player_posY))

#동물 친구들 기본 위치
animal_posX = 0
animal_posY = 0

#동물 친구와 충돌 상태
is_animal_touch = False

animal_image = pygame.image.load("images/characters/hamster_zzizzi.png").convert_alpha()
player_image = pygame.image.load("images/player/Player_Idle_1.png").convert_alpha()

class Player(pygame.sprite.Sprite):
    def __init__(self, input_player_image):
        pygame.sprite.Sprite.__init__(self)
        self.input_player_image = input_player_image
        self.rect = self.input_player_image.get_rect()
        self.rect.center = (player_posX, player_posY)
        self.mask = pygame.mask.from_surface(input_player_image)

class Animal(pygame.sprite.Sprite):
    def __init__(self, input_animal_image):
        pygame.sprite.Sprite.__init__(self)
        self.input_animal_image = input_animal_image
        self.rect = self.input_animal_image.get_rect()
        self.rect.center = (animal_posX, animal_posY)
        self.mask = pygame.mask.from_surface(input_animal_image)

is_read = False
is_move = True

#시작하면 게임창에서 시작
def main_game():
    global player_posX, player_posY, is_up, is_down, is_right, is_left
    global walkCount, is_animal_touch, is_read, is_move, animal_posX, animal_posY, animal_image, player_image

    player_posX = 565
    player_posY = 285

    animal_posX = 665
    animal_posY = 185

    line = 0

    while True:

        animal = Animal(animal_image)
        player = Player(player_image)

        fps.tick(30)
        if is_move == True:
            screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                is_move = True
                if event.key == pygame.K_SPACE:
                    is_read = True                    

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
                is_move = True
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
            screen.fill((0, 0, 0))
        elif is_up == True:
            player_posY -= 10
            screen.fill((0, 0, 0))
        elif is_right == True:
            player_posX += 10
            screen.fill((0, 0, 0))
        elif is_left == True:
            player_posX -= 10
            screen.fill((0, 0, 0))
        else:
            walkCount = 0

        if pygame.sprite.collide_rect(player, animal):
            hamzzizzi_dialog(screen, BLACK, line)            

            if is_read == True or line == 0:
                line += 1
                hamzzizzi_dialog(screen, BLACK, line)
                is_read = False

                if line > 5:
                    line = 0
    
        if is_animal_touch == False:
            screen.blit(animal_image, (animal_posX, animal_posY))

        player_load()

        pygame.display.update()

start_game()
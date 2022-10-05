import pygame
from load_fonts import *
from button_UI import *
from load_sounds import *
from game import *
from status_window import *
from load_backgrounds import *
from collision_detection import *
from load_building import *

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
    howtoplay_button = pygame.image.load("Game/images/UIs/howtoplay_button.png")
    howtoplay_button_act = pygame.image.load("Game/images/UIs/howtoplay_button_act.png")

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

#플레이어 걷기 프레임 수 변수
walkCount = 0

#키보드 키 누르는 상태
is_up = False
is_down = False
is_right = False
is_left = False

def stop_move():
    global is_down, is_left, is_right, is_up
    is_up = False
    is_down = False
    is_right = False
    is_left = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/UIs/collision_box.png").convert_alpha()
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(topleft = (365, 285))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
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
                    pygame.image.load("images/player/Player_Right_3.png"), pygame.image.load("images/player/Player_Right_2.png")]
    #왼쪽으로 걷는 프레임!
        left_walk = [pygame.image.load("images/player/Player_Left_1.png"), pygame.image.load("images/player/Player_Left_1.png"), 
                        pygame.image.load("images/player/Player_Left_2.png"), pygame.image.load("images/player/Player_Left_3.png"),
                    pygame.image.load("images/player/Player_Left_3.png"), pygame.image.load("images/player/Player_Left_2.png")]
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

        self.rect.topleft = (player_posX, player_posY)

#시작하면 게임창에서 시작
def main_game():
    #음악 재생
    menu_music(0, 1)
    background_music(1, 0.5)

    #플레이어 움직임
    global player_posX, player_posY, is_up, is_down, is_right, is_left, walkCount

    #대화 넘기기
    line = 1

    #읽는 상태
    is_read = False

    #동물 퀘스트 클리어
    animal_quest_clear = False

    #동물 퀘스트 충돌감지
    animal_quest_collision = False

    #동물 퀘스트 그리기
    animal_quest_draw = False

    #동물 클리어 상태
    hamzzizzi_clear = False
    pengiun_clear = False

    #배경 상태
    background = 1
    
    #플레이어 처음 위치
    player_posX = 0
    player_posY = 320

    #햄스터
    hamzzizzi_incomplete = pygame.image.load("images/characters/hamster_zzizzi.png")
    hamzzizzi_complete = pygame.image.load("images/characters/hamster_zzizzi_success.png")
    #팽귄
    pengiun_incomplete = pygame.image.load("images/characters/penguin_cry.png")
    pengiun_complete = pygame.image.load("images/characters/penguin_smile.png")
    #아이템
    sunflower_seed = pygame.image.load("images/quests/sunflower_seeds.png")
    duck_doll = pygame.image.load("images/quests/duck_doll.png")
    #장애물
    pond = pygame.image.load("images/backgrounds/pond.png")


    player = pygame.sprite.GroupSingle(Player())

    animal = pygame.sprite.GroupSingle(Animal(hamzzizzi_incomplete, 865, 85))
    animal_quest = pygame.sprite.GroupSingle(Quest(sunflower_seed, 1250, 50))

    obstacle = pygame.sprite.GroupSingle(Obstacle(pond, 150, 150))

    while True:

        fps.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_read = True

                if event.key == pygame.K_e and animal_quest_collision == True:                    
                    animal_quest_clear = True

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
                    stop_move()
                if event.key == pygame.K_s:
                    stop_move()
                if event.key == pygame.K_d:
                    stop_move()
                if event.key == pygame.K_a:
                    stop_move()

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

        if player_posX < -90:
            player_posX = 1270
            background = 1
        
        if player_posX > 1280:
            player_posX = -75
            background = 2
        
        if player_posY < -90:
            player_posY = 760
            background = 3
        #배경 1
        if background == 1:
            background_1(screen)
            obstacle.draw(screen)
        
            player.update()

            if player_posX < -25 or player_posY > 565 or player_posY < 5:
                stop_move()
            
            #햄스터 미션
            if hamzzizzi_clear == False:
                animal.draw(screen)
                animal_quest.draw(screen)

                if pygame.sprite.spritecollide(player.sprite, animal, False, pygame.sprite.collide_mask) and animal_quest_clear == False:
                    stop_move()
                    hamzzizzi_dialog(screen, BLACK, line)            

                    if is_read == True or line == 0:
                        line += 1
                        hamzzizzi_dialog(screen, BLACK, line)
                        is_read = False

                        if line > 5:                    
                            line = 1
                            is_read = False
                elif pygame.sprite.spritecollide(player.sprite, animal, False, pygame.sprite.collide_mask) and animal_quest_clear == True:
                    stop_move()
                    hamzzizzi_dialog_clear(screen, BLACK,line)

                    if is_read == True or line == 0:
                        line += 1
                        hamzzizzi_dialog_clear(screen, BLACK, line)
                        is_read = False

                        if line == 6:
                            animal = pygame.sprite.GroupSingle(Animal(hamzzizzi_complete, 865, 85))

                        if line > 13:
                            line = 1
                            is_read = False
                            hamzzizzi_clear = True
                            animal_quest_clear = False
                        
                        if hamzzizzi_clear == True:
                            animal.remove(animal)
                            animal = pygame.sprite.GroupSingle(Animal(pengiun_incomplete, 350, 150))
                            animal_quest_draw = True
                            

                if pygame.sprite.spritecollide(player.sprite, animal_quest, False, pygame.sprite.collide_mask):
                    animal_quest_collision = True
                    stop_move()
                    seed_dialog(screen, BLACK, line)

                    if is_read == True or line == 0:
                        line += 1
                        seed_dialog(screen, BLACK, line)
                        is_read = False

                        if line > 1:
                            line = 1
                            is_read = False
                            
                    if animal_quest_clear == True:
                        line = 1                
                        is_read = False
                        animal_quest_collision = False
                        animal_quest.remove(animal_quest)
                                    
            #팽귄 미션
            if pengiun_clear == False:
                if hamzzizzi_clear == True:                
                    animal.draw(screen)

                    if pygame.sprite.spritecollide(player.sprite, animal, False, pygame.sprite.collide_mask) and animal_quest_clear == False:
                        stop_move()
                        pengiun_dialog(screen, BLACK, line)            

                        if is_read == True or line == 0:
                            line += 1
                            pengiun_dialog(screen, BLACK, line)
                            is_read = False

                            if line > 5:                    
                                line = 1
                                is_read = False
                    elif pygame.sprite.spritecollide(player.sprite, animal, False, pygame.sprite.collide_mask) and animal_quest_clear == True:
                        stop_move()
                        pengiun_dialog_clear(screen, BLACK,line)

                        if is_read == True or line == 0:
                            line += 1
                            pengiun_dialog_clear(screen, BLACK, line)
                            is_read = False

                            if line == 11:
                                animal = pygame.sprite.GroupSingle(Animal(pengiun_complete, 350, 150))

                            if line > 13:
                                line = 1
                                is_read = False
                                pengiun_clear = True
                                animal_quest_clear = False
                            
                            if pengiun_clear == True:
                                animal.remove(animal)
                                #animal = pygame.sprite.GroupSingle(Animal(pengiun_incomplete, 350, 150))                                

            #장애물 처리
            if pygame.sprite.spritecollide(player.sprite, obstacle, False, pygame.sprite.collide_mask):
                stop_move()

                obstacle_dialog(screen, BLACK, line)

                if is_read == True or line == 0:
                    line += 1
                    obstacle_dialog(screen, BLACK, line)
                    is_read = False

                    if line > 1:
                        line = 1
                        is_read = False   

            #아무것도 안 할 때
            if not pygame.sprite.spritecollide(player.sprite, animal, False, pygame.sprite.collide_mask) and not pygame.sprite.spritecollide(player.sprite, animal_quest, False, pygame.sprite.collide_mask):
                line = 0
                is_read = False
        #배경 2
        elif background == 2:
            background_2(screen)

            player.update()
            if hamzzizzi_clear == True:
                if pengiun_clear == False:
                    animal_quest.draw(screen)
                    if animal_quest_draw == True:
                        animal_quest = pygame.sprite.GroupSingle(Quest(duck_doll, 500, 200))                    

                    if pygame.sprite.spritecollide(player.sprite, animal_quest, False, pygame.sprite.collide_mask):
                        animal_quest_collision = True
                        stop_move()
                        duck_doll_dialog(screen, BLACK, line)

                        if is_read == True or line == 0:
                            line += 1
                            duck_doll_dialog(screen, BLACK, line)
                            is_read = False

                            if line > 1:
                                line = 1
                                is_read = False
                                
                        if animal_quest_clear == True:
                            line = 1                
                            is_read = False
                            animal_quest_collision = False
                            animal_quest_draw = False
                            animal_quest.remove(animal_quest)
            
            if not pygame.sprite.spritecollide(player.sprite, animal, False, pygame.sprite.collide_mask) and not pygame.sprite.spritecollide(player.sprite, animal_quest, False, pygame.sprite.collide_mask):
                line = 0
                is_read = False
        
        #배경 3
        elif background == 3:
            background_3(screen)
            player.update()
    
        pygame.display.update()

start_game()

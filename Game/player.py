import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fps = pygame.time.Clock()

player_x_pos = 0
player_y_pos = 0

is_right = False
is_left = False
is_up = False
is_down = False

walkCount = 0

left_walk = [pygame.image.load("images/player/Player_Moving_Left_1.png"), pygame.image.load("images/player/Player_Moving_Left_2.png")]

right_walk = [pygame.image.load("images/player/Player_Moving_Right_1.png"), pygame.image.load("images/player/Player_Moving_Right_2.png")]

up_walk = [pygame.image.load("images/player/Player_Moving_Up_1.png"), pygame.image.load("images/player/Player_Moving_Up_2.png")]

down_walk = [pygame.image.load("images/player/Player_Moving_Down_1.png"), pygame.image.load("images/player/Player_Moving_Down_2.png")]

idle = pygame.image.load("images/player/Player_Idle_1.png")

def playerMove():
    global walkCount, player_x_pos, player_y_pos

    screen.fill((0, 0, 0))

    if walkCount > 1:
        walkCount = 0

    if is_left == True:
        screen.blit(left_walk[walkCount], (player_x_pos, player_y_pos))
        walkCount += 1
    elif is_right == True:
        screen.blit(right_walk[walkCount], (player_x_pos, player_y_pos))
        walkCount += 1
    elif is_up == True:
        screen.blit(up_walk[walkCount], (player_x_pos, player_y_pos))
        walkCount += 1
    elif is_down == True:
        screen.blit(down_walk[walkCount], (player_x_pos, player_y_pos))
        walkCount += 1
    else:
        screen.blit(idle, (player_x_pos, player_y_pos))

while True:
    fps.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                is_right = True
                is_left = False
                is_up = False
                is_down = False
            if event.key == pygame.K_LEFT:
                is_left = True
                is_right = False
                is_up = False
                is_down = False
            if event.key == pygame.K_UP:
                is_up = True
                is_down = False
                is_right = False
                is_left = False
            if event.key == pygame.K_DOWN:
                is_down = True
                is_up = False
                is_left = False
                is_right = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                is_right = False
                is_left = False
                is_up = False
                is_down = False
            if event.key == pygame.K_LEFT:
                is_left = False
                is_right = False
                is_up = False
                is_down = False
            if event.key == pygame.K_UP:
                is_left = False
                is_right = False
                is_up = False
                is_down = False
            if event.key == pygame.K_DOWN:
                is_left = False
                is_right = False
                is_up = False
                is_down = False

    if is_right == True:
        player_x_pos += 10
    elif is_left == True:
        player_x_pos -= 10
    elif is_up == True:
        player_y_pos -= 10
    elif is_down == True:
        player_y_pos += 10
    else:
        walkCount = 0

    playerMove()

    pygame.display.update()
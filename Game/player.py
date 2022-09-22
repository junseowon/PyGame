import pygame

def player_move(input_screen, input_fps):
    player_posX = 0
    player_posY = 0

    is_right = False
    is_left = False

    walkCount = 0

    right_walk = [pygame.image.load("images/player/Player_Right_1.png"), pygame.image.load("images/player/Player_Right_2.png")]

    left_walk = [pygame.image.load("images/player/Player_Left_1.png"), pygame.image.load("images/player/Player_Left_2.png")]

    idle = pygame.image.load("images/player/Player_Idle_1.png")

    if walkCount > 1:
        walkCount = 0

    if is_left == True:
        input_screen.blit(left_walk[walkCount], (player_posX, player_posY))
        walkCount += 1
    elif is_right == True:
        input_screen.blit(right_walk[walkCount], (player_posX, player_posY))
        walkCount += 1
    else:
        input_screen.blit(idle, ( player_posX, player_posY))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    is_right = True
                    is_left = False
                if event.key == pygame.K_a:
                    is_left = True
                    is_right = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    is_right = False
                    is_left = False
                if event.key == pygame.K_a:
                    is_left = False
                    is_right = False
        
        if is_right == True:
            player_posX += 10

        elif is_left == True:
            player_posY -= 10

        else:
            walkCount = 0

        pygame.display.update()
        input_fps.tick(30)
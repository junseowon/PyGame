import pygame

def background_1(input_screen):

    ground = pygame.image.load("images/backgrounds/ground_1.png")

    input_screen.blit(ground, (0, 0))

def background_2(input_screen):

    input_screen.fill((0, 255, 0))
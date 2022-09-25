import pygame

def menu_music(set_play, set_volume):
    pygame.mixer.music.load("sounds/menu_music.mp3")
    pygame.mixer.music.set_volume(set_volume / 10)

    if set_play == 1:
        pygame.mixer.music.play(-1)

    if set_play == 0:
        pygame.mixer.music.stop()

def background_music(set_play, set_volume):
    pygame.mixer.music.load("sounds/background_music.mp3")
    pygame.mixer.music.set_volume(set_volume / 10)

    if set_play == 1:
        pygame.mixer.music.play(-1)

    if set_play == 0:
        pygame.mixer.music.stop()
import pygame

def menu_music(set_play, set_volume):
    sound = pygame.mixer.Sound("sounds/No.8 Requiem - Esther Abrami.mp3")
    sound.play(set_play)
    sound.set_volume(set_volume / 10)
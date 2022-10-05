import pygame

class Animal(pygame.sprite.Sprite):
    def __init__(self, animal, animal_x, animal_y):
        super().__init__()
        self.image = animal
        self.rect = self.image.get_rect(center = (animal_x, animal_y))
        self.mask = pygame.mask.from_surface(self.image)

class Quest(pygame.sprite.Sprite):
    def __init__(self, quest, quest_x, quest_y):
        super().__init__()
        self.image = quest
        self.rect = self.image.get_rect(center = (quest_x, quest_y))
        self.mask = pygame.mask.from_surface(self.image)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle, obstacle_x, obstacle_y):
        super().__init__()
        self.image = obstacle
        self.rect = self.image.get_rect(center = (obstacle_x, obstacle_y))
        self.mask = pygame.mask.from_surface(self.image)
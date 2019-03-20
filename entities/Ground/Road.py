import pygame

from entities.Ground.AbstractEntities import AbstractEntities


class Road(AbstractEntities):
    def __init__(self, x, y):
        self.image = pygame.image.load("resources/sprites/dirt.png")
        self.image = pygame.transform.scale(self.image, (32, 32))

        super().__init__("Road", self.image, x, y)

import pygame
import os

class Belly(pygame.sprite.Sprite):
    def __init__(self, width, height, cords, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((148, 57, 107))
        self.cords = cords
        self.direction = direction
        self.setRect(direction)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()

    def setRect(self, direction):
        if self.direction == "left":
            self.rect = self.image.get_rect(midleft = self.cords)
        elif self.direction == "right":
            self.rect = self.image.get_rect(midright = self.cords)
        elif self.direction == "up":
            self.rect = self.image.get_rect(midtop = self.cords)
        elif self.direction == "down":
            self.rect = self.image.get_rect(midbottom = self.cords)

    def blit(self, screen):
        screen.blit(self.image, self.rect)
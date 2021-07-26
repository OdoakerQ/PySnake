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

    def setRect(self, direction):
        if self.direction == "left":
            self.rect = self.image.get_rect(midleft = self.cords)
        elif self.direction == "right":
            self.rect = self.image.get_rect(midright = self.cords)
        elif self.direction == "up":
            self.rect = self.image.get_rect(midtop = self.cords)
        elif self.direction == "down":
            self.rect = self.image.get_rect(midbottom = self.cords)

    def rotate(self, head):
        if self.direction == "left":
            angle = 90 if head.direction == "up" else -90
        elif self.direction == "right":
            angle = -90 if head.direction == "up" else 90
            self.direction = "right"
        elif self.direction == "up":
            angle = -90 if head.direction == "left" else 90
            self.direction = "up"
        elif self.direction == "down":
            angle = 90 if head.direction == "left" else -90
            self.direction = "down"

        self.direction = head.direction
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()

    def blit(self, screen):
        screen.blit(self.image, self.rect)
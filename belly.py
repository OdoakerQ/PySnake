import pygame
import os

class Belly(pygame.sprite.Sprite):
    def __init__(self, width, height, cords, direction, is_first = False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((87, 176, 48))
        self.direction = direction
        self.is_first = is_first
        self.spawnRotate()
        self.spawn(cords)

    def spawn(self, cords):
        if self.direction == "left":
            self.rect = self.image.get_rect(midleft = cords)
        elif self.direction == "right":
            self.rect = self.image.get_rect(midright = cords)
        elif self.direction == "up":
            self.rect = self.image.get_rect(midtop = cords)
        elif self.direction == "down":
            self.rect = self.image.get_rect(midbottom = cords)

    def getCords(self):
        if self.direction == "left":
            return self.rect.midright
        elif self.direction == "right":
            return self.rect.midleft
        elif self.direction == "up":
            return self.rect.midbottom
        elif self.direction == "down":
            return self.rect.midtop

    def move(self, head_direction, head_rect):
        if self.is_first:
            if head_direction == "left":
                self.rect.midleft = head_rect.midright
            elif head_direction == "right":
                self.rect.midright = head_rect.midleft
            elif head_direction == "up":
                self.rect.midtop = head_rect.midbottom
            elif head_direction == "down":
                self.rect.midbottom = head_rect.midtop
        else:
            self.rect.x, self.rect.y = head_rect.x, head_rect.y

    def rotate(self, head_direction):
        if self.direction == "left":
            angle = 90 if head_direction == "up" else -90
        elif self.direction == "right":
            angle = -90 if head_direction == "up" else 90
            self.direction = "right"
        elif self.direction == "up":
            angle = -90 if head_direction == "left" else 90
            self.direction = "up"
        elif self.direction == "down":
            angle = 90 if head_direction == "left" else -90
            self.direction = "down"

        self.direction = head_direction
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()

    def spawnRotate(self):
        if self.direction == "left":
            return
        elif self.direction == "right":
            angle = 180
        elif self.direction == "up":
            angle = 90
        elif self.direction == "down":
            angle = -90

        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()

    def blit(self, screen):
        screen.blit(self.image, self.rect)
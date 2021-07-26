import pygame
import os

class SnakeHead():
    def __init__(self, x : int, y : int, direction : str, options):
        self.image = pygame.image.load(os.path.join(options.path, "images/head.png")).convert_alpha()
        self.cords = (x, y)
        self.rect = self.image.get_rect(topleft = (self.cords))
        self.direction = direction

    def getBackHead(self):
        if self.direction == "left":
            return self.rect.midright
        elif self.direction == "right":
            return self.rect.midleft
        elif self.direction == "up":
            return self.rect.midbottom
        elif self.direction == "down":
            return self.rect.midtop

    def getDirection(self):
        return self.direction

    def rotate(self, key):
        if self.direction == "left":
            angle = -90 if key == pygame.K_w else 90
        elif self.direction == "right":
            angle = 90 if key == pygame.K_w else -90
        elif self.direction == "up":
            angle = 90 if key == pygame.K_a else -90
        elif self.direction == "down":
            angle = -90 if key == pygame.K_a else 90

        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(topleft = self.rect.topleft)

    def move(self):
        if self.direction == "left":
            x, y = -21, 0
        elif self.direction == "right":
            x, y = 21, 0
        elif self.direction == "up":
            x, y = 0, -21
        elif self.direction == "down":
            x, y = 0, 21

        self.rect.move_ip(x, y)

    def blit(self, screen):
        screen.blit(self.image, self.rect)


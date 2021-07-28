import pygame
import os

class SnakeHead():
    def __init__(self, x : int, y : int, direction : str, options):
        self.image = pygame.image.load(os.path.join(options.path, "images/snake_head_2.png")).convert_alpha()
        self.cords = (x, y)
        self.rect = self.image.get_rect(center = (self.cords))
        self.direction = direction
        self.options = options

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

    def rotate(self, key, headBelly, primaryDirection, newDirection):
        if self.direction == "left":
            angle = -90 if key == pygame.K_w else 90
        elif self.direction == "right":
            angle = 90 if key == pygame.K_w else -90
        elif self.direction == "up":
            angle = 90 if key == pygame.K_a else -90
        elif self.direction == "down":
            angle = -90 if key == pygame.K_a else 90

        self.image = pygame.transform.rotate(self.image, angle)
        self.setRectAfterRotation(headBelly, primaryDirection, newDirection)
        self.direction = newDirection

        self.rect = self.image.get_rect(topleft = self.rect.topleft)

    def setRectAfterRotation(self, headBelly, primaryDirection, newDirection):
        oldDirection = primaryDirection

        if oldDirection == newDirection:
            if newDirection == "left":
                self.rect = self.image.get_rect(midright = headBelly.rect.midleft)
            elif newDirection == "right":
                self.rect = self.image.get_rect(midleft = headBelly.rect.midright)
            elif newDirection == "up":
                self.rect = self.image.get_rect(midbottom = headBelly.rect.midtop)
            elif newDirection == "down":
                self.rect = self.image.get_rect(midtop = headBelly.rect.midbottom)
        elif oldDirection == "left":
            if newDirection == "up":
                self.rect = self.image.get_rect(bottomright = headBelly.rect.bottomleft)
            else:
                self.rect = self.image.get_rect(topright = headBelly.rect.topleft)
        elif oldDirection == "right":
            if newDirection == "up":
                self.rect = self.image.get_rect(bottomleft = headBelly.rect.bottomright)
            else:
                self.rect = self.image.get_rect(topleft = headBelly.rect.topright)
        elif oldDirection == "up":
            if newDirection == "left":
                self.rect = self.image.get_rect(bottomright = headBelly.rect.topright)
            else:
                self.rect = self.image.get_rect(bottomleft = headBelly.rect.topleft)
        elif oldDirection == "down":
            if newDirection == "left":
                self.rect = self.image.get_rect(topright = headBelly.rect.bottomright)
            else:
                self.rect = self.image.get_rect(topleft = headBelly.rect.bottomleft)

    def move(self):
        if self.direction == "left":
            x, y = -self.options.speed, 0
        elif self.direction == "right":
            x, y = self.options.speed, 0
        elif self.direction == "up":
            x, y = 0, -self.options.speed
        elif self.direction == "down":
            x, y = 0, self.options.speed

        self.rect.move_ip(x, y)

    def blit(self, screen):
        screen.blit(self.image, self.rect)


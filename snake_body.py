import pygame
import os

from pygame.transform import rotate
from belly import Belly

class SnakeBody():
    def __init__(self, cords, direction):
        self.body = []
        self.first_belly = Belly(19, 19, cords, direction)
        self.body.append(self.first_belly)

    def add(self, belly):
        self.body.add(belly)

    def move(self, screen, head, speed):
        afterBelly = self.body[0]
        if head.direction != self.body[0].direction:
            self.body[0].rotate(head)
        self.moveHeadBody(self.body[0], head)

        for belly in self.body[1:]:
            beforeBelly = belly
            if head.direction != afterBelly.direction:
                belly.rotate(afterBelly)
            self.moveHeadBody(self.body[0], afterBelly)

            afterBelly = beforeBelly

    def moveHeadBody(self, belly, head):
        if head.direction == "left":
            belly.rect.midleft = head.rect.midright
        elif head.direction == "right":
            belly.rect.midright = head.rect.midleft
        elif head.direction == "up":
            belly.rect.midtop = head.rect.midbottom
        elif head.direction == "down":
            belly.rect.midbottom = head.rect.midtop

    def blit(self, screen):
        for belly in self.body:
            belly.blit(screen)
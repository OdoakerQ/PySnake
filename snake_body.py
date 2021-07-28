import pygame
import os
import copy
from pygame.transform import rotate
from belly import Belly

class SnakeBody():
    def __init__(self, cords, direction, options):
        self.bellies = []
        self.options = options
        for _ in range(2):
            lastBelly = Belly(options.part_width, options.bellyWidth, cords, direction)
            self.bellies.append(lastBelly)
            cords = lastBelly.rect.midright

    def add(self, belly):
        self.bellies.add(belly)

    def move(self, screen, head):
        firstBelly = self.bellies[0]
        cords = self.getCords(firstBelly)
        head_part = Belly(self.options.part_width, self.options.bellyWidth, cords, firstBelly.direction)
        if head.direction != self.bellies[0].direction:
            self.bellies[0].rotate(head)
        self.movePart(self.bellies[0], head)

        for belly in self.bellies[1:]:
            cords = self.getCords(head_part)
            beforeBelly = Belly(self.options.part_width, self.options.bellyWidth, cords, belly.direction)
            if head_part.direction != belly.direction:
                belly.rotate(belly)
            self.movePart(belly, head_part)

            head_part = beforeBelly

    def getCords(self, head):
        if head.direction == "left":
            return head.rect.midleft
        elif head.direction == "right":
            return head.rect.midright
        elif head.direction == "up":
            return head.rect.midtop
        elif head.direction == "down":
            return head.rect.midbottom

    def movePart(self, belly, head):
        if head.direction == "left":
            belly.rect.midleft = head.rect.midright
        elif head.direction == "right":
            belly.rect.midright = head.rect.midleft
        elif head.direction == "up":
            belly.rect.midtop = head.rect.midbottom
        elif head.direction == "down":
            belly.rect.midbottom = head.rect.midtop

    def blit(self, screen):
        for belly in self.bellies:
            belly.blit(screen)
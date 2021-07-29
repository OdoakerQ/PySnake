import pygame
import os
import copy
from pygame.transform import rotate
from belly import Belly

class SnakeBody():
    def __init__(self, cords, direction, options):
        self.bellies = []
        self.options = options
        firstBelly = Belly(options.belly_width, options.square_side, cords, direction, True)
        self.bellies.append(firstBelly)
        cords = firstBelly.getCords()

        for _ in range(options.belly_number - 1):
            lastBelly = Belly(options.belly_width, options.square_side, cords, direction)
            self.bellies.append(lastBelly)
            cords = lastBelly.getCords()

    def enlarge(self):
        cords = self.bellies[-1].getCords()
        direction = self.bellies[-1].direction

        firstBelly = Belly(self.options.belly_width, self.options.square_side, cords, direction)
        self.bellies.append(firstBelly)
        cords = firstBelly.getCords()


        for _ in range(self.options.belly_number - 1):
            lastBelly = Belly(self.options.belly_width, self.options.square_side, cords, direction)
            self.bellies.append(lastBelly)
            cords = lastBelly.getCords()

    def move(self, head):
        firstBelly = self.bellies[0]
        head_belly_direction = copy.deepcopy(firstBelly.direction)
        head_belly_rect = copy.deepcopy(firstBelly.rect)
        if firstBelly.direction != head.direction:
            firstBelly.rotate(head.direction)
        firstBelly.move(head.direction, head.rect)

        for belly in self.bellies[1:]:
            before_belly_direction = copy.deepcopy(belly.direction)
            before_belly_rect = copy.deepcopy(belly.rect)
            if belly.direction != head_belly_direction:
                belly.rotate(head_belly_direction)
            belly.move(head_belly_direction, head_belly_rect)

            head_belly_direction = before_belly_direction
            head_belly_rect = before_belly_rect

    def getHeadBelly(self):
        return self.bellies[0]

    def blit(self, screen):
        for belly in self.bellies:
            belly.blit(screen)
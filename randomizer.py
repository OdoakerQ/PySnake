import pygame
import random

class Randomizer:
    def __init__(self, options):
        self.options = options

    def randomizeCords(self):
        spawn_min_x, spawn_max_x = self.options.spawn_min_x, self.options.spawn_max_x
        spawn_min_y, spawn_max_y = self.options.spawn_min_y, self.options.spawn_max_y
        x = random.randint(spawn_min_x, spawn_max_x)
        y = random.randint(spawn_min_y, spawn_max_y)
        return x, y
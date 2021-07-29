import pygame
import random

class Randomizer:
    def __init__(self, options):
        self.options = options

    def randomizeDefaultCords(self):
        spawn_min_x, spawn_max_x = self.options.spawn_min_x, self.options.spawn_max_x
        spawn_min_y, spawn_max_y = self.options.spawn_min_y, self.options.spawn_max_y
        x = random.randint(spawn_min_x, spawn_max_x)
        y = random.randint(spawn_min_y, spawn_max_y)
        return x, y

    def randomizeDirection(self):
        choice = random.choice([0, 1, 2, 3])
        if choice == 0:
            direction = "left"
        elif choice == 1:
            direction = "right"
        elif choice == 2:
            direction = "up"
        else:
            direction = "down"

        return direction

    def randomizeFruitCords(self, objects):
        (x, y) = self.randomizeDefaultCords()
        is_found = False
        reset = False
        while not is_found:
            for object in objects:
                top_left = object.rect.topleft
                top_right = object.rect.topright
                bottom_left = object.rect.bottomleft
                bottom_right = object.rect.bottomright

                if (x > top_left[0] and x < top_right[0]) or (x > bottom_left[0] and x < bottom_right[0]):
                    if random.choice([0, 1]) == 0:
                        x += self.options.fruit_distance
                    else:
                         x -= self.options.fruit_distance
                    reset = True
                    break
                elif (y < top_right[1] and y > bottom_right[1]) or (y < top_left[1] and y > bottom_left[1]):
                    if random.choice([0, 1]) == 0:
                        y += self.options.fruit_distance
                    else:
                         y -= self.options.fruit_distance
                    reset = True
                    break
            if reset:
                reset = False
                continue
            else:
                is_found = True
        return x, y





import pygame
import os

class Fruit:
    def __init__(self, x, y, options):
        self.image = pygame.image.load(os.path.join(options.path, "images/fruit_1.png")).convert_alpha()
        self.cords = (x, y)
        self.rect = self.image.get_rect(bottomleft = (self.cords))

    def checkIfCollision(self, head):
        if self.rect.colliderect(head.rect) == 1:
            return True
        return False

    def blit(self, screen):
        screen.blit(self.image, self.rect)

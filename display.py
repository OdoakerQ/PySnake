import pygame
import os

class Display:
    def __init__(self, options):
        self.background = pygame.image.load(os.path.join(options.path, "images/background_2.jpg"))
        self.display_size = options.display_size

    def show(self, screen, objects):
        screen.fill((0,0,0))
        screen.blit(self.background, (0,0))

        for object in objects:
            object.blit(screen)

        pygame.display.update()
        pygame.display.flip()




import pygame

class KeyboardHandler:
    def __init__(self, direction):
        self.primaryDirection = direction
        self.lastDirection = direction

    def handleKey(self, event, screen, head, body, options):
        key = event.key

        newDirection = self.setNewDirection(key)

        if self.isEqualDirection(key, newDirection):
            return

        if newDirection == "left" and not self.isDirectionConflict("left"):
            head.rotate(key)
            head.direction = "left"
        elif newDirection == "right" and not self.isDirectionConflict("right"):
            head.rotate(key)
            head.direction = "right"
        elif newDirection == "up" and not self.isDirectionConflict("up"):
            head.rotate(key)
            head.direction = "up"
        elif newDirection == "down" and not self.isDirectionConflict("down"):
            head.rotate(key)
            head.direction = "down"
        else:
            return

        self.lastDirection = head.direction

        screen.fill(options.background_color)

        head.blit(screen)
        body.blit(screen)

        pygame.display.update()
        pygame.display.flip()

    def setNewDirection(self, key):
        if key == pygame.K_a:
            return "left"
        elif key == pygame.K_d:
            return "right"
        elif key == pygame.K_w:
            return "up"
        elif key == pygame.K_s:
            return "down"

    def isDirectionConflict(self, newDirection):
        if newDirection == "left" and self.primaryDirection == "right":
            return True
        elif newDirection == "right" and self.primaryDirection == "left":
            return True
        elif newDirection == "up" and self.primaryDirection == "down":
            return True
        elif newDirection == "down" and self.primaryDirection == "up":
            return True
        elif newDirection == "left" and self.lastDirection == "right":
            return True
        elif newDirection == "right" and self.lastDirection == "left":
            return True
        elif newDirection == "up" and self.lastDirection == "down":
            return True
        elif newDirection == "down" and self.lastDirection == "up":
            return True
        return False

    def isEqualDirection(self, key, newDirection):
        if newDirection == "left" and self.lastDirection == "left":
            return True
        elif newDirection == "right" and self.lastDirection == "right":
            return True
        elif newDirection == "up" and self.lastDirection == "up":
            return True
        elif newDirection == "down" and self.lastDirection == "down":
            return True
        return False

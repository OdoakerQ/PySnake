import pygame
from snake_head import SnakeHead
from snake_body import SnakeBody
import settings
import display as disply
import time
import randomizer as rand
from keyboard_handler import KeyboardHandler
from time import time

def main():
    pygame.init()
    options = settings.Settings()
    screen = pygame.display.set_mode(options.display_size)
    display = disply.Display(options)
    randomizer = rand.Randomizer(options)
    pygame.display.set_caption("PySnake")
    spawn_x, spawn_y = randomizer.randomizeCords()
    head = SnakeHead(spawn_x, spawn_y, "left", options)
    head_cords = head.getBackHead()
    body = SnakeBody(head_cords, "left", options)

    running = True
    while running:
        screen.fill(options.background_color)
        head.move()
        body.move(screen, head)
        objects = [head, body]
        display.show(screen, objects)

        start_time = time()
        keayboard_handler = KeyboardHandler(head.direction)
        while time() - start_time < options.time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    else:
                        keayboard_handler.handleKey(event, screen, head, body, display, options)



if __name__ == "__main__":
    main()

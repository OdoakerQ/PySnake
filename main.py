import pygame
from snake_head import SnakeHead
from snake_body import SnakeBody
import settings
import time
from keyboard_handler import KeyboardHandler
from time import time

def main():
    pygame.init()
    options = settings.Settings()
    screen = pygame.display.set_mode(options.display_size)
    head = SnakeHead(500, 400, "left", options)
    head_cords = head.getBackHead()
    body = SnakeBody(head_cords, "left")
    pygame.display.set_caption("PySnake")

    running = True


    while running:
        screen.fill(options.background_color)
        head.move()
        head.blit(screen)
        body.move(screen, head, options.speed)
        body.blit(screen)
        pygame.display.update()
        pygame.display.flip()


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
                        print(event.key)
                        keayboard_handler.handleKey(event, screen, head, body, options)



if __name__ == "__main__":
    main()

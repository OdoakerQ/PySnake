import pygame
from snake_head import SnakeHead
from snake_body import SnakeBody
from boosters import Boosters
from fruit import Fruit
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
    spawn_x, spawn_y = randomizer.randomizeDefaultCords()
    spawn_direction = randomizer.randomizeDirection()
    head = SnakeHead(spawn_x, spawn_y, spawn_direction, options)
    body = SnakeBody(head.getBackHead(), spawn_direction, options)
    boosters = Boosters(options)
    object_elements = [head]
    for belly in body.bellies: object_elements.append(belly)
    spawn_x, spawn_y = randomizer.randomizeFruitCords(object_elements)
    fruit = Fruit(spawn_x, spawn_y, options)
    boosters.add(fruit)
    objects = [head, body, boosters]
    display.show(screen, objects)

    running = True
    while running:
        screen.fill(options.background_color)
        head.move()
        display.show(screen, objects)
        body.move(head)
        objects = [head, body, boosters]
        is_fruit_colison = fruit.checkIfCollision(head)
        if is_fruit_colison:
            body.enlarge()
            boosters.elements.remove(fruit)
            spawn_x, spawn_y = randomizer.randomizeFruitCords(object_elements)
            fruit = Fruit(spawn_x, spawn_y, options)
            boosters.add(fruit)
            is_fruit_colison = False

        display.show(screen, objects)

        start_time = time()
        keyboard_handler = KeyboardHandler(head.direction)
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
                        keyboard_handler.handleKey(event, screen, head, body.getHeadBelly(), display, options)
                        display.show(screen, [head, body, boosters])


if __name__ == "__main__":
    main()

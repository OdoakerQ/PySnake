import os

class Settings():
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.time = 0.01
        self.display_size = [1023, 683]
        self.fruit_size = [22, 15]
        self.fruit_distance = 110
        self.square_side = 20
        self.speed = 5
        self.background_color = (255, 255, 255)
        self.spawn_min_x = 100
        self.spawn_max_x = 900
        self.spawn_min_y = 100
        self.spawn_max_y = 550
        self.spawn_start = 23

        self.belly_number = int(self.square_side / self.speed)
        self.belly_width = self.speed

import os

class Settings():
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.time = 3
        self.display_size = [1023, 683]
        self.bellyWidth = 22
        self.speed = 5
        self.background_color = (255, 255, 255)
        self.spawn_min_x = 100
        self.spawn_max_x = 900
        self.spawn_min_y = 100
        self.spawn_max_y = 550
        self.spawn_start = 23

        self.part_number = int(self.bellyWidth / self.speed)
        self.part_width = self.speed

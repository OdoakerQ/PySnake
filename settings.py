import os

class Settings():
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.speed = 1
        self.time = 1
        self.display_size = [1000, 800]
        self.background_color = (38, 139, 6)
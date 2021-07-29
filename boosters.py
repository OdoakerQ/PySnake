
class Boosters:
    def __init__(self, options):
        self.options = options
        self.elements = list()

    def add(self, element):
        self.elements.append(element)

    def blit(self, screen):
        for element in self.elements:
            element.blit(screen)

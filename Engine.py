import pygame

class Engine(object):
    def __init__(self):
        self.frames_per_second = 60
        self.clock = pygame.time.Clock()
        self.delta_time = 0

    def get_delta_time(self):
        return self.clock.tick(self.frames_per_second)
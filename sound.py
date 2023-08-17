import pygame

class Sound:

    def __init__(self, path) -> None:
        self.path = path
        self.sound = pygame.mixer.Sound(self.path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)
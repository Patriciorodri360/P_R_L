import random
import pygame

from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp:
    def __init__(self, image: pygame.Surface):
        self.type = power_up_type
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.rendint(100, 150)


    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x <= self.rect.width:
            self.power_ups.pop()

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
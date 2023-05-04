import random
import pygame
from dino_runner.components.power_ups.hammer import Hammer

from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups: list[PowerUp] = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if not self.power_ups and self.when_appears == score:
            self.when_appears += random.randint(300, 400)
            self.power_ups.append(Shield())

    def generate_hammer(self, score):
        if not self.power_ups and self.when_appears == score:
            self.when_appears += random.randint(300, 400)
            self.power_ups.append(Hammer())

    def update(self, game_speed, score, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if power_up.rect.colliderect(player.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up)
                self.power_ups.remove(power_up)
                break

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
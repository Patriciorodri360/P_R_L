import random

from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class Cactus(Obstacle):
    CACTUS_TYPES = [
        (SMALL_CACTUS, 325),
        (LARGE_CACTUS, 300)
    ]

    def __init__(self):
        images, pos_y = random.choice(self.CACTUS_TYPES)
        cactus_image = random.choice(images)
        super().__init__(cactus_image)
        self.rect.y = pos_y
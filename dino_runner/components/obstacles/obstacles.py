from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < - self.rect.width:
            obstacles.pop()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score

from dino_runner.utils.constants import BG, DINO_START, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS, RESET
from dino_runner.components.obstacles.obstacleManager import ObstacleManager
from dino_runner.utils.text import draw_message


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.death_count = 0
        self.power_up_manager = PowerUpManager()
        self.hammer = Hammer()

    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.quit()

    def play(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset()
        self.score.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.playing = True
        self.game_speed = 20
        self.obstacle_manager.reset()
        self.score.reset()
        self.power_up_manager.reset()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed() 
        self.player.update(user_input)
        self.obstacle_manager.update(
            self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.hammer.update(self.game_speed, [self.hammer])
        self.power_up_manager.update(
            self.game_speed, self.score.score, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player.draw_power_up(self.screen)
        self.hammer.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        print("BOOM")
        is_invencible = self.player.type == SHIELD_TYPE
        if not is_invencible:
            pygame.time.delay(500)
            self.playing = False
            self.death_count += 1

    def show_menu(self):
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        self.screen.fill((255, 255, 255))
        if self.death_count == 0:
            draw_message("Press any key to restart", self.screen)
            self.screen.blit(DINO_START, (center_x - 49, center_y - 121))
        else:
            draw_message("Press any key to restart", self.screen)
            draw_message(
                f"Your Score: {self.score.score}",
                self.screen,
                pos_x_center=center_y + 250,
                pos_y_center=center_y + 200
            )
            draw_message(
                f"Death Count: {self.death_count}",
                self.screen,
                pos_y_center=center_y + 100 
            )
            self.screen.blit(RESET, (center_x - 38, center_y - 121))
            
        pygame.display.update()
        self.handle_menu_events()
    
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()


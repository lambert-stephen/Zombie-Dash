import pygame
from menu import *

import player

class Game():
    def __init__(self, playerInfo):
        # pygame.init()
        pygame.mixer.quit()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = 'Chopsic-K6Dp.ttf'
        self.BLACK, self.WHITE = (0,0,0), (255, 255, 255)
        # Able to reference main menu object
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.watch = WatchVideoMenu(self)
        # Allows current menu to change
        self.curr_menu = self.main_menu
        # self.energy_level = 100
        self.energy_decrease = 10
        self.clock = pygame.time.Clock()
        self.exit = False

        self.playerInfo = player.Player(playerInfo)

        self.energyx, self.energyy = 175, 25

    def display_energy(self):
        pygame.draw.rect(self.display, (255, 0, 0), (12, 50, 200, 20))
        pygame.draw.rect(self.display, (0, 255, 0), (12, 50, 200 - (2 * (100 - self.playerInfo.energy_level)), 20))
        self.draw_text("Energy Left: " + str(self.playerInfo.energy_level), 30, self.playerInfo.energyx, self.playerInfo.energyy)
        # pygame.draw.rect(self.display, (255, 0, 0), (12, 50, 200, 20))
        # pygame.draw.rect(self.display, (0, 255, 0), (12, 50, 200 - (2 * (100 - self.energy_level)), 20))
        # self.draw_text("Energy Left: " + str(self.energy_level), 30, self.energyx, self.energyy)

    # Check our key input
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self.running, self.playing = False, False
                # # Stops the current menu from running
                self.curr_menu.run_display = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def game_loop(self):
        while self.playing and self.playerInfo.energy_level >= self.energy_decrease:
            self.check_events()
            if self.START_KEY:
                self.playing = False
                self.playerInfo.energy_level -= self.energy_decrease
            #self.display.blit(bg, (0,0))
            self.draw_text('Gameplay', 30, self.DISPLAY_W/2, self.DISPLAY_H / 2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
            self.clock.tick(30)

    # Draws our text
    def draw_text(self, text, size, x, y):

        font = pygame.font.Font(self.font_name, size)
        # Rectangular image to place our text
        text_surface = font.render(text, True, self.WHITE)
        # Get rectangle
        text_rect = text_surface.get_rect()
        # Centers text in rectangle
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)





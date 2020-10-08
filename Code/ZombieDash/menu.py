import pygame

#Adding a background image
bg = pygame.image.load("zombies.jpg")

class Menu():
    def __init__(self, game):
        # Reference to game object to access methods and variables
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H / 2
        self.run_display = True
        # Cursor to traverse the menu
        self.cursor_rect = pygame.Rect(0,0,20,20)
        # Places cursor to left of text
        self.offset = - 150;

    # Draws cursor
    def draw_cursor(self):
        self.game.draw_text("->", 15, self.cursor_rect.x, self.cursor_rect.y)

    # Blits menu to the screen
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        self.game.display.blit(bg, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

# Inherit values from our base class Menu
class MainMenu(Menu):
    def __init__(self, game):
        # Gets all variables from Menu class
        Menu.__init__(self, game)
        self.energyx, self.energyy = 175, 25
        self.state = "Join Match"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70
        self.watchx, self.watchy = self.mid_w, self.mid_h + 110
        # Aligns cursor with start
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    # Displays menu
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            # Sets logic for our cursor
            self.game.check_events()
            self.check_input()
            pygame.draw.rect(self.game.display, (255,0,0), (12, 50, 200, 20))
            pygame.draw.rect(self.game.display, (0,255,0), (12, 50, 200 - (2 * (100 - self.game.energy_level)), 20))
            self.game.draw_text("Energy Left: " + str(self.game.energy_level), 30, self.energyx, self.energyy)
            self.game.draw_text("Zombie Dash", 30, self.game.DISPLAY_W /2, self.game.DISPLAY_H/2 - 70)
            # Sets text at specified positions
            self.game.draw_text("Join Match", 30, self.startx, self.starty)
            self.game.draw_text("Options", 30, self.optionsx, self.optionsy)
            self.game.draw_text("Watch Video", 30, self.watchx, self.watchy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Join Match":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.watchx + self.offset, self.watchy)
                self.state = "Watch Video"
            elif self.state == "Watch Video":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Join Match"

        elif self.game.UP_KEY:
            if self.state == "Join Match":
                self.cursor_rect.midtop = (self.watchx + self.offset, self.watchy)
                self.state = "Watch Video"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Join Match"
            elif self.state == "Watch Video":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Options"

    def check_input(self):
        # Check to see if player moves cursor
        self.move_cursor()
        # If player hits start on Join Match, game loop begins
        if self.game.START_KEY:
            if self.state == "Join Match":
                self.game.playing = True
            elif self.state == "Options":
                self.game.curr_menu = self.game.options
            elif self.state == "Watch Video":
                self.game.curr_menu = self.game.watch
            print(self.state)
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h + 30
        self.brightnessx, self.brightnessy = self.mid_w, self.mid_h + 70
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 110
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.draw_text("Options", 30, self.game.DISPLAY_W /2, self.game.DISPLAY_H / 2 - 70)
            self.game.draw_text("Volume", 25, self.volx, self.voly)
            self.game.draw_text("Brightness", 25, self.brightnessx, self.brightnessy)
            self.game.draw_text("Controls", 25, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        self.move_cursor()

        # If backspace is pressed, return to the main menu and stop the current display
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        # START_KEY TO: DO IN MENU (VOLUME + BRIGHTNESS)
        elif self.game.START_KEY:
            pass

    # Moves cursor down the menu options
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Volume":
                self.cursor_rect.midtop = (self.brightnessx + self.offset, self.brightnessy)
                self.state = "Brightness"
            elif self.state == "Brightness":
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = "Controls"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.state = "Volume"

        elif self.game.UP_KEY:
            if self.state == "Volume":
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = "Controls"
            elif self.state == "Brightness":
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.state = "Volume"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.brightnessx + self.offset, self.brightnessy)
                self.state = "Brightness"


class WatchVideoMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Watch Video"

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()

            # Returns back to the main menu
            if self.game.BACK_KEY or self.game.START_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

                # If energy level is already at 100, don't increment
                if self.game.energy_level >= 100:
                    pass

                # If energy level is greater than 0 and less than or equal to 98, increment
                elif self.game.energy_level >= 0 and self.game.energy_level <= 98:
                    self.game.energy_level += 2;

            # Draw to Watch Video Screen
            self.game.draw_text("Watch Video", 30, self.mid_w, self.mid_h)
            self.blit_screen()





import pygame
import player


def draw_text(text, size, x, y, display):
    font = pygame.font.Font('Chopsic-K6Dp.ttf', size)
    # Rectangular image to place our text
    text_surface = font.render(text, True, (255, 255, 255))
    # Get rectangle
    text_rect = text_surface.get_rect()
    # Centers text in rectangle
    text_rect.center = (x, y)
    display.blit(text_surface, text_rect)

def mainMenu(game_display, p):

    bg = pygame.image.load("zombiebg.jpg")
    #Blit the text
    game_display.blit(bg, (0, 0))

    #Set font
    title = pygame.font.Font("PopulationZeroBB.ttf", 70)
    play_title = pygame.font.Font("PopulationZeroBB.ttf", 25)
    multiplayer_title = pygame.font.Font("PopulationZeroBB.ttf", 25)
    shop_title = pygame.font.Font("PopulationZeroBB.ttf", 25)
    options_title = pygame.font.Font("PopulationZeroBB.ttf", 25)
    quit_title = pygame.font.Font("PopulationZeroBB.ttf", 25)
    font = pygame.font.Font('Chopsic-K6Dp.ttf', 30)

    playerInfo = p

    clock = pygame.time.Clock()

    play_pressed = False

    while not play_pressed:


        # play button
        play_button = pygame.image.load("black_button.png")
        play_button = pygame.transform.scale(play_button, (150, 50))

        # multiplayer button
        multiplayer_button = pygame.image.load("black_button.png")
        multiplayer_button = pygame.transform.scale(multiplayer_button, (150, 50))

        # shop button
        shop_button = pygame.image.load("black_button.png")
        shop_button = pygame.transform.scale(shop_button, (150, 50))

        # options button
        options_button = pygame.image.load("black_button.png")
        options_button = pygame.transform.scale(options_button, (150, 50))

        # quit button
        quit_button = pygame.image.load("black_button.png")
        quit_button = pygame.transform.scale(quit_button, (150, 50))

        bg = pygame.image.load("zombiebg.jpg")
        # Blit the text
        game_display.blit(bg, (0, 0))

        # Render text
        title_texture = title.render("Zombie Dash", True, pygame.Color('black'))

        # Blit text
        game_display.blit(title_texture, ((400 - (title_texture.get_width() / 2)), 75))

        #listeners
        playing = game_display.blit(play_button, ((400 - (play_button.get_width() / 2)), 180))
        multiplayer = game_display.blit(multiplayer_button, ((400 - (multiplayer_button.get_width() / 2)), 260))
        shop = game_display.blit(shop_button, ((400 - (shop_button.get_width() / 2)), 340))
        options = game_display.blit(options_button, ((400 - (options_button.get_width() / 2)), 420))
        quitting = game_display.blit(quit_button, ((400 - (quit_button.get_width() / 2)), 500))

        #set the textures
        play_texture = play_title.render("Play", True, pygame.Color('black'))
        game_display.blit(play_texture, ((400 - (play_texture.get_width() / 2)), 190))

        multiplayer_texture = multiplayer_title.render("Multiplayer", True, pygame.Color('black'))
        game_display.blit(multiplayer_texture, ((400 - (multiplayer_texture.get_width() / 2)), 270))

        shop_texture = shop_title.render("Shop", True, pygame.Color('black'))
        game_display.blit(shop_texture, ((400 - (shop_texture.get_width() / 2)), 350))

        options_texture = options_title.render("Options", True, pygame.Color('black'))
        game_display.blit(options_texture, ((400 - (options_texture.get_width() / 2)), 430))

        quit_texture = quit_title.render("Exit", True, pygame.Color('black'))
        game_display.blit(quit_texture, ((400 - (quit_texture.get_width() / 2)), 510))

        pygame.draw.rect(game_display, (255, 0, 0), (12, 50, 200, 20))
        pygame.draw.rect(game_display, (0, 255, 0), (12, 50, 200 - (2 * (100 - playerInfo.energy_level)), 20))
        draw_text("Energy Left: " + str(playerInfo.energy_level), 30, playerInfo.energyx, playerInfo.energyy, game_display)

        user_surface = font.render(playerInfo.userName, True, (255, 255, 255))
        game_display.blit(user_surface, (800 - user_surface.get_width(), 7))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if playing.collidepoint(event.pos) and playerInfo.energy_level >= 10:
                    print("Time to play")
                    playerInfo.energy_level -= 10
                    return "play"

                if multiplayer.collidepoint(event.pos):
                    return "multiplayer"

                if shop.collidepoint(event.pos):
                    return "shop"

                if options.collidepoint(event.pos):
                    print("Options")
                    return "options"


                if quitting.collidepoint(event.pos):
                    print("Quitting")
                    return "quit"

        clock.tick(30)

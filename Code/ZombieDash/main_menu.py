import pygame

def mainMenu(game_display):

    bg = pygame.image.load("zombiebg.jpg")
    #Blit the text
    game_display.blit(bg, (0, 0))

    #Set font
    title = pygame.font.SysFont("The Stranger Brush.ttf", 70)
    play_title = pygame.font.SysFont("PopulationZeroBB.ttf", 55)
    multiplayer_title = pygame.font.SysFont("PopulationZeroBB.ttf", 55)
    shop_title = pygame.font.SysFont("PopulationZeroBB.ttf", 55)
    options_title = pygame.font.SysFont("PopulationZeroBB.ttf", 55)
    quit_title = pygame.font.SysFont("PopulationZeroBB.ttf", 55)


    play_pressed = False

    while not play_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if playing.collidepoint(event.pos):
                    print("Time to play")
                    # game_display.fill((0, 0, 0))
                    # return 1

                if multiplayer.collidepoint(event.pos):
                    print("Time for Multiplayer")

                if shop.collidepoint(event.pos):
                    print("Time to shop")

                if options.collidepoint(event.pos):
                    print("Options")
                    # return 1


                if quitting.collidepoint(event.pos):
                    print("Quitting")
                    # return 1



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
        game_display.blit(title_texture, ((400 - (title_texture.get_width() / 2)), 25))

        #listeners
        playing = game_display.blit(play_button, (350, 100))
        multiplayer = game_display.blit(multiplayer_button, (350, 200))
        shop = game_display.blit(shop_button, (350, 300))
        options = game_display.blit(options_button, (350, 400))
        quitting = game_display.blit(quit_button, (350, 500))

        #set the textures
        play_texture = play_title.render("Play", True, pygame.Color('black'))
        game_display.blit(play_texture, (385, 105))

        multiplayer_texture = multiplayer_title.render("Multiplayer", True, pygame.Color('black'))
        game_display.blit(multiplayer_texture, (385, 205))

        shop_texture = shop_title.render("Shop", True, pygame.Color('black'))
        game_display.blit(shop_texture, (385, 305))

        options_texture = options_title.render("Options", True, pygame.Color('black'))
        game_display.blit(options_texture, (350, 405))

        quit_texture = quit_title.render("Exit", True, pygame.Color('black'))
        game_display.blit(quit_texture, (385, 505))

        pygame.display.update()

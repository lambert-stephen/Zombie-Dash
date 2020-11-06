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

def mapSelect(game_display, p):

    bg = pygame.image.load("zombiebg.jpg")
    #Blit the text
    game_display.blit(bg, (0, 0))

    #Set font
    map1_title = pygame.font.Font("PopulationZeroBB.ttf", 25)
    map2_title = pygame.font.Font("PopulationZeroBB.ttf", 25)
    map3_title = pygame.font.Font("PopulationZeroBB.ttf", 25)
    map4_title = pygame.font.Font("PopulationZeroBB.ttf", 25)
    font = pygame.font.Font('Chopsic-K6Dp.ttf', 30)


    playerInfo = p

    clock = pygame.time.Clock()

    play_pressed = False

    while not play_pressed:


        # play button
        map1_button = pygame.image.load("black_button.png")
        map1_button = pygame.transform.scale(map1_button, (150, 50))

        # multiplayer button
        map2_button = pygame.image.load("black_button.png")
        map2_button = pygame.transform.scale(map2_button, (150, 50))

        # shop button
        map3_button = pygame.image.load("black_button.png")
        map3_button = pygame.transform.scale(map3_button, (150, 50))

        # options button
        map4_button = pygame.image.load("black_button.png")
        map4_button = pygame.transform.scale(map4_button, (150, 50))


        bg = pygame.image.load("zombiebg.jpg")
        # Blit the text
        game_display.blit(bg, (0, 0))

        #listeners
        map1 = game_display.blit(map1_button, ((400 - (map1_button.get_width() / 2)), 180))
        map2 = game_display.blit(map2_button, ((400 - (map2_button.get_width() / 2)), 260))
        map3 = game_display.blit(map3_button, ((400 - (map3_button.get_width() / 2)), 340))
        map4 = game_display.blit(map4_button, ((400 - (map4_button.get_width() / 2)), 420))

        #set the textures
        map1_texture = map1_title.render("Undead Forest", True, pygame.Color('black'))
        game_display.blit(map1_texture, ((400 - (map1_texture.get_width() / 2)), 190))

        map2_texture = map2_title.render("Zombie Zafari", True, pygame.Color('black'))
        game_display.blit(map2_texture, ((400 - (map2_texture.get_width() / 2)), 270))

        map3_texture = map3_title.render("tunnels", True, pygame.Color('black'))
        game_display.blit(map3_texture, ((400 - (map3_texture.get_width() / 2)), 350))

        map4_texture = map4_title.render("Sea World", True, pygame.Color('black'))
        game_display.blit(map4_texture, ((400 - (map4_texture.get_width() / 2)), 430))


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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "main menu"

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if map1.collidepoint(event.pos) and playerInfo.energy_level >= 10:
                    print("Time to play")
                    playerInfo.energy_level -= 10
                    return 'trial.tmx'

                if map2.collidepoint(event.pos):
                    playerInfo.energy_level -= 10
                    return "omarmap.tmx"

                if map3.collidepoint(event.pos):
                    playerInfo.energy_level -= 10
                    return "z-map.tmx"

                if map4.collidepoint(event.pos):
                    playerInfo.energy_level -= 10
                    return "untitled.tmx"

        clock.tick(30)

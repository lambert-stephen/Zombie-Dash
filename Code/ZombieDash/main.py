
import login

import pygame
import main_menu
import trial
import game
import play
import map_selection

import player


pygame.init()

pygame.mixer.music.load("zombiedashtrack.mp3");
pygame.mixer.music.play(-1);

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('Zombie Dash')

clock = pygame.time.Clock()

currentView = "main menu"

player1 = login.menu(gameDisplay)

multiplayerMenu = game.Game(player1)

currentView = main_menu.mainMenu(gameDisplay, player1)



while currentView != "quit":

    if currentView == "main menu":
        currentView = main_menu.mainMenu(gameDisplay, player1)

    if currentView == "play":
        #currentView = main_menu.mainMenu(gameDisplay, player1)

        selection = map_selection.mapSelect(gameDisplay, player1);

        if selection != 'main menu':
            #Play map music
            pygame.mixer.music.load("maptrack.mp3");
            pygame.mixer.music.play(-1);

            #Play game.
            currentView = play.gamePlay(gameDisplay, selection)

            #Play normal music
            pygame.mixer.music.load("zombiedashtrack.mp3");
            pygame.mixer.music.play(-1);
        else:
            currentView = 'main menu'

    if currentView == "multiplayer":

        multiplayerMenu.playerInfo.energy_level = player1.energy_level
        multiplayerMenu.playerInfo.userName = player1.userName

        while not multiplayerMenu.exit:
            multiplayerMenu.curr_menu.display_menu()
        multiplayerMenu.exit = False

        #Update player energy and return to maain menu.
        player1 = multiplayerMenu.playerInfo
        currentView = "main menu"

    if currentView == "shop":
        currentView = trial.shop_menu(gameDisplay, player1)

    if currentView == "main menu":
        currentView = main_menu.mainMenu(gameDisplay, player1)

    if currentView == "options":
        multiplayerMenu.curr_menu = multiplayerMenu.options

        while not multiplayerMenu.exit:
            multiplayerMenu.curr_menu.display_menu()

        multiplayerMenu.exit = False
        player1 = multiplayerMenu.playerInfo
        currentView = "main menu"
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            currentView = "quit"

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()








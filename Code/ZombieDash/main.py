
import login

import pygame
import main_menu
import trial
import game

import player


pygame.init()

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
        currentView = main_menu.mainMenu(gameDisplay, player1)

    if currentView == "multiplayer":

        while not multiplayerMenu.exit:
            multiplayerMenu.curr_menu.display_menu()
        multiplayerMenu.exit = False

        #Update player energy and return to maain menu.
        player1 = multiplayerMenu.playerInfo
        currentView = "main menu"

    if currentView == "shop":
        currentView = trial.shop_menu(gameDisplay)

    if currentView == "main menu":
        currentView = main_menu.mainMenu(gameDisplay, player1)

    if currentView == "options":
        multiplayerMenu.options.display_menu()
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            currentView = "quit"

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()








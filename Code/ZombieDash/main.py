
import login

import pygame
import main_menu


pygame.init()

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('Zombie Dash')

clock = pygame.time.Clock()

dead = False

x = login.menu(gameDisplay)
i = main_menu.mainMenu(gameDisplay)
while not dead:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()








# import pygame, time
# from gui_lib import Button
#
# #initialize the game
# pygame.init()
#
# #create a window for the game
# window= pygame.display.set_mode((800,600))
# #myfont=pygame.font.SysFont("Arial", 60)
# #label=myfont.render("hello pygame",1,(255,255,0))
# #window.blit(label, (100,100))
#
# #background image variable
# background_image= pygame.image.load('background_store.jpg')
# button_image= pygame.image.load('logout.png')
#
# # Define and create button
# button = Button(button_image, (10,500), "exit")
#
# dead = False
# while not dead:
#     window.fill((0,0,0))
#     window.blit(background_image,(0,0))
#     window.blit(button.image, button.rect)
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             dead = True
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             button.on_click(event)
#
#

import pygame
from gui_lib import Button


def shop_menu(display, p):

    clock = pygame.time.Clock()

    # create a window of game
    screen = display
    # icon load
    man = pygame.image.load('man.png')
    mansmall = pygame.image.load('mansmall.png')
    girl = pygame.image.load('girl.png')
    girlsmall = pygame.image.load('girlsmall.png')
    background = pygame.image.load('background.jpg')
    logout = pygame.image.load('logout.png')
    shirt = pygame.image.load('shirt.png')
    tshirt = pygame.image.load('tshirt.png')
    ttshirt = pygame.image.load('ttshirt.png')
    trousers = pygame.image.load('trousers.png')
    trouserssub1 = pygame.image.load('trouserssub1.png')
    trouserssub2 = pygame.image.load('trouserssub2.png')
    gun = pygame.image.load('gun.png')
    hunter = pygame.image.load('hunter.png')
    rifle = pygame.image.load('rifle.png')
    energy = pygame.image.load('energy.png')
    energy = pygame.transform.scale(energy, (37, 37))

    font = pygame.font.Font('Chopsic-K6Dp.ttf', 30)

    player_info = p

    submenu = False;
    #pygame.display.set_icon(logout)

    # Define and create button
    button = Button(logout, (750, 50), callback=False)
    button1 = Button(shirt, (50, 50), callback=False)
    button11 = Button(tshirt, (20, 50), callback=False)
    button12 = Button(ttshirt, (20, 50), callback=False)
    button2 = Button(trousers, (100, 50), callback=False)
    button21 = Button(trouserssub1, (40, 50), callback=False)
    button22 = Button(trouserssub2, (80, 90), callback=False)
    button3 = Button(gun, (150, 50), callback=False)
    button31 = Button(hunter, (60, 50), callback=False)
    button32 = Button(rifle, (60, 50), callback=False)
    button4 = Button(man, (20, 60), callback=False)
    button41 = Button(mansmall, (50, 300), callback=False)
    button5 = Button(girl, (300, 60), callback=False)
    button55 = Button(girlsmall, (50, 300), callback=False)
    running = True



    energy_button = Button(energy, (200, 50), callback=False)

    #hitman purchase box

    if p.purchased[1]:
        item_box1 = pygame.image.load("purchased.png")
    else:
        item_box1 = pygame.image.load("notpurchased.png")

    item_box1 = pygame.transform.scale(item_box1, (100, 125))

    if p.purchased[4]:
        item_box2 = pygame.image.load("purchased.png")
    else:
        item_box2 = pygame.image.load("notpurchased.png")

    item_box2 = pygame.transform.scale(item_box2, (100, 125))

    if p.purchased[2]:
        item_box3 = pygame.image.load("purchased.png")
    else:
        item_box3 = pygame.image.load("notpurchased.png")

    item_box3 = pygame.transform.scale(item_box3, (100, 125))

    if p.purchased[6]:
        item_box4 = pygame.image.load("purchased.png")
    else:
        item_box4 = pygame.image.load("notpurchased.png")

    item_box4 = pygame.transform.scale(item_box4, (100, 125))

    if p.purchased[3]:
        item_box5 = pygame.image.load("purchased.png")
    else:
        item_box5 = pygame.image.load("notpurchased.png")

    item_box5 = pygame.transform.scale(item_box5, (100, 125))

    if p.purchased[5]:
        item_box6 = pygame.image.load("purchased.png")
    else:
        item_box6 = pygame.image.load("notpurchased.png")

    item_box6 = pygame.transform.scale(item_box6, (100, 125))



    # while not (button4.callback or button5.callback):
    #     screen.fill((255, 255, 255))
    #     screen.blit(button4.image, button4.rect)
    #     screen.blit(button5.image, button5.rect)
    #     pygame.display.update()
    #
    #     clock.tick(30)
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running=False
    #         elif event.type ==  pygame.MOUSEBUTTONDOWN :
    #             button4.on_click(event)
    #             button5.on_click(event)


    while running:



        screen.fill((255, 0, 0))
        screen.blit(background, (0, 0))

        hitman_listener = display.blit(item_box1, ((400 - (item_box1.get_width() / 2)), 200))
        hitman = pygame.image.load('hitman1_gun.png')
        display.blit(hitman, ((400 - (hitman.get_width() / 2)), 238))

        robot_listener = display.blit(item_box2, ((400 - (item_box2.get_width() / 2)), 350))
        robot = pygame.image.load('robot1_gun.png')
        display.blit(robot, ((400 - (robot.get_width() / 2)), 388))


        oldman_listener = display.blit(item_box3, ((200 - (item_box3.get_width() / 2)), 200))
        oldman = pygame.image.load('manOld_gun.png')
        display.blit(oldman, ((200 - (oldman.get_width() / 2)), 238))

        survivor_listener = display.blit(item_box4, ((200 - (item_box4.get_width() / 2)), 350))
        survivor = pygame.image.load('survivor1_gun.png')
        display.blit(survivor, ((200 - (survivor.get_width() / 2)), 388))

        manbrown_listener = display.blit(item_box5, ((600 - (item_box5.get_width() / 2)), 200))
        manbrown = pygame.image.load('manBrown_gun.png')
        display.blit(manbrown, ((600 - (manbrown.get_width() / 2)), 238))

        solider_listener = display.blit(item_box6, ((600 - (item_box6.get_width() / 2)), 350))
        soldier = pygame.image.load('soldier1_gun.png')
        display.blit(soldier, ((600 - (soldier.get_width() / 2)), 388))


        #hitmanCollide = screen.blit(hitmanButton.image, hitmanButton.rect)
        # if hitmanButton.callback :
        #       print('m a hitman')


        if button4.callback :
            screen.blit(button41.image, button41.rect)
        if button5.callback :
            screen.blit(button55.image, button55.rect)
        screen.blit(button.image, button.rect)
        screen.blit(button1.image, button1.rect)

        if button1.callback:
            item1 = screen.blit(tshirt, ((53, 110)))
            item2 = screen.blit(ttshirt, ((53, 150)))

        screen.blit(button2.image, button2.rect)
        if button2.callback :
              item3 = screen.blit(trouserssub1, ((103,110)))
              item4 =screen.blit(trouserssub2, ((103,150)))

        screen.blit(button3.image, button3.rect)
        if button3.callback :
              item5 = screen.blit(rifle, ((153,110)))
              item6 = screen.blit(hunter, ((153,150)))

        energy_listener = screen.blit(energy_button.image, energy_button.rect)


        if button.callback:
            return "main menu"

        money_surface = font.render(str(player_info.money)+"$", True, (255, 255, 255))
        screen.blit(money_surface, (800 - money_surface.get_width(), 600- money_surface.get_height()))

        energy_surface = font.render("Energy: " + str(player_info.energy_level), True, (255, 255, 255))
        screen.blit(energy_surface, (800 - energy_surface.get_width(), 600 - money_surface.get_height() - money_surface.get_height()))


        pygame.display.update()

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            elif event.type ==  pygame.MOUSEBUTTONDOWN :
                button.on_click(event)
                button1.on_click(event)
                button2.on_click(event)
                button3.on_click(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.callback:
                    item1 = screen.blit(tshirt, ((53, 110)))
                    item2 = screen.blit(ttshirt, ((53, 150)))
                    print('shirts')

                    if item1.collidepoint(event.pos):
                        player_info.money -= 10
                    if item2.collidepoint(event.pos):
                        player_info.money -= 10


                if button2.callback:
                    item3 = screen.blit(trouserssub1, ((103, 110)))
                    item4 = screen.blit(trouserssub2, ((103, 150)))

                    if item3.collidepoint(event.pos):
                        player_info.money -= 10
                    if item4.collidepoint(event.pos):
                        player_info.money -= 10

                if button3.callback:
                    item5 = screen.blit(rifle, ((153, 110)))
                    item6 = screen.blit(hunter, ((153, 150)))

                    if item5.collidepoint(event.pos):
                        player_info.money -= 10
                    if item6.collidepoint(event.pos):
                        player_info.money -= 10

                if energy_listener.collidepoint(event.pos):
                    player_info.energy_level +=30
                    if player_info.energy_level > 100:
                        player_info.energy_level = 100
                    player_info.money -= 25

                if hitman_listener.collidepoint(event.pos):
                    p.current_character = 1

                    if not p.purchased[1]:
                        p.purchased[1] = True
                        player_info.money -= 100
                        item_box1 = pygame.image.load("purchased.png")
                        item_box1 = pygame.transform.scale(item_box1, (100, 125))

                if oldman_listener.collidepoint(event.pos):
                    p.current_character = 2

                    if not p.purchased[2]:
                        p.purchased[2] = True
                        player_info.money -= 100
                        item_box3 = pygame.image.load("purchased.png")
                        item_box3 = pygame.transform.scale(item_box3, (100, 125))

                if manbrown_listener.collidepoint(event.pos):
                    p.current_character = 3

                    if not p.purchased[3]:
                        p.purchased[3] = True
                        player_info.money -= 100
                        item_box5 = pygame.image.load("purchased.png")
                        item_box5 = pygame.transform.scale(item_box5, (100, 125))

                if robot_listener.collidepoint(event.pos):
                    p.current_character = 4

                    if not p.purchased[4]:
                        p.purchased[4] = True
                        player_info.money -= 100
                        item_box2 = pygame.image.load("purchased.png")
                        item_box2 = pygame.transform.scale(item_box2, (100, 125))

                if solider_listener.collidepoint(event.pos):
                    p.current_character = 5

                    if not p.purchased[5]:
                        p.purchased[5] = True
                        player_info.money -= 100
                        item_box6 = pygame.image.load("purchased.png")
                        item_box6 = pygame.transform.scale(item_box6, (100, 125))

                if survivor_listener.collidepoint(event.pos):
                    p.current_character = 6

                    if not p.purchased[6]:
                        p.purchased[6] = True
                        player_info.money -= 100
                        item_box4 = pygame.image.load("purchased.png")
                        item_box4 = pygame.transform.scale(item_box4, (100, 125))






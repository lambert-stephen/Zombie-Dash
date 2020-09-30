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

#pygame initialize
pygame.init()
#create a window of game
screen=pygame.display.set_mode((800,600))
#icon load
background=pygame.image.load('background.jpg')
logout= pygame.image.load('logout.png')
shirt=pygame.image.load('shirt.png')
tshirt=pygame.image.load('tshirt.png')
ttshirt=pygame.image.load('ttshirt.png')
trousers=pygame.image.load('trousers.png')
trouserssub1=pygame.image.load('trouserssub1.png')
trouserssub2=pygame.image.load('trouserssub2.png')
gun=pygame.image.load('gun.png')
hunter=pygame.image.load('hunter.png')
rifle=pygame.image.load('rifle.png')


submenu=False;
pygame.display.set_icon(logout)

# Define and create button
button = Button(logout, (750,50), callback=False)
button1 = Button(shirt, (50,50), callback=False)
button11 = Button(tshirt, (20,50), callback=False)
button12 = Button(ttshirt, (20,50), callback=False)
button2 = Button(trousers, (100,50), callback=False)
button21 = Button(trouserssub1, (40,50), callback=False)
button22 = Button(trouserssub2, (80,90), callback=False)
button3 = Button(gun, (150,50), callback=False)
button31 = Button(hunter, (60,50), callback=False)
button32 = Button(rifle, (60,50), callback=False)


# In event loop. Under pygame.MOUSEBUTTONDOWN.
#button.on_click(pygame.MOUSEBUTTONDOWN)
running=True
while running:
    screen.fill((255, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(button.image, button.rect)
    screen.blit(button1.image, button1.rect)
    if button1.callback :
          screen.blit(tshirt, ((53,110)))
          screen.blit(ttshirt, ((53,150)))

    screen.blit(button2.image, button2.rect)
    if button2.callback :
          screen.blit(trouserssub1, ((103,110)))
          screen.blit(trouserssub2, ((103,150)))

    screen.blit(button3.image, button3.rect)
    if button3.callback :
          screen.blit(rifle, ((153,110)))
          screen.blit(hunter, ((153,150)))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type ==  pygame.MOUSEBUTTONDOWN :
            button1.on_click(event)
            button2.on_click(event)
            button3.on_click(event)










import pygame



def menu(display):

    bg = pygame.image.load("zombiecity.jpg")

    display.blit(bg, (0, 0))

    #Boxes for typing username/pass
    username_box = pygame.Rect(325, 225, 200, 32)
    password_box = pygame.Rect(325, 300, 200, 32)

    #For storing username/pass
    user_name = ""
    password = ""

    #User Prompts
    user_prompt = "Username:"
    pass_prompt = "password:"

    #Fonts for the gui.
    welcome_font = pygame.font.Font("The Stranger Brush.ttf", 70)
    prompt_font = pygame.font.Font("The Stranger Brush.ttf", 40)
    game_font = pygame.font.Font(None, 32)

    #To know when a text box is active.
    user_name_active = False
    password_active = False


    login = False


    while not login:

        for event in pygame.event.get():

            #If exitting app.
            if event.type == pygame.QUIT:
                pygame.quit()

            #If user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:

                #Check if username box clicked
                if username_box.collidepoint(event.pos):
                    user_name_active = True
                else:
                    user_name_active = False

                #Check is password bo clicked.
                if password_box.collidepoint(event.pos):
                    password_active = True
                else:
                    password_active = False

                if login_listener.collidepoint(event.pos):
                    #Try logging in
                    #If succcesful return to main game.
                    display.fill((0, 0, 0))
                    print("login")
                    return 1

                if register_listener.collidepoint(event.pos):
                    #Make an account on the server
                    print ("Registered")

            #If user pressed a key.
            if event.type == pygame.KEYDOWN:

                #If user is typing username.
                if user_name_active:
                    if event.key == pygame.K_RETURN:
                        print(user_name)
                    elif event.key == pygame.K_BACKSPACE:
                        print("backspace")
                        user_name = user_name[:-1]
                    else:
                        print("text")
                        user_name += event.unicode
                #If user is typing password.
                if password_active:
                    if event.key == pygame.K_RETURN:
                        print(user_name)
                    elif event.key == pygame.K_BACKSPACE:
                        print("backspace")
                        password = password[:-1]
                    else:
                        print("text")
                        password += event.unicode


        google_login = pygame.image.load('ggl_icon.png')
        google_login = pygame.transform.scale(google_login, (80, 80))

        fb_login = image = pygame.image.load("fb_icon.png")
        fb_login = pygame.transform.scale(fb_login, (80, 80))

        log_in_button = pygame.image.load("gray_button.png")
        log_in_button = pygame.transform.scale(log_in_button, (150, 50))

        sign_up_button = pygame.image.load("gray_button.png")
        sign_up_button = pygame.transform.scale(log_in_button, (150, 50))

        bg = pygame.image.load("zombiecity.jpg")

        display.blit(bg, (0, 0))

        surface = game_font.render(user_name, True, pygame.Color('black'))
        surface2 = game_font.render(password, True, pygame.Color('black'))
        title_surface = welcome_font.render("Zombie Dash", True, pygame.Color('Red'))

        user_prompt_surf = prompt_font.render(user_prompt, True, pygame.Color('Red'))
        password_prompt_surf = prompt_font.render(pass_prompt, True, pygame.Color('Red'))

        display.blit(user_prompt_surf, ((username_box.x -5 - user_prompt_surf.get_width()), 220))
        display.blit(password_prompt_surf, ((username_box.x - 5 - password_prompt_surf.get_width()), 295))

        # Display a dodge blue Text box, width 2
        pygame.draw.rect(display, pygame.Color('gray'), username_box, 0)
        pygame.draw.rect(display, pygame.Color('gray'), password_box, 0)

        # Blit the text.
        display.blit(surface, (username_box.x + 5, username_box.y + 5))
        display.blit(surface2, (password_box.x + 5, password_box.y + 5))
        display.blit(title_surface, ((400 - (title_surface.get_width() /2)), 50))


        display.blit(google_login, (400 - google_login.get_width(), 400))
        display.blit(fb_login, (400 , 400))

        register_listener = display.blit(sign_up_button, (400 - 10 - (log_in_button.get_width() ), 350))
        login_listener = display.blit(log_in_button, (400 + 10, 350))

        login_surface = game_font.render("Login", True, pygame.Color('black'))
        display.blit(login_surface, (455, 360))

        register_surface = game_font.render("Register", True, pygame.Color('black'))
        display.blit(register_surface, (275, 360))

        pygame.display.flip()

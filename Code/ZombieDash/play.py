import pygame
import pygame as pg
import sys
from os import path
from tilemap import *
from random import uniform, choice
vec = pg.math.Vector2
import events
import random


def gamePlay(display, chosen_map, p):

    alive = True

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    finish = pygame.sprite.Group()
    zombies = pygame.sprite.Group()
    shotgun_ammo = pygame.sprite.Group()
    machine_gun_ammo = pygame.sprite.Group()
    zombie_gun_fire = pygame.sprite.Group()
    medkits = pygame.sprite.Group()
    consumables = pygame.sprite.Group()
    gun_fire = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    ZOMBIE_IMGS = ['zombie1_hold.png', 'zombie1_hold.png', 'zombie1_hold.png', 'zombie1_hold.png', 'zombie1_gun.png', 'zombie1_machine.png', 'zombie1_silencer.png']
    ZOMBIE_SPEEDS = [150, 100, 75, 125, 200]
    ZOMBIE_BULLET_RATE = [1000, 1300, 800]

    CHARACTER_IMGGS = [['manBlue_gun.png', 'manBlue_machine.png', 'manBlue_shotgun.png'], ['hitman1_gun.png', 'hitman1_machine.png', 'hitman1_shotgun.png'],
                       ['manOld_gun.png', 'manOld_machine.png', 'manOld_shotgun.png'], ['manBrown_gun.png', 'manBrown_machine.png', 'manBrown_shotgun.png'],
                       ['robot1_gun.png', 'robot1_machine.png', 'robot1_shotgun.png'], ['soldier1_gun.png', 'soldier1_machine.png', 'soldier1_shotgun.png'],
                       ['survivor1_gun.png', 'survivor1_machine.png', 'survivor1_shotgun.png']]

    class sharedClock():
        def __init__(self, c):
            self.clock = c
            self.clk = 0

        def tick(self):
            self.clk = self.clock.tick(60) / 1000.0;

        def get_tick(self):
            return self.clk

    #A shared frame rate clock among all rendering sprites.
    clock = pygame.time.Clock()
    shared_clock = sharedClock(clock)
    shared_clock.tick()

    # Shotgun Ammo Drops
    class Medkit(pygame.sprite.Sprite):
        def __init__(self, x, y):
            self.current_position = vec(x, y)

            # Set sprite group
            self.groups = consumables, medkits

            # initialize parent values
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.image = pygame.image.load(
                path.join(path.join(path.dirname(__file__), 'img'),
                          'medkit.png')).convert_alpha()

            # Create hit box
            self.rect = self.image.get_rect()
            self.hit_rect = pygame.Rect(0, 0, 35, 35)
            self.hit_rect.center = self.rect.center

        def update(self):
            # Get current position
            self.rect = self.image.get_rect()
            self.rect.center = self.current_position

            # Update hit box location and check for collisions.
            self.hit_rect.centerx = self.current_position.x
            self.hit_rect.centery = self.current_position.y
            self.rect.center = self.hit_rect.center

    # Shotgun Ammo Drops
    class MachinegunAmmo(pygame.sprite.Sprite):
        def __init__(self, x, y):
            self.current_position = vec(x, y)

            # Set sprite group
            self.groups = consumables, machine_gun_ammo

            # initialize parent values
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.image = pygame.image.load(
                path.join(path.join(path.dirname(__file__), 'img'),
                          'machine_gun_ammo.png')).convert_alpha()

            # Create hit box
            self.rect = self.image.get_rect()
            self.hit_rect = pygame.Rect(0, 0, 35, 35)
            self.hit_rect.center = self.rect.center

        def update(self):
            # Get current position
            self.rect = self.image.get_rect()
            self.rect.center = self.current_position

            # Update hit box location and check for collisions.
            self.hit_rect.centerx = self.current_position.x
            self.hit_rect.centery = self.current_position.y
            self.rect.center = self.hit_rect.center

    # Shotgun Ammo Drops
    class ShotgunAmmo(pygame.sprite.Sprite):
        def __init__(self, x, y):

            self.current_position = vec(x, y)

            # Set sprite group
            self.groups = consumables, shotgun_ammo

            # initialize parent values
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.image = pygame.image.load(
                path.join(path.join(path.dirname(__file__), 'img'),
                          'shotgun_shells.png')).convert_alpha()

            # Create hit box
            self.rect = self.image.get_rect()
            self.hit_rect = pygame.Rect(0, 0, 35, 35)
            self.hit_rect.center = self.rect.center

        def update(self):
            # Get current possition
            self.rect = self.image.get_rect()
            self.rect.center = self.current_position

            # Update hit box location and check for collisions.
            self.hit_rect.centerx = self.current_position.x
            self.hit_rect.centery = self.current_position.y
            self.rect.center = self.hit_rect.center


    # Player Sprite
    class PlayerSprite(pygame.sprite.Sprite):
        def __init__(self, c,  x, y):

            # Set sprite group
            self.groups = all_sprites

            #index for current character
            self.cur_character = p.current_character

            #Index for current weapon
            self.cur_weapon = 0

            # initialize parent values
            pygame.sprite.Sprite.__init__(self, self.groups)

            # Get images of player sprite.
            self.cur_character_images = CHARACTER_IMGGS[self.cur_character]


            self.update_img()

            # Create hit box
            self.rect = self.image.get_rect()
            self.hit_rect = pygame.Rect(0, 0, 35, 35)
            self.hit_rect.center = self.rect.center

            self.movement = vec(0, 0)
            self.current_position = vec(x, y)

            self.current_direction = 0
            self.last_shot = 0
            self.health = 100
            self.clock = c

            self.machine_gun_ammo = 50;
            self.shotgun_ammo = 10;

        def update_img(self):
            self.image = pygame.image.load(
                path.join(path.join(path.dirname(__file__), 'img'),
                          self.cur_character_images[self.cur_weapon])).convert_alpha()
            self.stock_image = pygame.image.load(
                path.join(path.join(path.dirname(__file__), 'img'),
                          self.cur_character_images[self.cur_weapon])).convert_alpha()

        def update(self):

            self.update_img()

            # For keeping track degrees of character rotation
            self.rotationation = 0

            # Vector for storing player movement
            self.movement = vec(0, 0)

            # Get the keys being presssed at the moment
            keys = pygame.key.get_pressed()

            # Rotate right or left
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.rotationation = 200
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.rotationation = -200
            # Move up or down
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.movement = vec(200, 0).rotate(-self.current_direction)
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.movement = vec(-200 / 2, 0).rotate(-self.current_direction)
            # Shoot bullets
            if keys[pygame.K_SPACE]:
                now = pygame.time.get_ticks()

                #Pistol
                if(self.cur_weapon == 0):
                    if now - self.last_shot > 400:
                        self.last_shot = now
                        direction = vec(1, 0).rotate(-self.current_direction)
                        position = self.current_position + vec(30, 10).rotate(-self.current_direction)
                        GunFire(self.clock, position, direction)
                #Machine gun
                elif (self.cur_weapon == 1 and self.machine_gun_ammo > 0):
                    if now - self.last_shot > 100:
                        self.machine_gun_ammo = self.machine_gun_ammo -1
                        self.last_shot = now
                        direction = vec(1, 0).rotate(-self.current_direction)
                        position = self.current_position + vec(30, 10).rotate(-self.current_direction)
                        GunFire(self.clock, position, direction)
                #Shotgun
                elif (self.cur_weapon == 2 and self.shotgun_ammo > 0):
                    if now - self.last_shot > 600:
                        self.shotgun_ammo = self.shotgun_ammo -1
                        self.last_shot = now
                        direction = vec(1, 0).rotate(-self.current_direction)
                        position = self.current_position + vec(30, 10).rotate(-self.current_direction)
                        direction2 = vec(1, 0).rotate(-self.current_direction + 5)
                        direction3 = vec(1, 0).rotate(-self.current_direction - 5)
                        direction4 = vec(1, 0).rotate(-self.current_direction + 10)
                        direction5 = vec(1, 0).rotate(-self.current_direction - 10)
                        GunFire(self.clock, position, direction)
                        GunFire(self.clock, position, direction2)
                        GunFire(self.clock, position, direction3)
                        GunFire(self.clock, position, direction4)
                        GunFire(self.clock, position, direction5)


            # Calculate the current direction of player
            self.current_direction = (self.current_direction + self.rotationation * self.clock.get_tick()) % 360

            # Rotate image accordingly
            self.image = pygame.transform.rotate(self.stock_image, self.current_direction)

            # Get current possition
            self.rect = self.image.get_rect()
            self.rect.center = self.current_position

            # Add the new movement to the current possition
            self.current_position += self.movement * self.clock.get_tick()  # self.game.dt

            # Update hit box location and check for collisions.
            self.hit_rect.centerx = self.current_position.x
            events.check_wall_collisions(self, walls, 'x')
            self.hit_rect.centery = self.current_position.y
            events.check_wall_collisions(self, walls, 'y')
            self.rect.center = self.hit_rect.center

    #Load and get map file.
    map = TiledMap(path.join(path.dirname(__file__), 'maps/' + chosen_map))

    #initilaize map
    map_img = map.make_map()

    #Setup current view of map
    camera = Camera(map.width, map.height)

    #Add sprites to map
    for object in map.tmxdata.objects:
        if object.name == 'player':
            player = PlayerSprite(shared_clock, object.x, object.y)
        if object.name == 'wall':
            events.Wall(walls, object.x, object.y,
                     object.width, object.height)
        if object.name == 'finish':
            events.Finish(finish, object.x, object.y,
                   object.width, object.height)
        if object.name == 'shotgun':
            ShotgunAmmo(object.x, object.y)
        if object.name == 'machinegun':
            MachinegunAmmo(object.x, object.y)
        if object.name == 'medkit':
            Medkit(object.x, object.y)
        if object.name == 'zombie':

            #Zombie sprite class
            class Zombie(pygame.sprite.Sprite):
                def __init__(self, c, x, y):
                    self.groups = all_sprites, zombies
                    pygame.sprite.Sprite.__init__(self, self.groups)

                    #Get the kind of zombie
                    imageName = choice(ZOMBIE_IMGS)
                    self.imageString = imageName

                    # Get images of zombie sprite.
                    self.image = pygame.image.load(
                        path.join(path.join(path.dirname(__file__), 'img'), imageName)).convert_alpha()
                    self.stock_image = pygame.image.load(
                        path.join(path.join(path.dirname(__file__), 'img'), imageName)).convert_alpha()

                    #When last shot gun
                    self.last_shot = 0


                    self.rect = self.image.get_rect()
                    self.hit_rect = pg.Rect(0, 0, 30, 30)
                    self.hit_rect.center = self.rect.center
                    self.current_position = vec(x, y)
                    self.movement = vec(0, 0)
                    self.acc = vec(0, 0)
                    self.rect.center = self.current_position
                    self.rotation = 0
                    self.health = 30
                    self.speed = choice(ZOMBIE_SPEEDS)
                    self.active = True;
                    self.rate = choice(ZOMBIE_BULLET_RATE)
                    self.clock = c
                    self.got_shot = False

                def spread_zombies(self):
                    for zombie in zombies:
                        if zombie != self:
                            dist = self.current_position - zombie.current_position
                            if 0 < dist.length() < 50:
                                self.acc += dist.normalize()

                def update(self):


                    if self.active or self.got_shot:

                        #Rotate image to player
                        self.rotation = (player.current_position - self.current_position).angle_to(vec(1, 0))
                        self.image = pygame.transform.rotate(self.stock_image, self.rotation)
                        self.rect = self.image.get_rect()
                        self.rect.center = self.current_position

                        #Move towards player
                        self.acc = vec(1, 0).rotate(-self.rotation)
                        self.spread_zombies()
                        self.acc.scale_to_length(self.speed)
                        self.acc += self.movement * -1
                        self.movement += self.acc * self.clock.get_tick()
                        self.current_position += self.movement * self.clock.get_tick() + 0.5 * self.acc * self.clock.get_tick() ** 2

                        #Check for wall collisons
                        self.hit_rect.centerx = self.current_position.x
                        events.check_wall_collisions(self, walls, 'x')
                        self.hit_rect.centery = self.current_position.y
                        events.check_wall_collisions(self, walls, 'y')
                        self.rect.center = self.hit_rect.center

                        now = pygame.time.get_ticks()

                        #Shoot Gun Fire accoring to gun rate.
                        if (now - self.last_shot > self.rate) and self.imageString != 'zombie1_hold.png':
                            self.last_shot = now
                            dir = vec(1, 0).rotate(-self.rotation)
                            pos = self.current_position + vec(30, 10).rotate(-self.rotation)
                            ZombieGunfire(self.clock, pos, dir)
                            # self.vel = vec(-KICKBACK, 0).rotate(-self.rotation)

                    #Kill sprite at 0 health
                    if self.health <= 0:

                        luck = random.randint(0, 4)

                        if luck == 0:
                            what = random.randint(0, 2)

                            if what == 0:
                                MachinegunAmmo(self.current_position.x, self.current_position.y)
                            elif what == 1:
                                ShotgunAmmo(self.current_position.x, self.current_position.y)
                            elif what == 2:
                                Medkit(self.current_position.x, self.current_position.y)


                        self.kill()

                    #Activate zombie if close enough
                    #Deactivate if walked far enough
                    dist = self.current_position - player.current_position

                    if dist.length() < 300:
                        self.active = True;
                    elif dist.length() > 350:
                        self.active = False;

            Zombie(shared_clock, object.x, object.y)

    class GunFire(pygame.sprite.Sprite):
        def __init__(self, c, position, direction):
            self.groups = all_sprites, gun_fire
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.image = pygame.image.load(
                path.join(path.join(path.dirname(__file__), 'img'), 'bullet.png')).convert_alpha()
            self.rect = self.image.get_rect()


            self.current_position = vec(position)
            self.rect.center = position

            self.movement = direction * 500

            self.spawn_time = pygame.time.get_ticks()

            self.clock = c

        def update(self):
            self.current_position += self.movement * self.clock.get_tick()
            self.rect.center = self.current_position
            if pygame.sprite.spritecollideany(self, walls):
                self.kill()
            if pygame.time.get_ticks() - self.spawn_time > 800:
                self.kill()

            hits = pygame.sprite.spritecollide(self, zombies, False)
            for hit in hits:
                hit.health -= 10
                print('hit')
                hit.vel = vec(0, 0)
                hit.got_shot = True
                self.kill()

    class ZombieGunfire(pygame.sprite.Sprite):
        def __init__(self, c, position, direction):
            self.groups = all_sprites, zombie_gun_fire
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.image = pygame.image.load(
                path.join(path.join(path.dirname(__file__), 'img'), 'bullet.png')).convert_alpha()
            self.rect = self.image.get_rect()

            self.current_position = vec(position)
            self.rect.center = position

            self.movement = direction * 500

            self.spawn_time = pygame.time.get_ticks()

            self.clock = c

        # For bullets
        def update(self):
            self.current_position += self.movement * self.clock.get_tick()
            self.rect.center = self.current_position
            if pygame.sprite.spritecollideany(self, walls):
                self.kill()
            if pygame.time.get_ticks() - self.spawn_time > 700:
                self.kill()

            hits = pygame.sprite.spritecollide(player, zombie_gun_fire, False, collide_hit_rect)
            for hit in hits:
                self.kill()
                player.health -= 2.5
                hit.vel = vec(0, 0)

    def display_health(game_display):
        pygame.draw.rect(game_display, (255, 0, 0), (12, 10, 200, 20))
        pygame.draw.rect(game_display, (0, 255, 0), (12, 10, 200 - (2 * (100 - player.health)), 20))

    def display_timer(game_display, time):
        font = pygame.font.Font('Chopsic-K6Dp.ttf', 30)
        user_surface = font.render(time, True, (255, 255, 255))
        game_display.blit(user_surface, (400 - (user_surface.get_width()/2), 7))

    def display_weapon_info(game_display):

        if player.cur_weapon == 0:
            ammo = "AMMO: INF"
            weapon = "PISTOL"
        elif player.cur_weapon == 1:
            ammo = "AMMO: " + str(player.machine_gun_ammo)
            weapon = 'MACHINE GUN'
        elif player.cur_weapon == 2:
            weapon = "SHOTGUN"
            ammo = "AMMO: " + str(player.shotgun_ammo)



        font = pygame.font.Font('Chopsic-K6Dp.ttf', 25)
        user_surface = font.render(weapon, True, (255, 255, 255))
        game_display.blit(user_surface, (800 -  user_surface.get_width() - 10, 7))

        font = pygame.font.Font('Chopsic-K6Dp.ttf', 18)
        user_surface = font.render(ammo, True, (255, 255, 255))
        game_display.blit(user_surface, (680, 30))

    start_ticks = pygame.time.get_ticks()  # starter tick


    while alive:



        shared_clock.tick()

        # Update camera
        camera.update(player)

        #Update sprites

        all_sprites.update()
        consumables.update()


        #Render map and camera
        display.blit(map_img, camera.apply_rect(map_img.get_rect()))


        for sprite in consumables:
            display.blit(sprite.image, camera.apply(sprite))

        for sprite in all_sprites:
            display.blit(sprite.image, camera.apply(sprite))



        #Check for zombie + player collisions.
        hits = pygame.sprite.spritecollide(player, zombies, False, collide_hit_rect)
        for hit in hits:
            player.health -= 2.5
            hit.vel = vec(0, 0)
            if player.health <= 0:
                alive = False

        #If he was hit, knockback player
        if hits:
            player.current_position += vec(20, 0).rotate(-hits[0].rotation)

        #Check for zombie + gunfire collisions
        # shot_zombies = pygame.sprite.groupcollide(zombies, gun_fire, False, True)
        # for shot_zombie in shot_zombies:
        #     hits = pygame.sprite.spritecollide(shot_zombie, gun_fire, False, collide_hit_rect)
        #     for hit in hits:
        #         print('hit')
        #         hit.got_shot = True
        #         #hit.health -= 10
        #         # hit.vel = vec(0, 0)

        #Check to see if player has reached finish line.
        hits = pg.sprite.spritecollide(player, finish, False, collide_hit_rect)
        if hits:
            alive = False;

        # Check to see if player has reached finish line.
        hits = pg.sprite.spritecollide(player, shotgun_ammo, False, collide_hit_rect)
        for hit in hits:
            hit.kill()
            player.shotgun_ammo +=10

        # Check to see if player has reached finish line.
        hits = pg.sprite.spritecollide(player, machine_gun_ammo, False, collide_hit_rect)
        for hit in hits:
            hit.kill()
            player.machine_gun_ammo += 30

        # Check to see if player has reached finish line.
        hits = pg.sprite.spritecollide(player, medkits, False, collide_hit_rect)
        for hit in hits:
            if player.health != 100:
                hit.kill()
                player.health = 100



        #display the players health.
        display_health(display)

        display_weapon_info(display)


        time_left = 300 - int((pygame.time.get_ticks() - start_ticks) / 1000)

        if(time_left != 0):
            display_timer(display, str(time_left))
        else:
            alive = False;

        #Update display
        pygame.display.flip()

        #Check for key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "main menu"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    player.cur_weapon = (player.cur_weapon+1) % 3
                    player.update_img()
                    print('lshift')


    return "main menu"






#Wall Sprite
import pygame

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

#Sprite class for walls
class Wall(pygame.sprite.Sprite):
        def __init__(self, group, x, y, w, h):
            self.groups = group
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.rect = pygame.Rect(x, y, w, h)
            self.hit_rect = self.rect
            self.x = x
            self.y = y
            self.rect.x = x
            self.rect.y = y

 #Sprite for finish line
class Finish(pygame.sprite.Sprite):
    def __init__(self, group, x, y, w, h):
        self.groups = group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect = pygame.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

def check_wall_collisions(sprite, group, axis):
    if axis == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.current_position.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.current_position.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.movement.x = 0
            sprite.hit_rect.centerx = sprite.current_position.x
    if axis == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.current_position.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.current_position.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.movement.y = 0
            sprite.hit_rect.centery = sprite.current_position.y

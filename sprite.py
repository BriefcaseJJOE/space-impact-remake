import sys, pygame
from typing import Any


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.cooldown = 0
        self.image = pygame.image.load("assets/player1.png")
        self.resize =  pygame.transform.scale(self.image,(100,50))
        self.rect = self.resize.get_rect()
        self.rect.centerx = 75
        self.rect.centery = 300
        self.speedy = 0
        self.speedx= 0
    

    def update(self):
        self.cooldown -= 1
        self.speedx = 0
        self.speedy = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speedx = -4
        if key_state[pygame.K_RIGHT]:
            self.speedx = + 4
        if key_state[pygame.K_UP]:
            self.speedy = - 4
        if key_state[pygame.K_DOWN]:
            self.speedy = + 4 
        self.rect.x += self.speedx
        self.rect.y += self.speedy    
        if self.cooldown == 0:
            self.cooldown = 20  
        

        
        

        

  
class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.resize = pygame.transform.scale(self.image,(5,5))
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = self.resize.get_rect()
        self.rect.center = (x,y)
        
    def update(self):
        self.rect.centerx += 10
        if self.rect.x > 1050:
            self.kill()
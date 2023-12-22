import sys, pygame
from typing import Any
import random

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
        #player boundaries
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 900:
            self.rect.x = 900
        if self.rect.y > 550:
            self.rect.y = 550
        if self.rect.y < 0:
            self.rect.y = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.cooldown = 0
        self.image = pygame.image.load("assets/enemy.png")
        self.resize =  pygame.transform.scale(self.image,(1,1))
        self.rect = self.resize.get_rect()
        self.rect.centerx = 1100
        self.rect.centery = random.randint(200,600)
      
    def update(self):
        self.rect.x -= 1
        #if pygame.sprite.spritecollide(Enemy,Bullets,False):
        #    self.kill()
        if self.rect.x < 0:
            self.kill()
        

        

  
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

        

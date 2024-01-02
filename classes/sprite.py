import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 3
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
            self.speedx = - 2
        if key_state[pygame.K_RIGHT]:
            self.speedx = + 2
        if key_state[pygame.K_UP]:
            self.speedy = - 2
        if key_state[pygame.K_DOWN]:
            self.speedy = + 2 
        self.rect.x += self.speedx
        self.rect.y += self.speedy    
        # player boundaries
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 900:
            self.rect.x = 900
        if self.rect.y > 550:
            self.rect.y = 550
        if self.rect.y < 70:
            self.rect.y = 70
        # death condition
        if self.lives == 0:
            self.kill()
            

        
    def reset(self):
        self.lives -= 1
        self.rect.centerx = 75
        self.rect.centery = 300


class Enemy(pygame.sprite.Sprite):
    def __init__(self, live:int ):
        pygame.sprite.Sprite.__init__(self)
        self.live = live
        self.cooldown = 0
        self.image = pygame.image.load("assets/enemy.png")
        #self.resize =  pygame.transform.scale(self.image,(1,1))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1050
        self.rect.centery = random.randint(100,500)
        self.spawn_point = self.rect.centery 
        self.spawn_point_upper = self.rect.centery
        self.spawn_point_lower = self.rect.centery + 100
        self.spawn_point_upper_1 = self.rect.centery +200 
        
       
    def update(self):
        self.rect.x -= 3
        
        if self.spawn_point_upper < self.spawn_point_lower:
            self.rect.y +=1

            self.spawn_point_upper +=1
        #spawn_point_upper = 400 spawn_point_lower = 400
        if self.spawn_point_upper == self.spawn_point_lower and self.spawn_point < self.spawn_point_upper_1:
            self.rect.y -=1
            self.spawn_point_upper_1 -=2

        if self.spawn_point_upper == self.spawn_point_lower and self.spawn_point == self.spawn_point_upper_1:
            self.spawn_point_upper = self.spawn_point
            self.spawn_point_upper_1 = self.rect.centery +200 
        #spawn 300
        #lower = 350
        
       
        if self.rect.x < 0:
            self.kill()
        if self.live == 0:
            self.kill()

        

  
class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #self.speed = 10
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.resize = pygame.transform.scale(self.image,(5,5))
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    

    def update(self):
        self.rect.centerx += 5
        if self.rect.x > 1050:
            self.kill()

        
class Power_up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/power_up.png").convert_alpha()
        self.resize = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.centery = random.randint(100,400)
        self.rect.centerx = 1050
    
    def update(self):
        self.rect.x -= 2
        if self.rect.x < 0:
            self.kill()

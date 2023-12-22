import sprite as s

import sys, pygame

pygame.init()
screen = pygame.display.set_mode((1000,600))

#setting frame rate cap tp run stabily
clock = pygame.time.Clock()

#setting screen title
pygame.display.set_caption("Space Impact Remake")


def game():
    #BACKGROUND
    bgx = -1000

    second_bgx = 0
    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(1000,600))
    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(1000,600))

    #sprites
    all_sprite = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_sprite = pygame.sprite.Group()
    player = s.Player()
    all_sprite.add(player)
    enemy = s.Enemy()
    enemy_sprite.add(enemy)
    #controls
    cooldown = 0
    shoot = False
    
    #bullet = s.Bullets(s.Player.rect.centerx,s.Player.rect.centery)
    run = True
    
    while run:
        # for every event check that if user click on cross of the screen
        #then quit the game
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()

            #event handler 
            #KEY DOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot = True
                    
            #KEY UP        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    shoot = False

            if shoot:
                if cooldown ==0:
                    bullet_group.add(s.Bullets(player.rect.centerx+45,player.rect.centery+2))
                    cooldown = 5
                else:
                    cooldown -= 1
                
       
        #background logic
        bgx += 0.5
        second_bgx +=0.5

        if bgx > -1:
            bgx = -1000
        if second_bgx > 1000:
            second_bgx = 0

        
        
        


        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        
        bullet_group.draw(screen)
        bullet_group.update()
        enemy_sprite.draw(screen)
        enemy_sprite.update()
        all_sprite.draw(screen)
        all_sprite.update()
        # constanly update gameboard 
       

        pygame.display.update()
    
        





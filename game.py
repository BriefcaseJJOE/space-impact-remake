import sprite as s

import sys, pygame

pygame.init()
screen = pygame.display.set_mode((1000,600))

#setting frame rate cap tp run stabily
clock = pygame.time.Clock()

#setting screen title
pygame.display.set_caption("Space Impact Remake")

#BACKGROUND
def game():
    #BACKGROUND
    bgx = -1000

    second_bgx = 0
    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(1000,600))
    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(1000,600))

    #player sprite
    all_sprite = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    player = s.Player()
    
    all_sprite.add(player)
    #controls
    shoot = False
    
    #bullet = s.Bullets(s.Player.rect.centerx,s.Player.rect.centery)
    
    
    while True:
        # for every event check that if user click on cross of the screen
        #then quit the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
        
        
        #background logic
        bgx += 0.5
        second_bgx +=0.5

        if bgx > -1:
            bgx = -1000
        if second_bgx > 1000:
            second_bgx = 0

        
        # display 
        if shoot:
            bullet = s.Bullets(player.rect.centerx,player.rect.centery)
            bullet_group.add(bullet)
             
        if pygame.key.get_pressed()[pygame.K_SPACE]:
                shoot = True
                
        
        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        
        bullet_group.draw(screen)
        bullet_group.update()
        all_sprite.draw(screen)
        all_sprite.update()
        
        # constanly update gameboard 
       
        pygame.display.update()
    
        clock.tick(60)




if __name__ == '__main__':
    game()
import pygame
import button as b
import sprite as s
from config import SCREEN_WIDTH , SCREEN_HEIGHT
import time
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


def main_menu():
    pygame.display.set_caption("Main Menu")
    # Title
    test_font = pygame.font.Font("freesansbold.ttf",70)
    text_surface = test_font.render("Space Impact Remake",False,"white")

    # Buttons
    credit_button = pygame.image.load("assets/chest.png")
    credit_button = pygame.transform.scale(credit_button,(100 ,100))

    play_button = pygame.image.load('assets/play.png')
    play_button = pygame.transform.scale(play_button,(250 ,100))

    quit_button = pygame.image.load('assets/quit.png')
    quit_button = pygame.transform.scale(quit_button,(250 ,100))
   
    cbutton = b.Button(credit_button,200,400)
    pbutton = b.Button(play_button,SCREEN_WIDTH/2 , 400)
    qbutton = b.Button(quit_button,SCREEN_WIDTH/2 , 520)

    # BACKGROUND|
    bgx = -SCREEN_WIDTH
    
    second_bgx = 0

    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

    # MENU LOOP
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if pbutton.checkforinput():
                game()
            if qbutton.checkforinput():
                pygame.QUIT()
            if cbutton.checkforinput():
                credit()

        bgx += 0.1
        second_bgx +=0.1

        if bgx > -1:
            bgx = -SCREEN_WIDTH
        if second_bgx > SCREEN_WIDTH:
            second_bgx = 0

        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        screen.blit(text_surface,(150,50))

        cbutton.update()
        qbutton.update()      
        pbutton.update()
        pygame.display.update()

def credit():
    pygame.display.set_caption("Credits")
    
    test_font = pygame.font.Font(None,100)
    text_surface = test_font.render("Made by:Irwin lai",False,"white")
    asset_surface = test_font.render("Assets by:Zai ndn",False,"white")
     
    back_button = pygame.image.load("assets/back.png")
    back_button = pygame.transform.scale(back_button,(100 ,100))

    bbutton = b.Button(back_button,70,50)

    bgx = -SCREEN_WIDTH
    
    second_bgx = 0

    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if bbutton.checkforinput():
                main_menu()
            

        bgx += 0.1
        second_bgx +=0.1

        if bgx > -1:
            bgx = -SCREEN_WIDTH
        if second_bgx > SCREEN_WIDTH:
            second_bgx = 0
        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        screen.blit(text_surface,(200,250))
        screen.blit(asset_surface,(190,350))  
        bbutton.update()
        
        pygame.display.update()

def gameover():
    pygame.display.set_caption("Credits")
    
    test_font = pygame.font.Font(None,100)
    text_surface = test_font.render("Game Over",False,"white")
     
    back_button = pygame.image.load("assets/back.png")
    back_button = pygame.transform.scale(back_button,(100 ,100))

    bbutton = b.Button(back_button,70,50)

    bgx = -SCREEN_WIDTH
    
    second_bgx = 0

    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if bbutton.checkforinput():
                main_menu()
            

        bgx += 0.1
        second_bgx +=0.1

        if bgx > -1:
            bgx = -SCREEN_WIDTH
        if second_bgx > SCREEN_WIDTH:
            second_bgx = 0
        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        screen.blit(text_surface,(300,250))  
        bbutton.update()
        
        pygame.display.update()

def game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # setting frame rate cap tp run stabily
    clock = pygame.time.Clock()
    
    # setting screen title
    pygame.display.set_caption("Space Impact Remake")

    # BACKGROUND
    bgx = -SCREEN_WIDTH

    second_bgx = 0
    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

    # sprites
    all_sprite_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_sprite_group = pygame.sprite.Group()

    player = s.Player()
    
   
    
    all_sprite_group.add(player)
    # controls
    cooldown = 0
    shoot = False
    
    spawn = 100
    total_enemy = 0

    t0 = time.time()
    timeout_seconds = 30    
    while player.alive():
        # for every event check that if user click on cross of the screen
        # then quit the game
        if time.time()-t0 > timeout_seconds:
            break
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()

            # event handler 
            # KEY DOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot = True
                    
            # KEY UP        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    shoot = False

            if shoot:
                if cooldown == 0:
                    bullet_group.add(s.Bullets(player.rect.centerx+45,player.rect.centery+2))
                    cooldown = 5
                else:
                    cooldown -= 1
        # enemy spawn
        if spawn == 0 and total_enemy <= 10:
            enemy_sprite_group.add(s.Enemy())
            spawn = 100 
            total_enemy += 1
        spawn -= 1                          
        
        # collsion 
        
        
        for bullet in bullet_group:
            collided_enemies_list = pygame.sprite.spritecollide(bullet,enemy_sprite_group,True)

            # if bullet hit any enemies in the enemy_sprite_group collided_enemies_list will increase in len
            if len(collided_enemies_list) > 0 :
                bullet.kill()
       
        
         
            
        if pygame.sprite.spritecollide(player,enemy_sprite_group,False):
            player.reset()  
        

        # background logic
        bgx += 0.5
        second_bgx +=0.5

        if bgx > -1:
            bgx = -SCREEN_WIDTH
        if second_bgx > SCREEN_WIDTH:
            second_bgx = 0                    

        
        
        
        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        
        bullet_group.draw(screen)
        bullet_group.update()
        enemy_sprite_group.draw(screen)
        enemy_sprite_group.update()
        all_sprite_group.draw(screen)
        all_sprite_group.update()
        # constanly update gameboard 
       
        pygame.display.update()
    gameover()

if __name__=="__main__":

    main_menu()


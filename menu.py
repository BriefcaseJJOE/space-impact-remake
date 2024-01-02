import pygame
import classes.button as b
import classes.sprite as s
import classes.text as t
from config import SCREEN_WIDTH , SCREEN_HEIGHT , BACKGROUND_IMAGE_FILE_PATH , BACK_BUTTON_IMAGE_FILE_PATH
import time
from classes.background import Background
from classes.gui import gui
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# BACKGROUND|
background = Background(
    image_file_path = BACKGROUND_IMAGE_FILE_PATH, 
    screen_width = SCREEN_WIDTH,
    screen_height = SCREEN_HEIGHT,
    screen_initial_x = 0 
)
second_background = Background(
    image_file_path = BACKGROUND_IMAGE_FILE_PATH, 
    screen_width = SCREEN_WIDTH,
    screen_height = SCREEN_HEIGHT,
    screen_initial_x = -SCREEN_WIDTH
)

# BUTTONS
back_button = b.Button(
    image_file_path = "assets/back.png", 
    image_x_pos=30, 
    image_y_pos=30,
    scale_height=50,
    scale_width=50
)

play_button = b.Button(
    image_file_path = 'assets/play.png',
    image_x_pos = SCREEN_WIDTH/2,
    image_y_pos = 400,
    scale_height = 100,
    scale_width = 200
)

credit_button = b.Button(
    image_file_path = 'assets/chest.png',
    image_x_pos = 200,
    image_y_pos = 400
)

quit_button = b.Button(
    image_file_path = 'assets/quit.png',
    image_x_pos = SCREEN_WIDTH/2,
    image_y_pos = 520,
    scale_height = 100,
    scale_width = 200
)
# GUI
hp_gui = gui("assets/hp.png")
rocket_gui = gui('assets/power.png')

def main_menu():
    pygame.display.set_caption("Main Menu")
    # Title
    title_text = t.text("Space Impact Remake","white")

  
    # MENU LOOP
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if play_button.checkforinput():
                game()
            if quit_button.checkforinput():
                pygame.QUIT()
            if credit_button.checkforinput():
                credit()

        
        background.update(screen)
        second_background.update(screen)        
        title_text.update(screen,150,100)

        credit_button.update(screen)
        quit_button.update(screen)      
        play_button.update(screen)
        pygame.display.update()


def credit():
    pygame.display.set_caption("Credits")
    
    creator_text = t.text("Made by:Irwin lai","white")
    asset_text = t.text("Assets by:Zai ndn","white")
     
  
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if back_button.checkforinput():
                main_menu()
            

        
        background.update(screen)
        second_background.update(screen)     
        creator_text.update(screen,200,250)
        asset_text.update(screen,190,350)  
        back_button.update(screen)
        
        pygame.display.update()

def gameover():
    pygame.display.set_caption("Gamer over")
    
    game_over_text = t.text("Game Over", "white")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if back_button.checkforinput():
                main_menu()
            
        
        background.update(screen)
        second_background.update(screen)     
        game_over_text.update(screen,300,250)  
        back_button.update(screen)
        
        pygame.display.update()

def game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # setting frame rate cap tp run stabily
    clock = pygame.time.Clock()
    
    # setting screen title
    pygame.display.set_caption("Space Impact Remake")

    

    # all text
    power_up_text = 2
    score = 0
    score_text = t.text(f"Score:{score}","white", 70)
    rocket_text = t.text(f":{power_up_text}","white", 70)
    
    # sprites
    all_sprite_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_sprite_group = pygame.sprite.Group()
    power_up_group = pygame.sprite.Group()
    power_shot_group = pygame.sprite.Group()
   
    player = s.Player()
    all_sprite_group.add(player)
    
    # controls
    cooldown = 0
    shoot = False
    power_shot = False
    power_up_timer = 100
    spawn_timer = 100
    total_enemy = 1

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    power_shot = True

            # KEY UP        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    shoot = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_x:
                    power_shot = False

            if power_shot:
                if power_up_text > 0:
                    power_shot_group.add(s.Power_shot(player.rect.centerx+45,player.rect.centery+2))
                    power_up_text -= 1
                    rocket_text = t.text(f":{power_up_text}","white", 70)

            if shoot:
                if cooldown == 0:
                    bullet_group.add(s.Bullets(player.rect.centerx+45,player.rect.centery+2))
                    cooldown = 3
                else:
                    cooldown -= 1
       
        # spawn timer
        if spawn_timer == 0 and total_enemy <= 100:
            enemy_sprite_group.add(s.Enemy(1))
            spawn_timer = 100
            total_enemy += 1

        if power_up_timer == 0 :
            power_up_group.add(s.Power_up())
            power_up_timer = 100
            

        spawn_timer -= 1                          
        power_up_timer -= 1
       
        
        # collsion 
        for bullet in bullet_group:
            collided_enemies_list = pygame.sprite.spritecollide(bullet,enemy_sprite_group,True)

            # if bullet hit any enemies in the enemy_sprite_group collided_enemies_list will increase in len
            if len(collided_enemies_list) > 0 :
                score += 10
                score_text = t.text(f"Score: {score}","white", 70)
                bullet.kill()

        for rocket in power_shot_group:
            rocket_collided_enemies_list = pygame.sprite.spritecollide(rocket,enemy_sprite_group,True)

            # if bullet hit any enemies in the enemy_sprite_group collided_enemies_list will increase in len
            if len(rocket_collided_enemies_list) > 0 :
                score += 10
                score_text = t.text(f"Score: {score}","white", 70)
                rocket.kill()

        if pygame.sprite.spritecollide(player,power_up_group,True):
            power_up_text += 1
            rocket_text = t.text(f":{power_up_text}","white", 70)
         
         
        if pygame.sprite.spritecollide(player,enemy_sprite_group,False):
            player.reset()  
        

        # drawing and updating screen
        background.update(screen,0.5)
        second_background.update(screen,0.5)     

        hp_gui.update(screen,20,20,player.lives)
        rocket_gui.update(screen,400,20,1)

        bullet_group.draw(screen)
        bullet_group.update()

        enemy_sprite_group.draw(screen)
        enemy_sprite_group.update()

        power_up_group.draw(screen)
        power_up_group.update()

        power_shot_group.draw(screen)
        power_shot_group.update()

        all_sprite_group.draw(screen)
        all_sprite_group.update()

        score_text.update(screen,650,20)
        rocket_text.update(screen,450,20)

        # constanly update gameboard 
       
        pygame.display.update()
    gameover()

if __name__=="__main__":

    main_menu()


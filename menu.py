import pygame
import button as b
import game 
pygame.init()
screen = pygame.display.set_mode((1000,600))


def main_menu():
    pygame.display.set_caption("Main Menu")
    #Title
    test_font = pygame.font.Font(None,100)
    text_surface = test_font.render("Space Impact Remake",False,"white")

    #Buttons
    credit_button = pygame.image.load("assets/chest.png")
    credit_button = pygame.transform.scale(credit_button,(100 ,100))

    play_button = pygame.image.load('assets/play.png')
    play_button = pygame.transform.scale(play_button,(250 ,100))

    quit_button = pygame.image.load('assets/quit.png')
    quit_button = pygame.transform.scale(quit_button,(250 ,100))

    cbutton = b.Button(credit_button,200,400)
    pbutton = b.Button(play_button,1000/2 , 400)
    qbutton = b.Button(quit_button,1000/2 , 520)

    #BACKGROUND
    bgx = -1000
    
    second_bgx = 0

    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(1000,600))

    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(1000,600))

    #MENU LOOP
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if pbutton.checkforinput():
                game.game()
            if qbutton.checkforinput():
                pygame.QUIT()
            if cbutton.checkforinput():
                credit()

        bgx += 0.1
        second_bgx +=0.1

        if bgx > -1:
            bgx = -1000
        if second_bgx > 1000:
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
    text_surface = test_font.render("made by:Irwin lai",False,"white")
     
    back_button = pygame.image.load("assets/back.png")
    back_button = pygame.transform.scale(back_button,(100 ,100))

    bbutton = b.Button(back_button,70,50)

    bgx = -1000
    
    second_bgx = 0

    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(1000,600))

    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(1000,600))
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
            bgx = -1000
        if second_bgx > 1000:
            second_bgx = 0
        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        screen.blit(text_surface,(200,300))
        bbutton.update()
        
        pygame.display.update()

if __name__ == '__main__':
    main_menu()
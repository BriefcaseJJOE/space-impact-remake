import pygame
import sys




class Button():
    def __init__(self, image_file_path:str , image_x_pos:int, image_y_pos:int, scale_height:None=100, scale_width:None=100):
        self.button = pygame.image.load(image_file_path)
        self.button = pygame.transform.scale(self.button,(scale_width, scale_height))
        self.image_x_pos = image_x_pos
        self.image_y_pos = image_y_pos
        self.rect = self.button.get_rect(center=(self.image_x_pos,self.image_y_pos))
        
        
        
        
    def update(self,screen:pygame.Surface):
        screen.blit(self.button,self.rect)
        
    def checkforinput(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False 
        return action
    


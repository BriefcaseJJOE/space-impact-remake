import pygame




class Background:
    def __init__(self,image_file_path:str, screen_width:int, screen_height:int, screen_initial_x:int):
        self.bg = pygame.image.load(image_file_path)
        self.bg = pygame.transform.scale(self.bg, (screen_width,screen_height))
        self.screen_width = screen_width
        self.screen_initial_x = screen_initial_x
        self.bgx = screen_initial_x
        

    def update(self,screen:pygame.Surface, shift_per_tick:float = 0.1):

        self.bgx += shift_per_tick
        # if my initial x move more than screen width reset back to original x 
        if self.bgx  >= self.screen_initial_x + self.screen_width:
            self.bgx = self.screen_initial_x
        screen.blit(self.bg, (self.bgx, 0))
           
        
        
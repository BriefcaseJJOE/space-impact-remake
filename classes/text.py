import pygame

class text():
    def __init__(self,  text:str, color:str, font_size:int = 100) -> None:
        self.text_font = pygame.font.Font(None,font_size)
        self.text_surface = self.text_font.render(text, True, color)

    def update(self, screen, x_cord:int, y_cord:int):
        screen.blit(self.text_surface,(x_cord,y_cord) )

    
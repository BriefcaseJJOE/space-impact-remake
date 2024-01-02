import pygame

class gui():
    def __init__(self, image_file_path) -> None:
        self.gui = pygame.image.load(image_file_path)
        self.gui = pygame.transform.scale(self.gui,(50,50))

    def update(self,screen ,x ,y ,lives):
        if lives == 1:
            screen.blit(self.gui, (x,y))
        if lives == 2:
            screen.blit(self.gui, (x,y))
            screen.blit(self.gui, (x+50,y))
        if lives == 3:
            screen.blit(self.gui, (x,y))
            screen.blit(self.gui, (x+50,y))
            screen.blit(self.gui, (x+100,y))
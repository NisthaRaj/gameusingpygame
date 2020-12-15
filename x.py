import pygame,sys
from pygame.locals import *

def main():
    pygame.init()
    global Window
    Window = pygame.display.set_mode((410,410))
    Window.fill((255,255,255))
    pygame.display.set_caption('First Game')
    Font1=pygame.font.SysFont('arial',22,True,True)
    textsurface=Font1.render('Hello',True,(0,0,0))
    Window.blit(textsurface,(0,0))
    image=pygame.image.load('sky.jpg')
    Window.blit(image,(0,0))
    pygame.display.update()
    print(pygame.font.get_fonts())

if __name__=="__main__":
    main()

##Mark Francis Aguarino a.k.a. Agua
import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 500
WINDOWHEIGHT = 500

#TEXT SIZE
LargeText = pygame.font.Font('freesansbold.ttf', 115)
MediumText = pygame.font.Font('freesansbold.ttf', 40)
SmallText = pygame.font.Font('freesansbold.ttf', 20)
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

bright_RED = (200, 0, 0)
bright_BLUE = (0, 0, 200)

def text_surfaceBLACK(text, surface):
    textSurf = surface.render(text, True, BLACK)
    textRect = textSurf.get_rect()

    return (textSurf, textRect)
def text_surfaceWHITE(text, surface):
    textSurf = surface.render(text, True, WHITE)
    textRect = textSurf.get_rect()

    return (textSurf, textRect)

def text_surfaceRED(text, surface):
    textSurf = surface.render(text, True, RED)
    textRect = textSurf.get_rect()

    return (textSurf, textRect)

def main():
    global DISPLAYSURF
    
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('SaveOurSoul')
    intro()
    
def intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        DISPLAYSURF.fill(WHITE)
        
        textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('SAVE OUR SOUL', MediumText)
        textRectObjGameName.center = (250, 200)
        DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)

    
        pygame.display.update()
       

    return()



if __name__ == '__main__':
    main()

import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 500
WINDOWHEIGHT = 500
FPS = 30
FPSCLOCK = pygame.time.Clock()
BoxSize = 60
GapSize = 10
LineTickness = 10
Board_Width_Height = 3
Player_1 = 'S'
Player_2 = 'O'
XMARGIN = int((WINDOWWIDTH - (Board_Width_Height * (BoxSize + GapSize))) / 2) 
YMARGIN = int((WINDOWHEIGHT - (Board_Width_Height * (BoxSize + GapSize))) / 2) 
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
    pygame.display.set_caption('SaveOurSole')
    intro()

def gamequit():
    pygame.quit()
    sys.exit()
    
def button(msg, x, y, w, h, ia, ac, action=None):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x+w > mouse[0] > x and y+h > mouse[1] > y:    
         pygame.draw.rect(DISPLAYSURF, ia, (x,y,w,h))
         if click[0] == 1 and action != None:
             action()
     else:
         pygame.draw.rect(DISPLAYSURF, ac, (x,y,w,h))
        
     textSurfaceObjPlay, textRectObjPlay = text_surfaceWHITE(msg, SmallText)
     textRectObjPlay.center = ( (x+(w/2)), (y+(h/2)) )
     DISPLAYSURF.blit(textSurfaceObjPlay, textRectObjPlay)
    
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

        button('PLAY',150,400,60,30,BLUE,bright_BLUE,game_loop)
        button('QUIT',250,400,60,30,RED,bright_RED,gamequit)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def right_side():
    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('p2', SmallText)
    textRectObjRound = (450,150)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)

    pygame.draw.rect(DISPLAYSURF, BLUE, (420, 180, 50, 50))

    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('S', LargeText)
    textRectObjRound = (400,290)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)

    return()

def left_side():

    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('p1', SmallText)
    textRectObjRound = (40,150)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)

    pygame.draw.rect(DISPLAYSURF, BLUE, (30, 180, 50, 50))

    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('S', LargeText)
    textRectObjRound = (20,290)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)

    return()

def leftTopCoordsOfBox(boxx, boxy):
    left = boxx * (BoxSize + GapSize) + XMARGIN
    top = boxy * (BoxSize + GapSize) + YMARGIN
    
    return (left, top)

def middle_invisible_boxes(x, y):
    
    for boxx in range(Board_Width_Height):
        for boxy in range(Board_Width_Height):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect((left, top, BoxSize, BoxSize))
            if boxRect.collidepoint(x, y):
                return(boxx, boxy)
    return(None, None)

def middle_vertical_lines():
    pygame.draw.line(DISPLAYSURF, BLACK, (XMARGIN+BoxSize+(GapSize/2),YMARGIN), ( (XMARGIN+BoxSize+(GapSize/2)), (YMARGIN + (BoxSize*3)+ (GapSize*2) ) ), 10)
    pygame.draw.line(DISPLAYSURF, BLACK, (XMARGIN + (BoxSize*2)+((GapSize*2)/2), YMARGIN) , ( (XMARGIN+ (BoxSize*2)+((GapSize*2)/2)), (YMARGIN + (BoxSize*3)+ (GapSize*2) ) ), 10)

def middle_horizontal_lines():
    pygame.draw.line(DISPLAYSURF, BLACK, (XMARGIN, YMARGIN + BoxSize +(GapSize/2)),(XMARGIN + (BoxSize*3)+ (GapSize*2), YMARGIN+BoxSize+(GapSize/2)), 10)
    pygame.draw.line(DISPLAYSURF, BLACK, (XMARGIN, YMARGIN + (BoxSize*2)+ ((GapSize*2)/2)),(XMARGIN+ (BoxSize*3)+ (GapSize*2), (YMARGIN+ (BoxSize*2)+((GapSize*2)/2))), 10)

def background():
    DISPLAYSURF.fill(WHITE)

    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('Round', MediumText)
    textRectObjRound.center = (250,30)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)
    
    right_side()
    left_side()
    middle_vertical_lines()
    middle_horizontal_lines()
    
    return()

def generateRevealedBoxesData():
    revealedBoxes = []
    for i in range(Board_Width_Height):
        revealedBoxes.append([' ']*Board_Width_Height)
    print(revealedBoxes)
    return revealedBoxes

def put_letter_on_board_player_1(boxes):
    for box in boxes:
        left, top = put_letter_on_board_center(box[0], box[1])


        textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(Player_1, MediumText)
        textRectObjLetter = (left,top)
        DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)

def put_letter_on_board_player_2(boxes):
    for box in boxes:
        left, top = put_letter_on_board_center(box[0], box[1])


        textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(Player_2, MediumText)
        textRectObjLetter = (left,top)
        DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
        
def put_letter_on_board_center(boxx, boxy):
    left = ((boxx * (BoxSize + GapSize) + XMARGIN) + (boxx+(BoxSize/4)))
    top = ((boxy * (BoxSize + GapSize) + YMARGIN) + (boxy+ (BoxSize/4)))
    
    return (left, top)

def boards(boxx, boxy, let):
    letter = []
    for x in range(9):
        if x == 0:
            letter.append(let)
        else:
            let = 0
            letter.append(let)

    board = []
    for x in range(Board_Width_Height):
        column = []
        for y in range(Board_Width_Height):
            column.append(letter[0])
            del letter[0]
        board.append(column)
    return(board)

def put_letter_on_board_leftTopCoordsOfBox(x, y):
    if x == 0:
        if y == 0:
            left = (((x+1) * (BoxSize/2)) + XMARGIN)-10
            top = (((y+1) * (BoxSize/2)) + YMARGIN)-10
        else:
            left = (((x+1) * (BoxSize/2)) + XMARGIN)-10
            top = (( (y*BoxSize) + (BoxSize/2)) + YMARGIN)-10
    else:
        left = (((x*BoxSize) + BoxSize/2 + (GapSize*x)) + XMARGIN)-10
        top = (( (y*BoxSize) + (BoxSize/2)) + YMARGIN)-10

    return (left, top)
    
def game_loop():
        
    global DISPLAYSURF, Player_1, Player_2, PLAYER_1
    PLAYER_1 = True
    mousex = 0
    mousey = 0
    
    revealedboxes = generateRevealedBoxesData()
    print(revealedboxes)
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('SaveOurSole')

    
    while True:
        background()
        if PLAYER_1 != False:
            textSurfaceObjLetter, textRectObjLetter = text_surfaceRED('PLAYER 1', MediumText)
            textRectObjLetter = (180,90)
            DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
        else:
            textSurfaceObjLetter, textRectObjLetter = text_surfaceRED('PLAYER 2', MediumText)
            textRectObjLetter = (180,90)
            DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)  
        for x in range(3):
            for y in range(3):
                if x == 0:
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)

                elif x == 1:
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)

                elif x == 2:
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter) 
        mouseClicked = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        boxx, boxy = middle_invisible_boxes(mousex, mousey)
        
        if PLAYER_1 != False:
            if boxx != None and boxy != None:
                if revealedboxes[boxx][boxy] != 'S' and revealedboxes[boxx][boxy] != 'O' and not mouseClicked:
                    put_letter_on_board_player_1([(boxx,boxy)])
                    revealedboxes[boxx][boxy] = 'S'
                    PLAYER_1 = False
                    print(revealedboxes)


        else:
            if boxx != None and boxy != None:
                if revealedboxes[boxx][boxy] != 'S' and revealedboxes[boxx][boxy] != 'O' and not mouseClicked:
                    put_letter_on_board_player_2([(boxx,boxy)])
                    revealedboxes[boxx][boxy] = 'O'
                    PLAYER_1 = True
                    print(revealedboxes)

                            
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()

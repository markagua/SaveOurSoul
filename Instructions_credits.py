import pygame
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


WINDOWWIDTH = 500
WINDOWHEIGHT = 500

fps = 25
FPSCLOCK = pygame.time.Clock()



win = False


BoxSize = 60
GapSize = 10
LineTickness = 10
Board_Width_Height = 3

PLAYER_Status = 'S'
Player_2 = 'O'

XMARGIN = int((WINDOWWIDTH - (Board_Width_Height * (BoxSize + GapSize))) / 2) 
YMARGIN = int((WINDOWHEIGHT - (Board_Width_Height * (BoxSize + GapSize))) / 2)

#TEXT SIZE
LargeText      = pygame.font.SysFont('comicsansms', 130)
MediumText     = pygame.font.SysFont('comicsansms', 30)
SmallText      = pygame.font.SysFont('comicsansms', 20)
supersmallText = pygame.font.SysFont('comicsansms', 12)

#Colors          R    G      B
WHITE       =  (255 , 255 , 255)
BLACK       =  (0   , 0   , 0  )
BLUE        =  (0   , 0   , 255)
RED         =  (255 , 0   , 0  )
GREEN       =  (0   , 255 , 0  )
GREY        =  (105 , 105 , 105)
bright_RED  =  (200 , 0   , 0  )
bright_BLUE =  (0   , 0   , 200)

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

def text_surfaceBLUE(text, surface):
    textSurf = surface.render(text, True, BLUE)
    textRect = textSurf.get_rect()

    return (textSurf, textRect)

def GameQuit():
    pygame.quit()
    sys.exit()

def Credits():
    pygame.mixer.music.stop()
    DISPLAYSURF.fill(WHITE)
    x = 0
    y = 700
    direction = 'up'
    
    while True:
        if direction == 'up':
            y = y - 5
            if y == 0:
                pygame.time.delay(2500)
                main()
                
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        companyname = pygame.image.load('images/credits.png')
        DISPLAYSURF.blit(companyname, (x,y))
        pygame.display.update()
        FPSCLOCK.tick(fps)
    
def Instructions():
    pygame.mixer.music.stop()
    DISPLAYSURF.fill(WHITE)
    textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('INSTRUCTION:', SmallText)
    textRectObjGameName.center = (250, 70)
    DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)
    textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('1. Player 1 will use S in order to get a point on every round.', supersmallText)
    textRectObjGameName = (50, 100)
    DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)
    textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('2. Player 2 will use O in order to get a point on every round.', supersmallText)
    textRectObjGameName = (50, 120)
    DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)
    textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('3. There are 10 rounds in a single match.', supersmallText)
    textRectObjGameName = (50, 140)
    DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)
    textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('4. If all of the boxes in a single round have been occupied and', supersmallText)
    textRectObjGameName = (50, 160)
    DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)
    textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('         no one has created S.O.S, it will be a draw.', supersmallText)
    textRectObjGameName = (50, 180)
    DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)
    textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('5. To win the game a player must make a letter combination S.O.S', supersmallText)
    textRectObjGameName = (50, 200)
    DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)
    textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('         (Horizontal, Vertical or Diagonal).', supersmallText)
    textRectObjGameName = (50, 220)
    DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)
    textSurfaceObjGameName, textRectObjGameName = text_surfaceBLACK('6. A player which acquires the highest score will win the game. ', supersmallText)
    textRectObjGameName = (50, 240)
    DISPLAYSURF.blit(textSurfaceObjGameName, textRectObjGameName)
    companyname = pygame.image.load('images/diagram.png')
    DISPLAYSURF.blit(companyname, (50,270))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        button('BACK',350,400,60,30,BLACK,GREY,Intro)
        
        pygame.display.update()
    
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Save Our Souls')

def main():
#Loading
    DISPLAYSURF.fill(WHITE)
    CompanyName()
#MAIN-Menu
    Intro()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
#Loading Starts
def CompanyName():

    companyname = pygame.image.load('images/company_name.png')
    DISPLAYSURF.blit(companyname, (0,0))
    pygame.display.update()
    pygame.time.delay(3000)

def Intro():
    intro = True
    
    
    while intro:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        DISPLAYSURF.fill(WHITE)
        
        background = pygame.image.load('images/gamemenu.png')
        DISPLAYSURF.blit(background, (0,0))

        button('PLAY',60,350,60,30,BLUE,bright_BLUE,Game_Loop)
        button('INSTRUCTIONS',140,350,200,30,GREY,BLACK,Instructions)
        button('CREDIT',360,350,80,30,BLACK,GREY,Credits)
        button('QUIT',220,400,60,30,RED,bright_RED,GameQuit)
        
        pygame.display.update()
        
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

def Game_Loop():
    global PLAYER_Status, win, Player_2, PLAYER_Status, revealedboxes, revealedcolor, Round, Score_P1, Score_P2, Count

    PLAYER_Status = True
    
    mousex = 0
    mousey = 0
    Round = 1
    boxx = 0
    boxy = 0
    Count = 0
    Score_P1 = 0
    Score_P2 = 0
    
    revealedboxes = generateRevealedBoxesData()
    revealedcolor = generateRevealedColor()

    DISPLAYSURF.fill(WHITE)
    while True:
        background(Round, Score_P1, Score_P2)
        
        if PLAYER_Status != False:
            textSurfaceObjLetter, textRectObjLetter = text_surfaceRED('PLAYER 1 Turn', MediumText)
            textRectObjLetter = (130,90)
            DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
        else:
            textSurfaceObjLetter, textRectObjLetter = text_surfaceBLUE('PLAYER 2 Turn', MediumText)
            textRectObjLetter = (130,90)
            DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
            
##        No one Win yet
        if win != False:
            pygame.time.delay(500)
            revealedboxes = generateRevealedBoxesData()
            Round = Round + 1
            mousex = 0
            mousey = 0
            boxx = 0
            boxy = 0
            Count = 0
            if PLAYER_Status == False:
                Score_P1 = Score_P1 + 1
            else:
                Score_P2 = Score_P2 + 1

            PLAYER_Status = True
            
#All Boxes is have Letters
        if Count  == 9 and win != True:
            DISPLAYSURF.fill(WHITE)
        
            background(Round, Score_P1, Score_P2)
            put_letter_on_board()
            
            textSurfaceObjLetter, textRectObjLetter = text_surfaceRED('DRAW!', MediumText)
            textRectObjLetter.center = (300,450)
            DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
            pygame.display.update()
            
            pygame.time.delay(3000)

            
            revealedboxes = generateRevealedBoxesData()
            Round = Round + 1
            mousex = 0
            mousey = 0
            boxx = 0
            boxy = 0
            Count = 0
            PLAYER_Status = True
            
#Check For Win When Rounds 11 
        if Round == 11:
            pygame.time.delay(2000)
            DISPLAYSURF.fill(WHITE)
            if Score_P1 > Score_P2:
                textSurfaceObjLetter, textRectObjLetter = text_surfaceRED('PLAYER 1 WIN!', MediumText)
                textRectObjLetter.center = (230,250)
                DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
                
            elif Score_P1 < Score_P2:
                textSurfaceObjLetter, textRectObjLetter = text_surfaceRED('PLAYER 2 WIN!', MediumText)
                textRectObjLetter.center = (230,250)
                DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
                
            elif Score_P1 == Score_P2:
                textSurfaceObjLetter, textRectObjLetter = text_surfaceRED('DRAW!', MediumText)
                textRectObjLetter.center = (230,250)
                DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)

            pygame.display.update()
            pygame.time.delay(3000)

            revealedboxes = generateRevealedBoxesData()
            Round = 1
            mousex = 0
            mousey = 0
            boxx = 0
            boxy = 0
            Count = 0
            Score_P1 = 0
            Score_P2 = 0
            
        mouseClicked = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        boxx, boxy = middle_invisible_boxes(mousex, mousey)
        
        if PLAYER_Status != False:
            if boxx != None and boxy != None:
                if revealedboxes[boxx][boxy] != 'S' and revealedboxes[boxx][boxy] != 'O' and not mouseClicked:
                    revealedboxes[boxx][boxy] = 'S'
                    revealedcolor[boxx][boxy] = 'blue'
                    PLAYER_Status = False
                    Count = Count + 1
        else:
            if boxx != None and boxy != None:
                if revealedboxes[boxx][boxy] != 'S' and revealedboxes[boxx][boxy] != 'O' and not mouseClicked:
                    revealedboxes[boxx][boxy] = 'O'
                    revealedcolor[boxx][boxy] = 'red'
                    PLAYER_Status = True
                    Count = Count + 1

        put_letter_on_board()
        win = draw_line()
        
        pygame.display.update()
# Generate array 
def generateRevealedBoxesData():
    revealedBoxes = []
    for i in range(Board_Width_Height):
        revealedBoxes.append([' ']*Board_Width_Height)
    return revealedBoxes

def generateRevealedColor():
    revealedBoxes = []
    for i in range(Board_Width_Height):
        revealedBoxes.append([' ']*Board_Width_Height)
    return revealedBoxes

def background(Round, Score_P1, Score_P2):
    DISPLAYSURF.fill(WHITE)
    background = pygame.image.load('images/battlegrounds.png')
    DISPLAYSURF.blit(background, (0,0))
    
    button('QUIT',400,450,60,30,RED,bright_RED,GameQuit)
    button('MENU',30,450,60,30,BLUE,bright_BLUE,Intro)
#Top
    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('Round', MediumText)
    textRectObjRound.center = (250,30)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)

    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('' + str(Round), MediumText)
    textRectObjRound.center = (350,30)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)
    
#Right_Side
    textSurfaceObjRound, textRectObjRound = text_surfaceBLUE('p2', SmallText)
    textRectObjRound = (430,150)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)

    pygame.draw.rect(DISPLAYSURF, BLUE, (420, 180, 50, 50))
    pygame.draw.rect(DISPLAYSURF, WHITE, (425, 185, 40, 40))

    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('O', LargeText)
    textRectObjRound = (400,290)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)

 
#Left_Side
    textSurfaceObjRound, textRectObjRound = text_surfaceRED('p1', SmallText)
    textRectObjRound = (40,150)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)

    pygame.draw.rect(DISPLAYSURF, RED, (30, 180, 50, 50))
    pygame.draw.rect(DISPLAYSURF, WHITE, (35, 185, 40, 40))

    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('S', LargeText)
    textRectObjRound = (20,290)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)
    
#Scoring
    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('' + str(Score_P1), MediumText)
    textRectObjRound.center = (45,205)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)

    textSurfaceObjRound, textRectObjRound = text_surfaceBLACK('' + str(Score_P2), MediumText)
    textRectObjRound.center = (435,205)
    DISPLAYSURF.blit(textSurfaceObjRound, textRectObjRound)
    
#Middle Vertical Lines
    pygame.draw.line(DISPLAYSURF, BLACK, (XMARGIN+BoxSize+(GapSize/2),YMARGIN), ( (XMARGIN+BoxSize+(GapSize/2)), (YMARGIN + (BoxSize*3)+ (GapSize*2) ) ), 10)
    pygame.draw.line(DISPLAYSURF, BLACK, (XMARGIN + (BoxSize*2)+((GapSize*2)/2), YMARGIN) , ( (XMARGIN+ (BoxSize*2)+((GapSize*2)/2)), (YMARGIN + (BoxSize*3)+ (GapSize*2) ) ), 10)

#Middle Horizontal Lines
    pygame.draw.line(DISPLAYSURF, BLACK, (XMARGIN, YMARGIN + BoxSize +(GapSize/2)),(XMARGIN + (BoxSize*3)+ (GapSize*2), YMARGIN+BoxSize+(GapSize/2)), 10)
    pygame.draw.line(DISPLAYSURF, BLACK, (XMARGIN, YMARGIN + (BoxSize*2)+ ((GapSize*2)/2)),(XMARGIN+ (BoxSize*3)+ (GapSize*2), (YMARGIN+ (BoxSize*2)+((GapSize*2)/2))), 10)

    
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

def put_letter_on_board():
    for x in range(3):
        for y in range(3):
            if x == 0:
                if revealedcolor[x][y] == 'red':
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceBLUE(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
                elif revealedcolor[x][y] == 'blue':
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
                else:
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)

            elif x == 1:
                if revealedcolor[x][y] == 'red':
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceBLUE(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
                elif revealedcolor[x][y] == 'blue':
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
                else:
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)

            elif x == 2:
                if revealedcolor[x][y] == 'red':
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceBLUE(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
                elif revealedcolor[x][y] == 'blue':
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
                else:
                    left, top = put_letter_on_board_leftTopCoordsOfBox(x, y)

                    textSurfaceObjLetter, textRectObjLetter = text_surfaceRED(revealedboxes[x][y], MediumText)
                    textRectObjLetter = (left,top)
                    DISPLAYSURF.blit(textSurfaceObjLetter, textRectObjLetter)
    
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

def put_letter_on_board_center(boxx, boxy):
    left = ((boxx * (BoxSize + GapSize) + XMARGIN) + (boxx+(BoxSize/4)))
    top = ((boxy * (BoxSize + GapSize) + YMARGIN) + (boxy+ (BoxSize/4)))
    
    return (left, top)

def draw_line():
    for i in range(3):
        y = 0
        if revealedboxes[i][0] != revealedboxes[i][1] and revealedboxes[i][0] == revealedboxes[i][2] and revealedboxes[i][2] == 'S' and revealedboxes[i][1] == 'O' and revealedboxes[i][0] == 'S':

            if i == 0:
                if PLAYER_Status == True:
                    pygame.draw.line(DISPLAYSURF, BLUE, ((XMARGIN + (BoxSize/2)), (YMARGIN + (BoxSize/2))), ((XMARGIN + (BoxSize/2)), (YMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2))), 10)
                    return(True)
                elif PLAYER_Status == False:
                    pygame.draw.line(DISPLAYSURF, RED, ((XMARGIN + (BoxSize/2)), (YMARGIN + (BoxSize/2))), ((XMARGIN + (BoxSize/2)), (YMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2))), 10) 
                    return(True)
            elif i == 1:
                if PLAYER_Status == True:                
                    pygame.draw.line(DISPLAYSURF, BLUE, ((XMARGIN + (BoxSize) + (GapSize) + (BoxSize/2)), (YMARGIN + (BoxSize/2))), ((XMARGIN + (BoxSize) + (GapSize) + (BoxSize/2)), (YMARGIN + (2*BoxSize)+ (2*GapSize) + (BoxSize/2))), 10)
                    return(True)
                elif PLAYER_Status == False:
                    pygame.draw.line(DISPLAYSURF, RED, ((XMARGIN + (BoxSize) + (GapSize) + (BoxSize/2)), (YMARGIN + (BoxSize/2))), ((XMARGIN + (BoxSize) + (GapSize) + (BoxSize/2)), (YMARGIN + (2*BoxSize)+ (2*GapSize) + (BoxSize/2))), 10)      
                    return(True)                    
            elif i == 2:
                if PLAYER_Status == True: 
                    pygame.draw.line(DISPLAYSURF, BLUE, ((XMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2)), (YMARGIN + (BoxSize/2))), ((XMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2)), (YMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2))), 10)
                    return(True)
                elif PLAYER_Status == False:
                    pygame.draw.line(DISPLAYSURF, RED, ((XMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2)), (YMARGIN + (BoxSize/2))), ((XMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2)), (YMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2))), 10)
                    return(True)       
        if revealedboxes[0][i] != revealedboxes[1][i] and revealedboxes[0][i] == revealedboxes[2][i] and revealedboxes[2][i] == 'S' and revealedboxes[1][i] == 'O' and revealedboxes[0][i] == 'S':
            if i == 0:
                if PLAYER_Status == True:                 
                    pygame.draw.line(DISPLAYSURF, BLUE, ((XMARGIN+ (BoxSize/2)), (YMARGIN + (BoxSize/2)+10)), ((XMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2)), (YMARGIN + (BoxSize/2)+10)), 10)
                    return(True)
                elif PLAYER_Status == False:
                    pygame.draw.line(DISPLAYSURF, RED, ((XMARGIN+ (BoxSize/2)), (YMARGIN + (BoxSize/2)+10)), ((XMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2)), (YMARGIN + (BoxSize/2)+10)), 10)
                    return(True)                    
            elif i == 1:
                if PLAYER_Status == True:                 
                    pygame.draw.line(DISPLAYSURF, BLUE, ((XMARGIN + (BoxSize/2)), (YMARGIN + (BoxSize) + (GapSize)+ (BoxSize/2))), ((XMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2)), (YMARGIN + (BoxSize)+ (GapSize)+ (BoxSize/2))), 10)
                    return(True)
                elif PLAYER_Status == False:
                    pygame.draw.line(DISPLAYSURF, RED, ((XMARGIN + (BoxSize/2)), (YMARGIN + (BoxSize) + (GapSize)+ (BoxSize/2))), ((XMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2)), (YMARGIN + (BoxSize)+ (GapSize)+ (BoxSize/2))), 10)
                    return(True)                    
            elif i == 2:
                if PLAYER_Status == True:                 
                    pygame.draw.line(DISPLAYSURF, BLUE, ((XMARGIN + (BoxSize/2)), (YMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2))-10), ((XMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2)), (YMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2)-10)), 10)
                    return(True)
                elif PLAYER_Status == False:
                    pygame.draw.line(DISPLAYSURF, RED, ((XMARGIN + (BoxSize/2)), (YMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2))-10), ((XMARGIN + (2*BoxSize)+ (2*GapSize)+ (BoxSize/2)), (YMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2)-10)), 10)
                    return(True)                    

        if revealedboxes[0][0] != revealedboxes[1][1] and revealedboxes[0][0] == revealedboxes[2][2] and revealedboxes[2][2] == 'S' and revealedboxes[1][1] == 'O' and revealedboxes[0][0] == 'S':          
            if PLAYER_Status == True: 
                pygame.draw.line(DISPLAYSURF, BLUE, (XMARGIN + ((BoxSize/2)), (YMARGIN + (BoxSize/2)+10)), ( (XMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2)) , (YMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2))), 10)
                return(True)
            elif PLAYER_Status == False:
                pygame.draw.line(DISPLAYSURF, RED, (XMARGIN + ((BoxSize/2)), (YMARGIN + (BoxSize/2)+10)), ( (XMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2)) , (YMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2))), 10)
                return(True)
        if revealedboxes[0][2] != revealedboxes[1][1] and revealedboxes[0][2] == revealedboxes[2][0] and revealedboxes[2][0] == 'S' and revealedboxes[1][1] == 'O' and revealedboxes[0][2] == 'S':
            if PLAYER_Status == True: 
                pygame.draw.line(DISPLAYSURF, BLUE, ((XMARGIN + (BoxSize/2)), (YMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2) ) ), ( (XMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2)), ( YMARGIN + (BoxSize/2)+10)), 10)
                return(True)
            elif PLAYER_Status == False:
                pygame.draw.line(DISPLAYSURF, RED, ((XMARGIN + (BoxSize/2)), (YMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2) ) ), ( (XMARGIN + (2*BoxSize) + (2*GapSize) + (BoxSize/2)), ( YMARGIN + (BoxSize/2)+10)), 10)
                return(True)
    return(False)

if __name__ == '__main__':
    main()

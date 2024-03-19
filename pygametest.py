import pygame
from pygame.locals import *
import sys
import random

Black = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAME_PER_SECOND = 60
PIC_WIDTH_HEIGHT = 140
MAX_WIDTH = WINDOW_WIDTH - PIC_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - PIC_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 140
N_PIXELS_TO_MOVE = 2
BLUE = (0,125,125)


#initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#load images and musics
A_h = pygame.image.load('images/1/1.png')
bgm = pygame.mixer.music.load('sounds/bgm.flac')
sound1 = pygame.mixer.Sound('sounds/123.wav')
pygame.mixer.music.play(-1,0)
# TargetImage = pygame.image.load('images/1/1.png')

#Initialize variables
Arect = A_h.get_rect()
Arect.left = 100
Arect.top = 100
# TargetRect = pygame.Rect(TARGET_X,TARGET_Y,TARGET_WIDTH_HEIGHT,TARGET_WIDTH_HEIGHT)
AXspeed = N_PIXELS_TO_MOVE
AYspeed = N_PIXELS_TO_MOVE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONUP:
        #     mouseX,mouseY = event.pos
        #     if Arect.collidepoint(event.pos):
        #         AX = random.randrange(MAX_WIDTH)
        #         AY = random.randrange(MAX_HEIGHT)
        #         Arect = pygame.Rect(AX,AY,PIC_WIDTH_HEIGHT,PIC_WIDTH_HEIGHT)
        
        # elif event.type == KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         AX = AX - N_PIXELS_TO_MOVE
        #     elif event.key == pygame.K_RIGHT:
        #         AX = AX + N_PIXELS_TO_MOVE
        #     elif event.key == pygame.K_UP:
        #         AY = AY - N_PIXELS_TO_MOVE
        #     elif event.key == pygame.K_DOWN:
        #         AY = AY + N_PIXELS_TO_MOVE
            
    # keyPressedTuple = pygame.key.get_pressed()

    # if keyPressedTuple[pygame.K_LEFT]:
    #     AX = AX - N_PIXELS_TO_MOVE
    # if keyPressedTuple[pygame.K_RIGHT]:
    #     AX = AX + N_PIXELS_TO_MOVE
    # if keyPressedTuple[pygame.K_UP]:
    #     AY = AY - N_PIXELS_TO_MOVE
    # if keyPressedTuple[pygame.K_DOWN]:
    #     AY = AY + N_PIXELS_TO_MOVE
    
    # if Arect.left<=0 or Arect.right>=WINDOW_WIDTH:
    #     AXspeed = -AXspeed
    #     # sound1.play()
        
    # if Arect.top<=0 or Arect.bottom>=WINDOW_HEIGHT:
    #     AYspeed = -AYspeed
    #     # sound1.play()

    # Arect.left = Arect.left + AXspeed
    # Arect.top = Arect.top + AYspeed
    

    window.fill(Black)

    #draw some pictures
    pygame.draw.line(window,BLUE,(20,20),(20,60),4)
    pygame.draw.line(window,BLUE,(20,60),(60,60),4)
    pygame.draw.line(window,BLUE,(60,60),(60,20),4)
    pygame.draw.line(window,BLUE,(60,20),(20,20),4)

    pygame.draw.ellipse(window,BLUE,(250,150,100,50),0)
    pygame.draw.ellipse(window,BLUE,(400,150,100,50),1)

    pygame.draw.aalines(window,BLUE,True,((230,432),(321,123),(323,121),(234,123)),20)
    # window.blit(TargetImage,(TARGET_X,TARGET_Y))
    # window.blit(A_h,Arect)
    pygame.display.update()
    clock.tick(FRAME_PER_SECOND)
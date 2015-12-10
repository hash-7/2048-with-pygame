import pygame, sys, time, random
from pygame.locals import *
from moves import *

pygame.init()
window = pygame.display.set_mode((450, 550), 0, 32)
pygame.display.set_caption("2048")



WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (77,204,0)
RED = (255,0,0)
PINK = (255,204,255)
BLUE = (0,0,255)
TEAL = (0,255,255)

board = init_board()

myfont = pygame.font.SysFont(None, 50)

blocks = []
for i in range(4):
    for j in range(4):
        blocks.append([pygame.Rect((i*100) + 30 , (j*100) + 135, 90, 90), WHITE])

def buildText(i,j):
        
    text = myfont.render(board[j][i], True, BLUE)
    textRect = text.get_rect()
    textRect.centerx = i*100 + 75
    textRect.centery = j*100 + 180
    return text, textRect

def showText():

    for i in range(4):
        for j in range(4):
            window.blit(buildText(i,j)[0], buildText(i,j)[1])
    
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:                
                board = main(board, "u")
            if event.key == K_DOWN:                
                board = main(board, "d")
            if event.key == K_LEFT:                
                board = main(board, "l")
            if event.key == K_RIGHT:                
                board = main(board, "r")

    window.fill(WHITE)
    pygame.draw.rect(window, GREEN, pygame.Rect(25, 130, 400, 400))

        
    for block in blocks:
        pygame.draw.rect(window, block[1], block[0])

        
    showText()
    
    pygame.display.update()

    time.sleep(0.02)
    

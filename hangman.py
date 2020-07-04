import pygame
from pygame.locals import *
import os

pygame.init()
#display screen
WIDTH,HEIGHT=800,500
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")
#button variables
RADIUS=20
GAP=15
letters=[]
startx=round((WIDTH-(RADIUS*2+GAP)*13)/2)
starty=400
for i in range(26):
    x=startx+GAP+2*((RADIUS*2+GAP)*(i%13))
    y=starty+((i//13)*(GAP+RADIUS*2))
    letters.append([x,y])
def draw():
        win.fill((255,255,255))
        for letter in letters:
            x,y=letter
            pygame.draw.circle(win,(0,0,0),(x,y),RADIUS,3)
        win.blit(images[hangman_status],(150,100))
        pygame.display.update()
#load images
images=list()
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".png")
    images.append(image)
    print(images)
#game variables
hangman_status=0



#Frame per second
FPS=60 #60 frames per second
clock=pygame.time.Clock()
draw()
#game loop
run=True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
pygame.quit()

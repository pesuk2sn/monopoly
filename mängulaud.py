import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((800,800), pygame.RESIZABLE)
green=159,226,191
black=0,0,0

ikoon=pygame.image.load("ikoon.png")
pygame.display.set_icon(ikoon)
pygame.display.set_caption("Monopoly")
laua_ikoon=pygame.image.load("laua_ikoon.png")
ristkülik=5, 5, 5, 5, 5

def mängulaud():
     pygame.draw.rect(screen, black, pygame.Rect(0,0,105,105))
     pygame.draw.rect(screen, green, pygame.Rect(1,1,103,103))
     ülemine_rida=["red", None, "red","red", None, "yellow","yellow", None, "yellow"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(i*80+105,0,80,105))
        pygame.draw.rect(screen, green, pygame.Rect(i*80+106,1,78,103))
        if ülemine_rida[i]!=None:
            pygame.draw.rect(screen, ülemine_rida[i], pygame.Rect(i*80+106,82, 78, 22 ))
     pygame.draw.rect(screen, black, pygame.Rect(825,0,105,105))
     pygame.draw.rect(screen, green, pygame.Rect(826,1,103,103))
     parempoolne_rida=["green","green", None, "green", None, None, "blue",None, "blue"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(900,i*80+105,80,105))
        pygame.draw.rect(screen, green, pygame.Rect(900,i*80,78,103))
        if parempoolne_rida[i]!=None:
            pygame.draw.rect(screen, ülemine_rida[i], pygame.Rect(82,i*80+106, 22, 78 ))

while True:
    screen.fill(green)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    mängulaud()
    pygame.display.update()

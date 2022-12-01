import pygame
import sys
#from monopoly import täringuvise
import random

pygame.init()

screen=pygame.display.set_mode((885,885), pygame.RESIZABLE)
green=159,226,191
black=0,0,0

x=800
y=800
width = 20
height=20
vel= 10
ikoon=pygame.image.load("ikoon.png")
pygame.display.set_icon(ikoon)
pygame.display.set_caption("Monopoly")
laua_ikoon=pygame.image.load("laua_ikoon.png")
laua_ikoon=pygame.transform.scale(laua_ikoon, (508.4, 133.6))
laua_ikoon=pygame.transform.rotate(laua_ikoon, 45)
vangla_ikoon=pygame.image.load("vangla_ikoon.jpg")
vangla_ikoon=pygame.transform.scale(vangla_ikoon,(72,72.125))
parkimise_ikoon=pygame.image.load("tasuta_parkimine.png")
parkimise_ikoon=pygame.transform.scale(parkimise_ikoon,(110,111.3))
parkimise_ikoon=pygame.transform.rotate(parkimise_ikoon, 235)
vanglasse_ikoon=pygame.image.load("vangi_ikoon.png")
vanglasse_ikoon=pygame.transform.scale(vanglasse_ikoon,(90,90))
vanglasse_ikoon=pygame.transform.rotate(vanglasse_ikoon, -45)
go_ikoon=pygame.image.load("go.jpg")
go_ikoon=pygame.transform.scale(go_ikoon,(106,100.2))
ristkülik=5, 5, 5, 5, 5
font=pygame.font.SysFont("Microsoft Sans Serif", 10)

def täringuvise():
    täring_1=random.randint(1,6)
    täring_2=random.randint(1,6)
    print(täring_1,täring_2)
    sammud=täring_1+täring_2
    return sammud

def mängulaud():

     pygame.draw.rect(screen, black, pygame.Rect(0,0,105,105))
     pygame.draw.rect(screen, green, pygame.Rect(1,1,103,103))

     ülemine_rida=["red", None, "red","red", None, "yellow","yellow", None, "yellow"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(i*75+105,0,75,105))
        pygame.draw.rect(screen, green, pygame.Rect(i*75+106,1,73,103))
        if ülemine_rida[i]!=None:
            pygame.draw.rect(screen, ülemine_rida[i], pygame.Rect(i*75+106,82, 73, 22 ))
     pygame.draw.rect(screen, black, pygame.Rect(780,0,105,105))
     pygame.draw.rect(screen, green, pygame.Rect(781,1,103,103))
     parempoolne_rida=["green","green", None, "green", None, None, "blue",None, "blue"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(780,i*75+105,105,75))
        pygame.draw.rect(screen, green, pygame.Rect(781,i*75+106,103,73))
        if parempoolne_rida[i]!=None:
          pygame.draw.rect(screen, parempoolne_rida[i], pygame.Rect(781,i*75+106, 22, 73 ))
     pygame.draw.rect(screen, black, pygame.Rect(780,780,105,105))
     pygame.draw.rect(screen, green, pygame.Rect(781,781,103,103))
     alumine_rida=["aqua", "aqua", None,"aqua", None, None, "brown", None, "brown"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(i*75+105,780,75,105))
        pygame.draw.rect(screen, green, pygame.Rect(i*75+106,781,73,103))
        if alumine_rida[i]!=None:
          pygame.draw.rect(screen, alumine_rida[i], pygame.Rect(i*75+106,781,  73, 22 ))
     pygame.draw.rect(screen, black, pygame.Rect(0,780,105,105))
     pygame.draw.rect(screen, green, pygame.Rect(1,781,103,103))
     vasakpoolne_rida=["orange", "orange", None, "orange", None, "purple","purple", None, "purple"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(0,i*75+105,105,75))
        pygame.draw.rect(screen, green, pygame.Rect(1,i*75+106,103,73))
        if vasakpoolne_rida[i]!=None:
          pygame.draw.rect(screen, vasakpoolne_rida[i], pygame.Rect(82,i*75+106, 22, 73 ))

def ikoonid():
   screen.blit(parkimise_ikoon,(-30,-10))
   screen.blit(laua_ikoon,(200,200))
   screen.blit(vangla_ikoon,(33,779))
   screen.blit(vanglasse_ikoon,(780,-10))
   screen.blit(go_ikoon,(780,780))

def kirjed():
  ülemine_rida=["PIKK   ","VÕIMALUS2","AARDLA","AARDLA","PUUSSEPA", "PUIESTEE","KALDA", "VEEVÄRK", "VÕRU"]
  ülemine_rida_hinnad=["220",None, "220", None, "240", "260", "260", None, "280"  ]
  for i in range(9):
    hind=font.render(ülemine_rida_hinnad[i], True, black)
    hind=pygame.transform.rotate(hind, 180)
    screen.blit(hind,(i*75+130,10))
    tekst=font.render(ülemine_rida[i], True, black)
    tekst=pygame.transform.rotate(tekst, 180)
    screen.blit(tekst,(i*75+110,65))
  parempoolne_rida=["TURU   ", " NARVA MNT","KIRST3", "RIIA   ","TARTU","VÕIMALUS3", "RÜÜTLI  ","MAKSUD2","RAEKODA"]
  parempoolne_rida_hinnad=["300", "300", None, "320", None, None, "350", None, "400", ]
  for i in range(9):
    hind=font.render(parempoolne_rida_hinnad[i], True, black)
    hind=pygame.transform.rotate(hind, 90)
    screen.blit(hind,(860,i*75+130))
    tekst=font.render(parempoolne_rida[i], True, black)
    tekst=pygame.transform.rotate(tekst, 90)
    screen.blit(tekst,(805,i*75+115))
  alumine_rida=["ILMATSALU", "RINGTEE","VÕIMALUS", "RAVILA", "ÜLENURME ","MAKSUD","SOINASTE", "KIRST1", "JAAMA"]
  alumine_rida_hinnad=["120","100",None, "100",None,None,"60",None, "60"]
  for i in range(9):
    hind=font.render(alumine_rida_hinnad[i], True, black)
    screen.blit(hind,(i*75+130,865))
    tekst=font.render(alumine_rida[i], True, black)
    screen.blit(tekst,(i*75+120,805))
  vasakpoolne_rida=["VAKSALI", "KREUTZWALDI","KIRST2","KALEVI","KIRSI","KESK KAAR", "SÕBRA","ELEKTER", "VABADUSE PST"]
  vasakpoolne_rida_hinnad=["200","180", None, "180", None,"160","140", None,"140"]
  for i in range(9):
    hind=font.render(vasakpoolne_rida_hinnad[i], True, black)
    hind=pygame.transform.rotate(hind, 270)
    screen.blit(hind,(10,i*75+130))
    tekst=font.render(vasakpoolne_rida[i], True, black)
    tekst=pygame.transform.rotate(tekst, 270)
    screen.blit(tekst,(70,i*75+105))

while True:
    screen.fill(green)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >0:
      x-=vel*täringuvise()
    if keys[pygame.K_RIGHT] and x<885-width:
      x+=vel
    if keys[pygame.K_UP] and y>0:
      y-=vel
    if keys[pygame.K_DOWN] and y<885-height:
      y+=vel
    
   
    mängulaud()
    ikoonid()
    kirjed() 
    pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
    pygame.display.update()

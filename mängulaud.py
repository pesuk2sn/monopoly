import pygame
import sys
from pygame.locals import *
from funktsioonid import *
import pygame_gui
from time import sleep

pygame.init()

screen = pygame.display.set_mode((885, 885), pygame.RESIZABLE)
green = 159, 226, 191
black = 0, 0, 0
manager = pygame_gui.UIManager((885, 885))
kell = pygame.time.Clock()
x = 800
y = 800
width = 20
height = 20
vel = 10
ikoon = pygame.image.load("pildid/ikoon.png")
mängija_1 = pygame.image.load("pildid/mängija1.png")
mängija_1 = pygame.transform.scale(mängija_1, (128, 72))
mängija_2 = pygame.image.load("pildid/mängija2.png")
mängija_2 = pygame.transform.scale(mängija_2, (80, 80))
mängija_1_pos = mängija_1.get_rect(topleft=(780, 780))
mängija_2_pos = mängija_2.get_rect(topleft=(800, 800))
current_image = None
LeftButton = 0
pygame.display.set_icon(ikoon)
pygame.display.set_caption("Monopoly")
laua_ikoon = pygame.image.load("pildid/laua_ikoon.png")
laua_ikoon = pygame.transform.scale(laua_ikoon, (508.4, 133.6))
laua_ikoon = pygame.transform.rotate(laua_ikoon, 45)
vangla_ikoon = pygame.image.load("pildid/vangla_ikoon.jpg")
vangla_ikoon = pygame.transform.scale(vangla_ikoon, (72, 72.125))
parkimise_ikoon = pygame.image.load("pildid/tasuta_parkimine.png")
parkimise_ikoon = pygame.transform.scale(parkimise_ikoon, (110, 111.3))
parkimise_ikoon = pygame.transform.rotate(parkimise_ikoon, 235)
vanglasse_ikoon = pygame.image.load("pildid/vangi_ikoon.png")
vanglasse_ikoon = pygame.transform.scale(vanglasse_ikoon, (90, 90))
vanglasse_ikoon = pygame.transform.rotate(vanglasse_ikoon, -45)
go_ikoon = pygame.image.load("pildid/go.jpg")
go_ikoon = pygame.transform.scale(go_ikoon, (106, 100.2))
font = pygame.font.SysFont("Microsoft Sans Serif", 10)
font2 = pygame.font.SysFont("Microsoft Sans Serif", 20)


def mängulaud():

     pygame.draw.rect(screen, black, pygame.Rect(0, 0, 105, 105))
     pygame.draw.rect(screen, green, pygame.Rect(1, 1, 103, 103))

     ülemine_rida = ["red", None, "red", "red",
         None, "yellow", "yellow", None, "yellow"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(i*75+105, 0, 75, 105))
        pygame.draw.rect(screen, green, pygame.Rect(i*75+106, 1, 73, 103))
        if ülemine_rida[i] != None:
            pygame.draw.rect(
                screen, ülemine_rida[i], pygame.Rect(i*75+106, 82, 73, 22))
     pygame.draw.rect(screen, black, pygame.Rect(780, 0, 105, 105))
     pygame.draw.rect(screen, green, pygame.Rect(781, 1, 103, 103))
     parempoolne_rida = ["green", "green", None,
         "green", None, None, "blue", None, "blue"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(780, i*75+105, 105, 75))
        pygame.draw.rect(screen, green, pygame.Rect(781, i*75+106, 103, 73))
        if parempoolne_rida[i] != None:
          pygame.draw.rect(
              screen, parempoolne_rida[i], pygame.Rect(781, i*75+106, 22, 73))
     pygame.draw.rect(screen, black, pygame.Rect(780, 780, 105, 105))
     pygame.draw.rect(screen, green, pygame.Rect(781, 781, 103, 103))
     alumine_rida = ["aqua", "aqua", None, "aqua",
         None, None, "brown", None, "brown"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(i*75+105, 780, 75, 105))
        pygame.draw.rect(screen, green, pygame.Rect(i*75+106, 781, 73, 103))
        if alumine_rida[i] != None:
          pygame.draw.rect(screen, alumine_rida[i], pygame.Rect(
              i*75+106, 781,  73, 22))
     pygame.draw.rect(screen, black, pygame.Rect(0, 780, 105, 105))
     pygame.draw.rect(screen, green, pygame.Rect(1, 781, 103, 103))
     vasakpoolne_rida = ["orange", "orange", None,
         "orange", None, "purple", "purple", None, "purple"]
     for i in range(9):
        pygame.draw.rect(screen, black, pygame.Rect(0, i*75+105, 105, 75))
        pygame.draw.rect(screen, green, pygame.Rect(1, i*75+106, 103, 73))
        if vasakpoolne_rida[i] != None:
          pygame.draw.rect(
              screen, vasakpoolne_rida[i], pygame.Rect(82, i*75+106, 22, 73))


def ikoonid():
   screen.blit(parkimise_ikoon, (-30, -10))
   screen.blit(laua_ikoon, (200, 200))
   screen.blit(vangla_ikoon, (33, 779))
   screen.blit(vanglasse_ikoon, (780, -10))
   screen.blit(go_ikoon, (780, 780))


def kirjed():
  ülemine_rida = ["PIKK   ", "VÕIMALUS2", "AARDLA", "PUUSSEPA",
      "   ", "PUIESTEE", "KALDA", "VEEVÄRK", "VÕRU"]
  ülemine_rida_hinnad = ["220", None, "220",
      "240", None, "260", "260", None, "280"]
  for i in range(9):
    hind = font.render(ülemine_rida_hinnad[i], True, black)
    hind = pygame.transform.rotate(hind, 180)
    screen.blit(hind, (i*75+130, 10))
    tekst = font.render(ülemine_rida[i], True, black)
    tekst = pygame.transform.rotate(tekst, 180)
    screen.blit(tekst, (i*75+110, 65))
  parempoolne_rida = ["TURU   ", " NARVA MNT", "KIRST3", "RIIA   ",
      "TARTU", "VÕIMALUS3", "RÜÜTLI  ", "MAKSUD2", "RAEKODA"]
  parempoolne_rida_hinnad = ["300", "300", None,
      "320", None, None, "350", None, "400", ]
  for i in range(9):
    hind = font.render(parempoolne_rida_hinnad[i], True, black)
    hind = pygame.transform.rotate(hind, 90)
    screen.blit(hind, (860, i*75+130))
    tekst = font.render(parempoolne_rida[i], True, black)
    tekst = pygame.transform.rotate(tekst, 90)
    screen.blit(tekst, (805, i*75+115))
  alumine_rida = ["ILMATSALU", "RINGTEE", "VÕIMALUS", "RAVILA",
      "ÜLENURME ", "MAKSUD", "SOINASTE", "KIRST1", "JAAMA"]
  alumine_rida_hinnad = ["120", "100", None,
      "100", None, None, "60", None, "60"]
  for i in range(9):
    hind = font.render(alumine_rida_hinnad[i], True, black)
    screen.blit(hind, (i*75+130, 865))
    tekst = font.render(alumine_rida[i], True, black)
    screen.blit(tekst, (i*75+120, 805))
  vasakpoolne_rida = ["VAKSALI", "KREUTZWALDI", "KIRST2", "KALEVI",
      "KIRSI", "KESK KAAR", "SÕBRA", "ELEKTER", "VABADUSE PST"]
  vasakpoolne_rida_hinnad = ["200", "180", None,
      "180", None, "160", "140", None, "140"]
  for i in range(9):
    hind = font.render(vasakpoolne_rida_hinnad[i], True, black)
    hind = pygame.transform.rotate(hind, 270)
    screen.blit(hind, (10, i*75+130))
    tekst = font.render(vasakpoolne_rida[i], True, black)
    tekst = pygame.transform.rotate(tekst, 270)
    screen.blit(tekst, (70, i*75+105))


while True:
    screen.fill(green)
    aeg_delta = kell.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if mängija_1_pos.collidepoint(event.pos):
            current_image = 0
          elif mängija_2_pos.collidepoint(event.pos):
            current_image = 1
          else:
            current_image = None
        if event.type == MOUSEMOTION:
          if event.buttons[LeftButton]:
            rel = event.rel
            if current_image == 0:
              mängija_1_pos.x += rel[0]
              mängija_1_pos.y += rel[1]
            elif current_image == 1:
              mängija_2_pos.x += rel[0]
              mängija_2_pos.y += rel[1]

                               
    
        manager.process_events(event)
    manager.update(aeg_delta)
   
    mängulaud()
    ikoonid()
    kirjed() 
    manager.draw_ui(screen)
    screen.blit(mängija_1, mängija_1_pos)
    screen.blit(mängija_2, mängija_2_pos)
    pygame.display.update()

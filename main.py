from genome import dot
from genome import chaser
import sys
import pygame as pg
import random as r
import threading

population_dot=30
population_chaser=5
pg.init()
screen = pg.display.set_mode((1200, 800))
dots=[]
chasers=[]

for x in range(population_dot):
    dots.append(dot())
for x in range(population_chaser):
    chasers.append(chaser())

dot=dot()
chaser=chaser()

def dotmove(population_dot):
    for i in range(population_dot):
        dots[i].update()
        dots[i].show(screen)

def chasermove(population_chaser):
    for i in range(population_chaser):
        chasers[i].update()
        chasers[i].show(screen)

def simulation():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill([255, 255,255])
        dotthread = threading.Thread(target=dotmove,args=(population_dot,))
        chaserthread = threading.Thread(target=chasermove, args=(population_chaser,))
        dotthread.start()
        chaserthread.start()
        pg.display.update()

simulation()

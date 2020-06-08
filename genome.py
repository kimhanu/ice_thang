import pygame as pg
import random as r
import math

class dot():
    def __init__(self):
        self.x_pos = r.randint(0,1200)
        self.y_pos = r.randint(0,800)
        self.x_speed = 1
        self.y_speed = 1

    def show(self,screen):#put sensor and show
        pg.draw.circle(screen, [0,0,0], [self.x_pos, self.y_pos], 10)
        #pg.draw.circle(screen, [240, 240, 240], [self.x_pos, self.y_pos], 40, 2)
        pg.draw.circle(screen, [240, 240, 240], [self.x_pos, self.y_pos-40], 4)
        pg.draw.circle(screen, [240, 240, 240], [self.x_pos, self.y_pos+40], 4)
        pg.draw.circle(screen, [240, 240, 240], [self.x_pos-40, self.y_pos], 4)
        pg.draw.circle(screen, [240, 240, 240], [self.x_pos+40, self.y_pos], 4)
        pg.draw.circle(screen, [240, 240, 240], [self.x_pos+30, self.y_pos+30], 4)
        pg.draw.circle(screen, [240, 240, 240], [self.x_pos-30, self.y_pos-30], 4)
        pg.draw.circle(screen, [240, 240, 240], [self.x_pos+30, self.y_pos-30], 4)
        pg.draw.circle(screen, [240, 240, 240], [self.x_pos-30, self.y_pos+30], 4)
    def update(self):
        if r.randint(0,100)>99:
            self.x_speed = r.randint(-1,1)
            self.y_speed = r.randint(-1,1)
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
        if self.x_pos<0 or self.x_pos>1200:
            self.x_speed=self.x_speed*-1
        elif self.y_pos<0 or self.y_pos>800:
            self.y_speed=self.y_speed*-1

class chaser():
    def __init__(self):
        self.x_pos = r.randint(0, 1200)
        self.y_pos = r.randint(0, 800)
        self.x_speed = 2
        self.y_speed = 2

    def show(self,screen):
        pg.draw.circle(screen, [255,0,0], [self.x_pos, self.y_pos], 20)
        pg.draw.circle(screen, [255, 220, 220], [self.x_pos, self.y_pos], 31, 2)
    def update(self):
        if r.randint(0,100)>99:
            self.x_speed = r.randint(-2,2)
            self.y_speed = r.randint(-2,2)
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
        if self.x_pos<0 or self.x_pos>1200:
            self.x_speed=self.x_speed*-1
        elif self.y_pos<0 or self.y_pos>800:
            self.y_speed=self.y_speed*-1

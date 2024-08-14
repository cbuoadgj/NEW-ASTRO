#Libraries
import pygame as pg
import math 
from random import randint

# Initialize pygame

pg.init()

# Create a widnow
screen_info = pg.display.Info()
width=screen_info.current_w 
height=screen_info.current_h
window = pg.display.set_mode((width-200, height-200))
pg.display.set_caption("SOLAR SYSTEM SIMULATION")

#Create simulation
run=True
while True:


    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

# Quit simulation
pg.quit()
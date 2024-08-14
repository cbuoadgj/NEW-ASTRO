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
window = pg.display.set_mode((width, height))
pg.display.set_caption("SOLAR SYSTEM SIMULATION")

# Color the screen
window.fill((0,0,0))

# Stars List with colors, center and radius information

stars_list=[
    { 
        'color': (randint(190,255),randint(190,255),randint(190,255)),
        'center': (randint(5,width-5),randint(5,height-5)),
        'radius': (randint(1,2))
    }
    for star in range (450)
]
# Function to draw the stars on window
def draw_stars(stars_list):
    for star in stars_list:
        pg.draw.circle(window,star['color'],star['center'],star['radius'])


#Create simulation
run=True
while True:


    draw_stars(stars_list)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key==pg.K_ESCAPE:
            pg.quit()
            quit()
    pg.display.update()
# Quit simulation
pg.quit()
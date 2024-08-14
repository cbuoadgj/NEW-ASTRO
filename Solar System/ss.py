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
black=(0,0,0)
yellow = (255,255,0)
gray = (183, 184, 185)
blue=	(107,147,214)
red=	(193,68,14)
yellow_white=(248,226,176)

# Class of Planets List with colors, center and radius information
class solarsystembodies :

    AU=1.496e+11
    scale=250/AU

    # Constructor function
    def __init__(self, name, color, x,y, mass, radius):
        self.name=name
        self.color=color
        self.x=x
        self.y=y
        self.mass=mass
        self.radius=radius
    # Method to create bodies 
    def draw_body(self,arg):
        x=self.x*solarsystembodies.scale + width//2
        y=self.y*solarsystembodies.scale + height//2
        pg.draw.circle(surface=window,color=self.color,center=(x,y),radius=self.radius)


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
sun=solarsystembodies("sun",yellow,0,0,1.989e30,30)
mercury=solarsystembodies("mercury",gray,0.39*solarsystembodies.AU,0,0.33e24,6) 
venus=solarsystembodies("venus",yellow_white,0.72*solarsystembodies.AU,0,4.87e24,14)
earth=solarsystembodies("earth",blue,1*solarsystembodies.AU,0,5.97e24,15)
mars=solarsystembodies("mars",red,1.52*solarsystembodies.AU,0,6.42e23,8)

while True:


    draw_stars(stars_list)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key==pg.K_ESCAPE:
            pg.quit()
            quit()
    ss_bodies= [sun,mercury,venus,earth,mars]
    for body in ss_bodies:
        body.draw_body(window)       
    pg.display.update()
# Quit simulation
pg.quit()
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
    time_step=24*3600
    # Constructor function
    def __init__(self, name, color, x,y, mass, radius):
        self.name=name
        self.color=color
        self.x=x
        self.y=y
        self.mass=mass
        self.radius=radius
        self.vel_x=0
        self.vel_y=0
        self.orbit=[]
    # Method 1 to create bodies 
    def draw_body(self,window):
        x=self.x*solarsystembodies.scale + width//2
        y=self.y*solarsystembodies.scale + height//2
        pg.draw.circle(surface=window,color=self.color,center=(x,y),radius=self.radius)

    # Method 2 to calculate the gravitational force
    def calculate_gravitational_force(self, ss_body):
        G=6.67430e-11
        x_diff=ss_body.x-self.x
        y_diff=ss_body.y-self.y
        distance=math.sqrt(x_diff**2 + y_diff**2)
        g_force=(G*self.mass*ss_body.mass/distance**2)
        theta=math.atan2(y_diff,x_diff)
        f_x=g_force*math.cos(theta)
        f_y=g_force*math.sin(theta)
        return f_x,f_y

    # Method to update position of bodies
    '''
    1) Net Force --> x and y
    2) Acceleration --> x and y
    3) velocity --> vel + acc*dt
    4) x --> x+v*dt
    5) store position
    '''
    def update_position(self,ss_bodies):
        net_fx,net_fy=0,0
        for ss_body in ss_bodies:
            if self!=ss_body:
                fx,fy=self.calculate_gravitational_force(ss_body)
                net_fx+=fx
                net_fy+=fy

        self.vel_x+=net_fx/self.mass*self.time_step
        self.vel_y+=net_fy/self.mass*self.time_step 
        self.x+=self.vel_x*self.time_step
        self.y+=self.vel_y*self.time_step  
        self.orbit.append((self.x,self.y))





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
pause=False

# Create planets
sun=solarsystembodies("sun",yellow,0,0,1.989e30,30)
mercury=solarsystembodies("mercury",gray,0.39*solarsystembodies.AU,0,0.33e24,6) 
mercury.vel_y= -47.4e3
venus=solarsystembodies("venus",yellow_white,0.72*solarsystembodies.AU,0,4.87e24,9)
venus.vel_y= -35e3
earth=solarsystembodies("earth",blue,1*solarsystembodies.AU,0,5.97e24,15)
earth.vel_y= -29.8e3
mars=solarsystembodies("mars",red,1.52*solarsystembodies.AU,0,6.42e23,10)
mars.vel_y= -24.1e3

# Set FPS for simulation
FPS=60
clock = pg.time.Clock()


while True:
    clock.tick(FPS)
    window.fill(black)
    draw_stars(stars_list)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                pg.quit()
                quit()
            elif event.key == pg.K_SPACE:
                pause=not pause
    if not pause: 
        ss_bodies= [sun,mercury,venus,earth,mars]
        for body in ss_bodies:
            body.update_position(ss_bodies)
            body.draw_body(window)       
        pg.display.update()
# Quit simulation
pg.quit()
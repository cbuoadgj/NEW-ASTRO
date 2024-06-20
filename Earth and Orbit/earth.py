import numpy as np
import matplotlib as plt

# Constants
G=6.67430e-11
M_sun=1.989e30

# Initial position and velocity 
r_0= np.array([147.098e9,0])  # in meters
v_0= np.array([0,30.29e3]) # in m/s

# Time steps and total time for simulation
dt=3600  # in seconds
t_max=3.154e7 # 1 year 

# Time array to be used in numerical solution
t=np.arange(0,t_max,dt)

# Initialize array to store positions and velocities at all time steps
r=np.empty(shape=(len(t),2))
v=np.empty(shape=(len(t),2))

# Set the initial conditions for position and velocity
r[0]=r_0
v[0]=v_0

# Defining the acceleration function
def accn(r):
    return (-G*M_sun/np.linalg.norm(r)**3 * r)

# Numerical integration using Euler method
def euler_method(r,v,accn,dt):

    """ 
    Equations for Euler method
    --------------------------

    ODE for position: dr/dt = v
    r_new = r_old + dt * v

    ODE for velocity: dv/dt = a(r)
    v_new = v_old + dt * a(r)

    Parameters:
    -----------
    r: empty array for position of size t
    v: empty array for velocity of size t
    a: function to calculate acceleration at a given position
    dt: time step for the simulation

    """
    for i in range(1, len(t)):
     r[i] = r[i-1] + dt * v[i-1]
     v[i] = v[i-1] + accn(r[i-1]) * dt
    
euler_method(r,v,accn,dt)
print(r)






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

# Apply Euler method on given initial conditions
euler_method(r,v,accn,dt)


# Find the point at which earth is at its aphelion(furthest from the sun)
sizes = np.array(np.linalg.norm(r, axis=1))
pos_aphelion=np.max(sizes)
arg_aphelion = np.argmax(sizes)
vel_aphelion = np.linalg.norm(v[arg_aphelion])

# Print the results

print(f"Earth is at its aphelion at t={t[arg_aphelion]/3600} years")
print(f"Speed at aphelion: {vel_aphelion/1000} km/s")

# RK4 integration      
def rk4_method(r, v, accn, dt):
    """
    Equations for RK4 method
    --------------------------

    ODE for position: dr/dt = v
    r_new = r_old + dt * (1/6) * (k1r + 2k2r + 2k3r + k4r)

    ODE for velocity: dv/dt = a(r)
    v_new = v_old + dt/6 * (k1v + 2k2v + 2k3v + k4v)

    Parameters:
    -----------
    r: empty array for position of size t
    v: empty array for velocity of size t
    a: function to calculate acceleration at a given position
    dt: time step for the simulation

    Method to calculate steps
    -------------------------
    step1 = 0
    k1v = dt * a(r[i-1])
    k1r = v[i-1]
     
    step2 = dt/2 using k1
    k2v = dt * a(r[i-1] +k1r*dt/2)
    k2r = v[i-1] + k1v*dt/2

    step3 = dt/2 using k2
    k3v = dt * a(r[i-1] + k2r*dt/2)
    k3r = v[i-1] + k2v*dt/2
    
    step4 = dt using k3
    k4v = dt * a(r[i-1] + k3r*dt/1)
    k4r = v[i-1] + k3v*dt
    """
    for i in range(1, len(r)):
        k1v = dt * accn(r[i-1])
        k1r = v[i-1]
     
        k2v = dt * accn(r[i-1] +k1r*dt/2)
        k2r = v[i-1] + k1v*dt/2

        k3v = dt * accn(r[i-1] + k2r*dt/2)
        k3r = v[i-1] + k2v*dt/2
    
        k4v = dt * accn(r[i-1] + k3r*dt/1)
        k4r = v[i-1] + k3v*dt

        r[i] = r[i-1] + dt * (1/6) * (k1r + 2*k2r + 2*k3r + k4r)
        v[i] = v[i-1] + dt/6 * (k1v + 2*k2v + 2*k3v + k4v)

rk4_method(r,v,accn,dt)
def numerical_intergration(r,v,accn,dt,method='euler'):
    """
    this function performs numerical integration using either Euler or RK4 method
    """
    if method=='euler':
      euler_method(r,v,accn,dt)
    elif method=='rk4':
      rk4_method(r,v,accn,dt)
    else:
      raise ValueError("Invalid method. Choose either 'euler' or 'rk4':")      
# Call the numerical integration function
numerical_intergration(r,v,accn,dt,method='rk4cls')
# Print the results
print(f"Speed at aphelion: {vel_aphelion/1000} km/s")
print(f"aphelion distance: {pos_aphelion/1e9} billion km") 
print(f"perihelion distance: {sizes[0]/1e9} billion km")        
   







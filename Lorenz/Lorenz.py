import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# define the initial system state (x, y, z positions in space)
initial_state = [0.1, 0, 0]

# define the system parameters sigma, rho, and beta
sigma = 10.
rho   = 26.
beta  = 8./3.

#define the time points to solve for, evenly spaced between the start and end times
start_time = 1
end_time = 60
interval = 100
tspan = np.linspace(start_time, end_time, end_time * interval)

# define the lorenz system
def lorenz_system(current_state, t):
    x, y, z = current_state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# get the points to plot, by integrating the system of equations
points = odeint(lorenz_system, initial_state, tspan)


# draw plots
fig = plt.figure(figsize=(12, 9))
ax = plt.axes(facecolor='black') 
plt.plot(points[:, 0], points[:, 1], 'r', linewidth = 1, label='sigma= ' + str(sigma) + '\nrho=' + str(rho) + '\nbeta' + str(beta))
plt.title("Lorenz system")
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

fig = plt.figure(figsize=(12, 9))
ax = plt.axes(facecolor='black') 
plt.plot(points[:, 0], points[:, 2], 'r', linewidth = 1, label='sigma= ' + str(sigma) + '\nrho=' + str(rho) + '\nbeta' + str(beta))
plt.title("Lorenz system")
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('z')
plt.grid()
plt.show()

fig = plt.figure(figsize=(12, 9))
ax = plt.axes(facecolor='black') 
plt.plot(points[:, 1], points[:, 2], 'r', linewidth = 1, label='sigma= ' + str(sigma) + '\nrho=' + str(rho) + '\nbeta' + str(beta))
plt.title("Lorenz system")
plt.legend(loc='best')
plt.xlabel('y')
plt.ylabel('z')
plt.grid()
plt.show()
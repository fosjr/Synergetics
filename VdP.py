import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tf = 50
tspan = np.arange(0, tf, 0.1)
init = [1, 1]

eps = [0.01, 0.1, 0.2, 0.5, 1, 1.5, 2]
sol = [0 for i in range(len(eps))]

#dxdt = y
#dydt = eps*(1-x**2)*y - x
for i in range(len(eps)):
    def pend(vect,  t):
        x, y = vect
        dvectdt = [y, eps[i]*(1-x**2)*y - x]
        #dvectdt = [i*(x - 1/3*x**3 - y), 1/i * x]
        return dvectdt

    sol[i] = odeint(pend, init, tspan)

    
plt.plot(sol[0][:, 0], sol[0][:, 1], 'k', linewidth = 0.3, label='eps = ' + str(eps[0]))
plt.plot(sol[1][:, 0], sol[1][:, 1], 'b', linewidth = 0.5, label='eps = ' + str(eps[1]))
plt.plot(sol[2][:, 0], sol[2][:, 1], 'y', linewidth = 0.6, label='eps = ' + str(eps[2]))
plt.plot(sol[3][:, 0], sol[3][:, 1], 'g', linewidth = 0.7, label='eps = ' + str(eps[3]))
plt.plot(sol[4][:, 0], sol[4][:, 1], 'r', linewidth = 0.7, label='eps = ' + str(eps[4]))
plt.plot(sol[5][:, 0], sol[5][:, 1], 'm', linewidth = 0.7, label='eps = ' + str(eps[5]))
plt.plot(sol[6][:, 0], sol[6][:, 1], 'c', linewidth = 0.9, label='eps = ' + str(eps[6]))
plt.title("Van der Pol equation")
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('x\'')
plt.grid()
plt.show()

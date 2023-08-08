import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k = 4
L = 10
xstart = 0
xstop = 20
ystart = -3
ystop = 10
xstep = 0.01
ystep = 0.2
linelength = 0.2

def dydx(t,y, k, L):
    # t is declared but never used to comply with scipy solve_ivp
    w = y[0]
    r = y[1]


    dwdt = r * w- w
    drdt = k*r * (1-r/L)-L/2*r*w


    return [dwdt,drdt]


x = np.arange(start=xstart, stop= xstop, step= xstep)
y = np.arange(start = ystart, stop = ystop, step=ystep)

sol1 = solve_ivp(dydx, [xstart,xstop],[0.3,1], args=(k,L), dense_output=True, max_step= 0.01,first_step = 0.01)
z = sol1.sol(x)
plt.plot(x, z.T, label=('100s of wolves', 'kilo-rabbits'))
plt.legend()


plt.title("Population of wolves W (100s of wolves) and Rabbits R (kilo-rabbits)")
plt.xlabel('t (years)')
plt.ylabel('amount of animals')
plt.show()
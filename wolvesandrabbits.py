import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k = 2
L = 2
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


    dwdt = -w + r * w
    drdt = k*r * (1-r/L)-L*r*w


    return [dwdt,drdt]


x = np.arange(start=xstart, stop= xstop, step= xstep)
y = np.arange(start = ystart, stop = ystop, step=ystep)

sol1 = solve_ivp(dydx, [xstart,xstop],[10,0.3], args=(k,L), dense_output=True, max_step= 0.01,first_step = 0.01)
z = sol1.sol(x)
plt.plot(x, z.T)



plt.title("Rate of rabbit and wolf population growth")
plt.xlabel('t (years)')
plt.ylabel('100s of animals')
plt.show()
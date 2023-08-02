import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k = 4
L = 5
xstart = 0
xstop = 2
ystart = 0
ystop = 10
xstep = 0.1
ystep = 0.2
linelength = 0.2

def dydx(t,R, k, L):
    # t is declared but never used to comply with scipy solve_ivp
    return k * R * ( 1 - R / L)

def slopefield( x, y,k, L,  linelenght):

    (x,y) = np.meshgrid(x,y)
    u = 1 # change in x
    v = dydx(0, y, k,L) # change in y
    r = np.power(np.add(1, np.power(v,2)),0.5) # for normalizing the vectors
    plt.quiver(x,y, 1/r, dydx(0,y, k, L)/ r, headwidth= 0, units = 'xy', scale=(1/linelenght), angles = 'xy' , color = '#ff4040')


x = np.arange(start=xstart, stop= xstop, step= xstep)
y = np.arange(start = ystart, stop = ystop, step=ystep)


sol1 = solve_ivp(dydx, [xstart,xstop],[0.2,2,8], args=(k,L), dense_output=True, max_step= 0.1,first_step = 0.1)
z = sol1.sol(x)
plt.plot(x, z.T)

slopefield(x, y, k,L,linelength)

plt.title("Rate of rabbit population growth over time")
plt.xlabel('t (years)')
plt.ylabel('R (kilo rabbits)')
plt.show()
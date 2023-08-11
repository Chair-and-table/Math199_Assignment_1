import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k = 3
L = -2
xstart = 0
xstop = 2
ystart = 0
ystop = 10
xstep = 0.1
ystep = 0.2
linelength = 0.3

def dwdr(r,w, k, L):
    return ((-w + r * w) / (k * r * ( 1- r/L) - L * r * w))

def dydx(t,R, k, L):
    # t is declared but never used to comply with scipy solve_ivp
    return k * R * ( 1 - R / L)

def slopefield( x, y,k, L,  linelenght):

    (x,y) = np.meshgrid(x,y)
    u = 1 # change in x
    v = dydx(0, y, k,L) # change in y
    r = np.power(np.add(1, np.power(v,2)),0.5) # for normalizing the vectors
    plt.quiver(x,y, u/r, dydx(0,y, k, L)/ r, headwidth= 0, units = 'xy', scale=(1/linelenght), angles = 'xy' , color = '#ff4040')


x_slopefield = np.arange(start=xstart, stop= xstop, step= xstep)
x_graph = np.arange(start = xstart, stop=xstop, step = xstep/10)

y = np.arange(start = ystart, stop = ystop, step=ystep)


sol1 = solve_ivp(dydx, [xstart,xstop],[0.2,2,8], args=(k,L), dense_output=True, max_step= 0.1,first_step = 0.1)
z = sol1.sol(x_graph)
plt.plot(x_graph, z.T, label=("0.2 kilo-rabbits start","2 kilo-rabbits start","8 kilo-rabbits start"))
plt.legend()

slopefield(x_slopefield, y, k,L,linelength)
plt.plot()

plt.title("Rabbit population dynamics  over time", fontsize = 20)
plt.xlabel('t (years)', fontsize = 15)
plt.ylabel('R (kilo-rabbits)', fontsize = 15)
plt.savefig('foo.png')
plt.show()
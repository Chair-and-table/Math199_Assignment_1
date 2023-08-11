import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k = 4
L = 5
xstart = 0
xstop = 2.5
ystart = 0
ystop = 1.5
xstep = 0.06
ystep = 0.06
linelength = 0.07
tstart = 0
tstop = 20


def dwdr(t,y, k, L):
    # t is declared but never used to comply with scipy solve_ivp
    w = y[0]
    r = y[1]


    dwdt = r * w- w
    drdt = k*r * (1-r/  L)-L*r*w

    return [dwdt,drdt]




def slopefield( r, w,k, L,  linelenght):
    (r,w) = np.meshgrid(r,w)
    u = r * w- w # change in x
    v = k*r * (1-r/L)-L*r*w # change in y
    R = np.power(np.add(np.power(u,2), np.power(v,2)),0.5) # for normalizing the vectors
    plt.quiver(r,w, v/R, u/R, units = 'xy', scale=(1/linelenght), angles = 'xy' , color = '#1e66f5')


r = np.arange(start=xstart, stop= xstop, step= xstep)
w = np.arange(start = ystart, stop = ystop, step=ystep)

sol1 = solve_ivp(dwdr, [tstart,tstop],[0.3,1], args=(k,L), dense_output=True, max_step= 0.01,first_step = 0.01)
slopefield(r, w, k, L,linelength)
plt.xlabel("Rabbits (kilo-rabbits)", fontsize = 15)
plt.ylabel("Wolves (100s of wolves)", fontsize = 15)
plt.title("Wolves against rabbits over time", fontsize = 20)
plt.plot(sol1.y[1],sol1.y[0],'-',lw=2, color = '#fe640b', label = ("Starts at (1 kilo-rabbit, 30 wolves) converges to (1 kilo-rabbit, 64 wolves) "))
plt.legend()
plt.show()
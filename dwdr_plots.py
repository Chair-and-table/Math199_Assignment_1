import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k = 4
L = 5
xstart = 0
xstop = 3
ystart = 0
ystop = 4
xstep = 0.1
ystep = 0.1
linelength = 0.1

def dwdr(t,y, k, L):
    # t is declared but never used to comply with scipy solve_ivp
    w = y[0]
    r = y[1]


    dwdt = r * w- w
    drdt = k*r * (1-r/L)-L/2*r*w


    return [dwdt,drdt]



#sol1 = solve_ivp(dwdr, [xstart,xstop],[1,0.3], args=(k,L), dense_output=True, max_step= 0.01,first_step = 0.01)




def slopefield( r, w,k, L,  linelenght):
    (r,w) = np.meshgrid(r,w)
    u = r * w- w # change in x
    v = k*r * (1-r/L)-L/2*r*w # change in y
    R = np.power(np.add(np.power(u,2), np.power(v,2)),0.5) # for normalizing the vectors
    plt.quiver(r,w, v/R, u/R, headwidth= 0, units = 'xy', scale=(1/linelenght), angles = 'xy' , color = '#ff4040')


r = np.arange(start=xstart, stop= xstop, step= xstep)
w = np.arange(start = ystart, stop = ystop, step=ystep)

slopefield(r, w, k, L,linelength)
#plt.plot(sol1.y[0],sol1.y[1],'-',lw=1 )
plt.show()
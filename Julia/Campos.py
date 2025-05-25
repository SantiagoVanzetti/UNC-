import matplotlib.pyplot as plt
import numpy as np
import vpython as vp

c= 4*np.pi*8.85e-12
k=1

def dip_pot(pos_q1,pos_q2,qt,r):
    phi=qt/c*(1/(vp.mag(r-pos_q1))-1/(vp.mag(r-pos_q2)))
    return phi

def dip_f(q,rq,ro):
    rt = ro-rq
    if rt==vp.vector(0,0,0):
        print("Estas dividiendo por 0")
    else:
        E = k*q*vp.norm(rt)/vp.mag(rt)**2
        return E

d = 1
lim = 2

x = np.linspace(-lim,lim,16)
y = np.linspace(-lim,lim,16)
#z = np.linspace(-5,5,10)

print(x)

pos_q1 = vp.vector(d,d,0)
pos_q2 = vp.vector(-d,d,0)
pos_q3 = vp.vector(d,-d,0)
pos_q4 = vp.vector(-d,-d,0)

q1 = 1
q2 = -1

for xt in x:
    for yt in y:
            ro = vp.vector(xt,yt,0)
            p = dip_f(q1,pos_q1,ro) + dip_f(q2,pos_q2,ro) + dip_f(q2,pos_q3,ro) + dip_f(q1,pos_q4,ro)
            color = vp.mag(p)*0.00001
            #print(color)
            plt.quiver(xt,yt,p.x,p.y,color)

plt.xlim(-lim,lim)
plt.ylim(-lim,lim)
plt.show()

#p = dipole_pot((1,0),(0,1),1)
#plt.quiver(x,p)

#print(vp.mod(1,1))
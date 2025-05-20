import matplotlib.pyplot as plt
import numpy as np

#x=np.cos(range(0,2*np.pi))
#y=np.sin(range(0,2*np.pi))
ax=plt.axes(projection="3d")

#plt.ion()
t=np.linspace(0,2*np.pi,500)
x_f=np.cos(2*t)
y_f=np.sin(2*t)
z_f=t
l=np.linspace(0,7,500)
eje_z=l

for i in np.linspace(0,2*np.pi,500):
    x=np.cos(2*i)
    y=np.sin(2*i)
    z=i
    ax.cla()
    ax.scatter(x,y,z,".",c="b")
    ax.plot(x_f,y_f,z_f,c="y")
    ax.plot(0, 0, eje_z, c="k")
    ax.set_xlim(-1.2,1.2 )
    ax.set_ylim(-1.2, 1.2)
    ax.set_zlim(0,7)
    plt.pause(0.01)
    ax.view_init(azim=45,elev=30)

#plt.ioff()
plt.show()
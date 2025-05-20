import matplotlib.pyplot as plt
import numpy as np

ax=plt.axes(projection="3d")

t=np.linspace(0,2*np.pi,500)
x_f=np.cos(2*t)
y_f=np.sin(2*t)
z_f=t
ax.scatter(x_f,y_f,z_f,c="y", linewidths=0.01)

plt.show()
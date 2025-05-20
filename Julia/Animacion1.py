import matplotlib.pyplot as plt
import numpy as np

x = 0
trayectoria = []

plt.ion()  # modo interactivo

for i in range(1000):
    x += np.random.normal(0, 1)  # paso aleatorio normal
    trayectoria.append(x)

    plt.clf()  # limpiar gráfico anterior
    plt.hist(trayectoria)
    plt.title(f"Paso {i}")
    plt.pause(0.01)

plt.ioff()
plt.show()


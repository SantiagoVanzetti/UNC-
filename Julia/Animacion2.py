import matplotlib.pyplot as plt
import numpy as np

print('¿ingresa los datos desde archivo (S/N)?')
respuesta=input()

if (respuesta=="S" or respuesta=="s"):
        print('Ingrese el nombre del archivo con los datos')
        archivo_datos=str(input())
        # Cargamos los datos completos en una matriz
        DATOS_todos = np.genfromtxt(archivo_datos, delimiter="")


        # Extraemos cada columna por separado en un vector
        x_dato = DATOS_todos[:,0]
        y_dato = DATOS_todos[:,1]
        #x_error = DATOS_todos[:,2]
        #y_error = DATOS_todos[:,3]

        nd = len(x_dato)
        print('Archivo leído')
        print('')
        print('Cantidad de datos=',nd)

for i in range(np.size(x_dato)):
    pasox=x_dato[i]
    pasoy=y_dato[i]
    if i==0:
        plt.plot(pasox,pasoy,"o", c="b")
    else:
        plt.plot(x_dato[:i+1],y_dato[:i+1],"-o", c="b")
    plt.title(f"Paso {i}")
    plt.xscale("log")
    plt.pause(0.2)
    plt.xlim(0.38,40)
    plt.ylim(0,1)
plt.ioff()
plt.show()
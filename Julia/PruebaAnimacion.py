import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from scipy.optimize import curve_fit,least_squares
from scipy import stats
from scipy.stats.distributions import  t

print('¿ingresa los datos desde archivo (S/N)?')
respuesta=input()

if (respuesta=="S" or respuesta=="s"):
        print('Ingrese el nombre del archivo con los datos')
        archivo_datos=str(input())
        # Cargamos los datos completos en una matriz
        DATOS_todos = np.genfromtxt(archivo_datos )


        # Extraemos cada columna por separado en un vector
        x_dato = DATOS_todos[:,0]
        y_dato = DATOS_todos[:,1]
        #x_error = DATOS_todos[:,2]
        #y_error = DATOS_todos[:,3]

        nd = len(x_dato)
        print('Archivo leído')
        print('')
        print('Cantidad de datos=',nd)

else:


        print('Ingrese el nombre del archivo donde va a grabar los datos')
        archivo_datos=str(input())

        nd = int(input('Ingrese la cantidad de datos: '))

        print('Ingrese los valores de la variable independiente (x_dato)=')
        x_dato=np.arange(nd,dtype=float)
        for i in range(nd):
            print('x[',i,']=', end= " ")
            x_dato[i] =float(input())

        print('Ingrese los errores de la variable independiente (x_error)=')
        x_error=np.arange(nd,dtype=float)
        for i in range(nd):
            print('x_err[',i,']=', end= " ")
            x_error[i] =float(input())

        print('Ingrese los valores de la variable dependiente (y_dato)=')
        y_dato=np.arange(nd,dtype=float)
        for i in range(nd):
            print('y[',i,']=', end= " ")
            y_dato[i]=float(input())

        print('Ingrese los errores de la variable dependiente (y_error)=')
        y_error=np.arange(nd,dtype=float)
        for i in range(nd):
            print('y_err[',i,']=', end= " ")
            y_error[i]=float(input())

        np.savetxt(archivo_datos, np.array([x_dato,y_dato,x_error,y_error]).T , delimiter="\tab" , fmt='%.5f')

print('Ingrese el numero de parametros (npar)=',end=" ")
npar = int(input())

print('Ingrese los valores de parámetros inciales (parametros_iniciales)=')
p_i=[]
for i in range(npar):
        print('p[',i,']=',end=" ")
        p = input()
        p=float(p)
        p_i.append(p)

def modelo(p,x):
    np.x=x 
    return (0.9104)*x/((x**2+(2*np.pi*p[1])**2*(x**2-p[0]**2)**2)**(1/2))
param_list=[]

def residuos(p, x, y, graficar=False):
    y_modelo = modelo(p, x)
    if graficar:
        fig, ax1 = plt.subplots()
        ax1.set_xscale('log')
        ax1.plot(x, y, 'o')
        ax1.plot(x, y_modelo, 'r-')
        plt.pause(0.01)
    return y_modelo - y

from functools import partial

res = least_squares(partial(residuos, graficar=True), p_i, method='trf', gtol=1e-8, args=(x_dato, y_dato))


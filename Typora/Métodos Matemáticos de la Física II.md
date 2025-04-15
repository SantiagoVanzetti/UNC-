# Métodos Matemáticos de la Física II

## Espacios lineales 

Un espacio vectorial (EV) o lineal es un conjunto de vectores $V=\{\vec v\}$ asociado a un cuerpo $\mathbb C$ que es **cerrado** bajo las operaciones de suma y el producto escalar que cumplan con las propiedades:

+ $(\vec a+\vec b)+\vec c=\vec a +(\vec b +\vec c)$
+ $\vec a+\vec b =\vec b+\vec a $
+ $\lambda(\vec a+\vec b)=\lambda\vec a+\lambda\vec b$
+ $(\lambda+\mu)\vec a=\lambda\vec a+\mu\vec a$
+ $\lambda(\mu\vec a)=\mu(\lambda\vec a)$
+ $\exists!\ \vec 0\in V:\vec a +\vec 0=\vec a\ \ \forall\vec a\in V$
+ $\exists ! \ 1\in \mathbb C: 1\cdot \vec a =\vec a\ \ \forall\vec a \in V$
+ $\forall\vec a \in V,\ \exists!(-\vec a ):\vec a +(-\vec a)=\vec 0$

#### Independencia Lineal

Un conjunto de $n$ vectores no nulos $\{\vec a\}_{i=1}^n$ es **linealmente independiente** (LI) si cumple que si $\sum \lambda_i\vec a_i=0 \Rightarrow \lambda_i=0\  \forall i$. Si un conjunto no es LI, es un conjunto **linealmente dependiente** (LD).

#### Dimensión

La dimensión es la cardinalidad del conjunto LI más grande que se puede formar en el EV. Se puede definir para dimensión finita como:
$$
dim(V)=\text{max}_{\mathbb N_0}\{n\in\mathbb N_0/\exists\{\vec x_i\}_{i=1}^n\sub V\ \text{LI}\}
$$

#### Base de un espacio vectorial

Si dim$(V)=n<\infty$ cualquier conjunto de $n$ vectores $\{\vec e_i\}\sub V$ LI es **base** de $V$, y los $\vec e_i$ son los vectores base.

**Teorema**: Sea dim$(V)=n<\infty$, $\{\vec e_i\}$ base de $V\Rightarrow \forall\vec x\neq\vec 0\in V,\ \exists!\{x^i\}\sub \C:\vec x=x^i\vec e_i$. 

#### Componentes de un vector 
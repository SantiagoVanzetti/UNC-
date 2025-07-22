# Hoja de ecuaciones Electromagnetismo I

## Ecuaciones de Maxwell 

**Ecuaciones de vinculo (o estáticas)**: $\newcommand{par}[2]{\frac{\partial #1}{\partial #2}}$$\newcommand{der}[2]{\frac{d#1}{d#2}}$

+ $\nabla\cdot \vec D=\rho$, Ley de Gauss para el campo eléctrico.

+ $\nabla\cdot\vec B=0$, Ley de Gauss para el campo magnético.

**Ecuaciones de evolución (o dinámicas)**:

+ $\nabla\times\vec E=-\par{\vec B}{t}$, Ley de Faraday.
+ $\nabla\times \vec H=\vec J+\par{\vec D}{t}$, Ley de Ampere-Maxwell.

**Ecuaciones de relaciones constitutivas**:

+ $\vec D=\varepsilon\vec E$ asociado con $\vec P$.
+ $\vec H=\frac{1}{\mu}\vec B$ asociado con $\vec M$.

**Fuerza de Lorentz**

+ $\vec F=q\vec E+q\vec v\times\vec B$

**Condiciones de empalme:**

+ $\hat{n}\cdot(\vec D_2-\vec D_1)=\sigma$
+ $\hat{n}\times(\vec E_2-\vec E_1)=0$
+ $\hat{n}\cdot(\vec B_2-\vec B_1)=0$
+ $\hat{n}\times(\vec H_2-\vec H_1)=\vec k$

$\bullet$ Suponemos para estas ecuaciones que nos encontramos en un medio homogéneo e isótropo,, y que las ecuaciones son lineales. Por lo que se vale el principio de superposición.

### Cambios de coordenadas

$\bullet$ Para todas las coordenadas curvilíneas vale:

+ $\nabla \cdot \vec F=\frac{1}{h_1h_2h_3}\bigg[\par{}{u_1}(h_2h_3F_1)+\par{}{u_2}(h_1h_3F_2)+\par{}{u_3}(h_1h_2F_3)\bigg]$
+ $\nabla\times\vec F=\frac{1}{h_1h_2h_3}\begin{array}{|c|}
  h_1\hat{e_1} & h_2\hat{e_2} & h_3\hat{e_3}\\
  \partial_1 & \partial_2 & \partial_3\\ 
  h_1F_1 & h_2F_2 & h_3F_3\\ 
  \end{array}$​

**Cartesianas**:

$\bullet$ Factores de escala: $h_i=1$
$\bullet$ $\nabla\cdot \vec V(x,y,z)= \partial_iV_i$

$\bullet\ \nabla\times\vec V(x,y,z)=
\begin{array}{|c|}
\hat{e_1} & \hat{e_2} & \hat{e_3}\\
\partial_1 & \partial_2 & \partial_3\\ 
V_1 & V_2 & V_3\\ 
\end{array}=\varepsilon_{ijk} \partial_jV_k\hat{e_i}$ 

**Cilíndricas**:

$\bullet$ Coordenadas: 

$x=r\cos(\theta)\\ y=r\sin(\theta)\\z=z$

$\bullet$ Factores de escala: $h_r=1,\ h_{\theta}=r,\ h_z=1$.
$\bullet$ Matriz de cambio de base de coordenadas cartesianas a cilíndricas $\mathbb{T}_c=\begin{bmatrix}\cos(\theta) & \sin(\theta) &0\\ -\sin(\theta) & \cos(\theta) & 0\\ 0&0&1\end{bmatrix}$, $\mathbb{T}_c\begin{bmatrix}v_x\\ v_y\\ v_z\end{bmatrix}= \begin{bmatrix}v_r\\ v_\theta\\ v_z\end{bmatrix}$

$\bullet$ $\boxed{\nabla \cdot \vec F(r,\theta,z)=\frac{1}{r}\par{}{r}(rF_r)+\frac{1}{r}\par{}{\theta}(F_\theta)+\par{}{z}(F_z)}$

 $\boxed{\nabla\times\vec F(r,\theta,z)=\frac{1}{h_1h_2h_3}
\begin{array}{|c|}
\hat{r} & r\hat{\theta} & \hat{k}\\
\par{}{r} & \par{}{\theta} & \par{}{z}\\ 
F_r & rF_\theta & F_z\\ 
\end{array}
=\bigg[\frac{1}{r}\par{}{\theta}(F_z)-\par{}{z}(F_\theta)\bigg]\hat{r} + \bigg[\par{}{z}(F_r)-\par{}{r}(F_z)\bigg]\hat{\theta} + \frac{1}{r}\bigg[\par{}{r}(rF_\theta)-\par{}{\theta}(F_r)\bigg]\hat{k}}$

**Esféricas**:

Coordenadas *($\varphi$ es el ángulo azimutal y $\theta$ es el ángulo polar)*:

$x=r\cos(\varphi)\sin(\theta)\\ y=r\sin(\varphi)\sin(\theta)\\ z=r\cos(\theta)$
$\bullet$ Factores de escala: $h_r=1,\ h_\varphi=r\sin(\theta),\ h_\theta=r$.

$\bullet$ Matriz de cambio de base de coordenadas cartesianas a cilíndricas $\mathbb{T}_e=\begin{bmatrix}\sin(\theta)\cos(\varphi) & \sin(\theta)\sin(\varphi) & \cos(\theta)\\ \cos(\theta)\cos(\varphi) & \cos(\theta)\sin(\varphi) & -\sin(\theta)\\ -\sin(\varphi) & \cos(\varphi) & 0 \end{bmatrix}$, $\mathbb{T}_e\begin{bmatrix}v_x\\ v_y\\ v_z\end{bmatrix}= \begin{bmatrix}v_r\\ v_\theta\\ v_\varphi\end{bmatrix}$
$\bullet$ $\boxed{\nabla \cdot \vec F(r,\theta,\varphi)=\frac{1}{r^2}\par{}{r}(r^2F_r)+\frac{1}{r\sin(\theta)}\par{}{\theta}[\sin(\theta)F_\theta]+\frac{1}{r\sin(\theta)}\par{}{\varphi}(F_\varphi)}$
$\bullet$ $\boxed{\nabla\times\vec F(r,\theta,\varphi)=\frac{1}{r^2\sin(\theta)}\begin{array}{|c|}
\hat{r} & r\hat{\theta} & r\sin(\theta)\hat{\varphi}\\
\par{}{r} & \par{}{\theta} & \par{}{\varphi}\\ 
F_r & rF_\theta & r\sin(\theta)F_\varphi\\ 
\end{array}}$
$\bullet$ $\boxed{\nabla\times\vec F(r,\theta,\varphi)=\frac{1}{r\sin(\theta)}\bigg[\par{}{\theta}(\sin(\theta)F_\varphi)-\par{}{\varphi}(F_\theta)\bigg]\hat{r}+\frac{1}{r}\bigg[ \frac{1}{\sin(\theta)}\par{}{\varphi}(F_r)-\par{}{r}(rF_\varphi)\bigg]\hat{\theta}+\frac{1}{r}\bigg[\par{}{r}(rF_\theta)-\par{}{\theta}(F_r)\bigg]\hat{\varphi}}$

#### Relaciones entre operadores diferenciales

+ $\nabla\cdot(\phi\vec a)=\phi(\nabla\cdot\vec a)+\vec a\cdot\nabla\phi$
+ $\nabla\times(\phi\vec a)=\phi(\nabla\times\vec a)+(\nabla\phi)\times\vec a$
+ $\nabla\cdot(\vec a\times\vec b)=\vec b\cdot (\nabla\times\vec a)-\vec a\cdot(\nabla\times\vec b)$
+ $\nabla\times(\vec a\times\vec b)=(\vec b\cdot\nabla)\vec a-(\vec a\cdot\nabla)\vec b+(\nabla\cdot\vec b)\vec a-(\nabla\cdot\vec a)\vec b$       ( $(\vec b\cdot \nabla)\vec a$ es la derivada direccional de $\vec a$ en la dirección de $\vec b$ )
+ $\nabla(\vec a\cdot\vec b)=(\vec a\cdot \nabla)\vec b+(\vec b\cdot \nabla)\vec a+\vec a\times(\nabla\times\vec b)+\vec b\times(\nabla\times\vec a)$
+ $\vec a \cdot(\vec b\times\vec c)=\vec b \cdot(\vec c\times\vec a)=\vec c \cdot(\vec a\times\vec b)$
+ $\vec a \times(\vec b\times\vec c)=(\vec a\cdot \vec c)\vec b-(\vec a\cdot \vec b)\vec c$
+ $\nabla\times(\nabla\times\vec a)=\nabla(\nabla\cdot\vec a)-\nabla^2\vec a$

#### Delta de Kronecker 

$\bullet$ $\delta_{ij}=\begin{cases}1 & \text{si}& i=j\\ 0 & \text{si}& i\neq j\end{cases}$

#### Símbolo de Levi-Civita

$\bullet$ $\varepsilon_{ijk}=\begin{cases}1& \text{si ijk es cualquier permutación par de 123}\\ 0& \text{si se repite indice}\\ -1& \text{si ijk es cualquir permutación impar de 123}\end{cases}$                ($i,j,k=1,2,3$)

$\bullet$ Se cumple: $\varepsilon_{ijk}\cdot\varepsilon_{kmn}=\delta_{im}\cdot\delta_{jn}-\delta_{in}\cdot\delta_{jm}$.















#### Teorema de Helmholtz 

$\bullet$ Dado un campo vectorial $\vec C$, puede ser escrito como la suma lineal de dos campos $\vec C=\vec C_\perp+\vec C_\parallel$ ;  tal que $\nabla \cdot\vec C_\perp=0$ y $\nabla\times \vec C_\parallel=0$. $\vec C$ no esta limitado. Con $\vec C_\perp=\nabla\times\vec F$ y $\vec C_\parallel=\nabla\phi\ \Rightarrow$ 
$$
\vec F=\frac{1}{4\pi}\iiint_V \frac{\nabla\times\vec C_\perp}{|\vec r-\vec r'|}d^3r'\\
\phi=\frac{1}{4\pi}\iiint_V \frac{\nabla\cdot\vec C_\parallel}{|\vec r-\vec r'|}d^3r'\\
\Rightarrow\ \vec C=\frac{1}{4\pi}\bigg[\nabla\times\bigg(\iiint_V \frac{\nabla\times\vec C_\perp}{|\vec r-\vec r'|}d^3r'\bigg)+\nabla\bigg(\iiint_V \frac{\nabla\cdot\vec C_\parallel}{|\vec r-\vec r'|}d^3r'\bigg)\bigg]
$$
$\bullet$ $\Large\phi(\vec x)=\frac{1}{4\pi\varepsilon_0}\iiint_V\frac{\rho(\vec x')}{|\vec x-\vec x'|}d^3x'$

## Funciones generalizadas

#### H de Heaviside

$\bullet$ $H(x)=\begin{cases}1 & \text{si}& x\geq0\\ 0&\text{si}&x<0\end{cases}$

$\bullet$ $H(x-x_0)=\begin{cases}1 & \text{si}& x\geq x_0\\ 0&\text{si}&x<x_0\end{cases}$

$\bullet$ Como $H$ se construye a partir de una serie de funciones diferenciables (funciones de soporte compacto diferenciable), por lo que se puede tener una noción de derivada de en $x_0$.
$\bullet$ $H$ es adimensional.

#### Distribución $\delta$ de Dirac

$\bullet$ Se devine como $\delta(x)=lim_{n\rightarrow\infty}\frac{n}{\sqrt{2\pi}}e^{-(x-x_0)^2n^2}$
$\bullet$ Cumple que: 
$$
\int^{\infty}_{-\infty}\delta(x)dx=1\\
\int^{\infty}_{-\infty}\delta(x-a)f(x)dx=f(a)\\
$$
 $\bullet$ $\delta$ en vectores $\delta(\vec r-\vec r_0)=\delta(x-x_0)\delta(y-y_0)\delta(z-z_0)$
$\bullet$ $[\delta]=\frac{1}{m},\ [\delta(\vec r)]=\frac{1}{m^3}$

$\bullet$ Propiedades:

+ $\delta(ax)=\frac{\delta(x)}{|a|}$
+ $\delta(g(x))=\sum_i\frac{\delta(x-x_i)}{|g'(x_i)|}$ con $g(x_i)=0$ y $g'$ no se anula nunca.
+ $\delta(\vec x-\vec x')=\frac{1}{h_1h_2h_3}\delta(x_1-x_1')\delta(x_2-x_2')\delta(x_3-x_3')$

## Ecuaciones de Poisson y Laplace

+ $\vec E=-\nabla\phi$
+ $\nabla^2\phi=-\frac{\rho}{\varepsilon_0}$

+ Solución para una carga puntual: $\phi(\vec r)=\frac{1}{4\pi\varepsilon_0} \frac{q}{|\vec r-\vec r_0|}$, tal que $\nabla^2\phi=-\frac{q}{\varepsilon_0}\delta(\vec r-\vec r_0)$.
+ Pues $\nabla^2\big(\frac{1}{|\vec r-\vec r_0|}\big)=-4\pi\delta(\vec r-\vec r_0)$

#### Igualdades de Green

Se usa que: 
$$
\nabla\cdot (\phi\nabla\psi)=\nabla \phi\cdot\nabla \psi+\phi\nabla^2\psi\tag{1}
$$
La primera identidad de Green se obtiene usando (1) y el teorema de la divergencia:
$$
\iiint_V(\nabla \phi\cdot\nabla \psi+\phi\nabla^2\psi)dV=\oiint_{\partial V}\phi\nabla\psi\cdot\vec {dS}\tag{2}\\
\iiint_V(\nabla \psi\cdot\nabla \phi+\psi\nabla^2\phi)dV=\oiint_{\partial V}\psi\nabla\phi\cdot\vec {dS}
$$
La segunda identidad de Green se obtiene restando las ecuaciones (2):
$$
\iiint_V(\phi\nabla^2\psi-\psi\nabla^2\phi)dV=\oiint_{\partial V}(\phi\nabla\psi-\psi\nabla\phi)\cdot\vec{dS}
$$
Tomando a $\phi$ como el potencial electrostático, por lo tanto $\nabla^2\phi=-\frac{\rho}{\varepsilon_0}$, y $\psi$ como una función $G(\vec x,\vec x')$ y le pedimos que $\nabla^2G=-4\pi\delta(\vec x,\vec x')$, tenemos:
$$
-4\pi \iiint_V\phi(\vec x')\ \delta(\vec x,\vec x')\ dV'+\iiint_V\frac{\rho(\vec x')}{\varepsilon_0}G(\vec x,\vec x')dV'=\oiint_{\partial V}\phi (\vec x')\nabla 'G(\vec x,\vec x')\cdot \vec{dS'}-\oiint_{\partial V}G(\vec x,\vec x')\nabla'\phi(\vec x')\cdot \vec{dS'}\\

\Rightarrow\ \phi(\vec x)=\frac{1}{4\pi}\iiint_V\frac{\rho(\vec x')}{\varepsilon_0}G(\vec x,\vec x')dV'-\frac{1}{4\pi}\oiint_{\partial V}\phi(\vec x')\nabla'G(\vec x,\vec x')\cdot \vec{dS'}+\frac{1}{4\pi}\oiint_{\partial V}G(\vec x,\vec x')\nabla'\phi(\vec x')\cdot \vec{dS'} \tag{3}
$$
$G$ tendrá la siguiente forma $G(\vec x,\vec x')=\frac{1}{|\vec x-\vec x'|}+F(\vec x,\vec x')$ con $\nabla^2F=0$, lo que se deduce de la forma de la solución general para el potencial de una carga puntual. Si se impone la **condición de Dirichlet** $\boxed{G_D(\vec x,\vec x')|_S=0}$:
$$
\Rightarrow\ \boxed{\phi(\vec x)=\frac{1}{4\pi\varepsilon_0}\iiint_V\rho(\vec x')G_D(\vec x,\vec x')dV'-\frac{1}{4\pi}\oiint_{\partial V}\phi(\vec x')\nabla'G_D(\vec x,\vec x')\cdot \vec{dS'}}\tag{4}
$$


La ecuación (4) permite deducir el potencial dentro de la región de interés conociendo su valor en el borde.

Si se utiliza la **condición de contorno de Neumann** $\boxed{\hat{n}\cdot \nabla'G_N(\vec x,\vec x')|_S=-\frac{4\pi}{S}}$ donde $S$ es el área del borde de la región de interés. Notar que no se puede tomar la condición $\hat{n}\cdot \nabla'G_N(\vec x,\vec x')|_S=0$ pues se contradice con la primer condición puesta sobre $G$, $\nabla^2G=-4\pi\delta(\vec x- \vec x')$. Tomando la condición de Neumann:
$$
\phi(\vec x)=\frac{1}{4\pi\varepsilon_0}\iiint_V\rho(\vec x')G_N(\vec x,\vec x')dV'+\frac{1}{S}\oiint_{\partial V}\phi(\vec x')dS'+\frac{1}{4\pi}\oiint_{\partial V}G_N(\vec x,\vec x')\nabla'\phi(\vec x')\cdot \vec{dS'}\\

\Rightarrow\ \boxed{\phi(\vec x)=\frac{1}{4\pi\varepsilon_0}\iiint_V\rho(\vec x')G_N(\vec x,\vec x')dV'+\phi_M+\frac{1}{4\pi}\oiint_{\partial V}G_N(\vec x,\vec x')\nabla'\phi(\vec x')\cdot \vec{dS'}}\tag{5}
$$
Donde $\phi_M$ es un promedio del potencial sobre el borde. Con la ecuación (5) se puede conocer $\phi$ a partir del valor de la derivada normal sobre $S$, es decir $\par{\phi}{N}\bigg|_S=\hat{n}\cdot \nabla\phi\big|_S$.

Es importante notar que la función $G$ **solo depende de la geometría** del borde de la región de interés, y no de las cargas sobre el borde. También hay que observar que la función $F(\vec x,\vec x')$ esta relacionada con la distribución de cargas en el exterior de la zona de interés, cosa que se verá mas adelante en el método de imágenes. 

Además, una vez encontrada una solución para un problema, con cualquiera de las dos condiciones, esta solución será única. Si suponemos que $\exist\phi_1,\phi_2$ soluciones con las mismas condiciones de contorno (Dirichlet o Neumann), tomo $\phi=\phi_1-\phi_2$ entonces $\nabla^2\phi=\nabla^2\phi_1-\nabla^2\phi_2=\frac{1}{\varepsilon_0}(-\rho+\rho)=0$. Luego remplazo ambos campos escalares de la primera igualdad de Green con $\phi$:
$$
\iiint_V(\phi\nabla^2\phi+\nabla\phi\cdot \nabla\phi)dV=\oiint_{\partial V}\phi\cdot(\hat{n}\cdot\nabla\phi)\ dS\\
\Rightarrow\iiint_V\nabla\phi\cdot\nabla\phi\ dV=0\\
\Rightarrow\nabla\phi=0\Rightarrow\phi=cte=\phi_1-\phi_2 
$$
Por lo que las soluciones son iguales salvo por una constante. En el caso de cumplir las condiciones de Dirichlet la constante será 0.

## Energía electrostática

La energía electrostática $U_E$ se define como el trabajo total requerido para formar una distribución de carga desde un estado inicial en el que las cargas están dispersas en el infinito. Nos imaginamos que estas cargas son traídas de forma cuasi-estática para que no ocurran efectos de disipación de energía asociados al campo magnético. Esto, además, asegura que el proceso sea reversible en términos termodinámicos.

Para una colección de N cargas puntuales se tiene que:
$$
U_E=W=\frac{1}{4\pi\varepsilon_0}\sum_{j=1}^N\sum_{i>j}^N\frac{q_iq_j}{|\vec r_i-\vec r_j|}\\
\Rightarrow \boxed{U_E=\frac{1}{4\pi\varepsilon_0}\frac{1}{2}\sum_{i=1}^N\sum_{j\neq i}^N \frac{q_iq_j}{|\vec r_i-\vec r_j|}=\frac{1}{2}\sum_{i=1}^Nq_i\phi(\vec r_i)} \tag{6}
$$
Para una distribución de carga $\rho(\vec r)$ se puede deducir que el diferencial de energía es:
$$
dU_E=\lambda\cdot\phi(\vec r)\cdot d\lambda\cdot dq=\lambda\cdot\phi(\vec r)\cdot d\lambda\cdot\rho(\vec r)\cdot dV
$$
La carga total en un dado momento será $\lambda\rho(\vec r)$ donde $\lambda$ es un numero real entre 0 y 1. Así $\lambda\phi(\vec r)$ es el potencial que se tiene, $dq=\rho(\vec r) dV$ es el diferencial de carga que se trae cuasi-estáticamente y $d\lambda$ es lo que aumenta este coeficiente al traer un diferencial de carga. Si se integra sobre todo el espacio:
$$
U_E=\iiint_VdU_E=\int_0^1\ \lambda d\lambda\iiint_V\rho(\vec r)\phi(\vec r)dV\\
\Rightarrow \boxed{U_E=\frac{1}{2}\iiint_V\rho(\vec r)\phi(\vec r)dV}\tag{7}
$$
Usando la ecuación de Poisson, $\vec E=-\nabla\phi$ y que $\nabla\cdot (\phi\nabla \phi)=\nabla\phi\cdot \nabla \phi+\phi\nabla^2\phi$ se obtiene que:
$$
U_E=-\frac{\varepsilon_0}{2}\bigg(\iiint_V\phi\ \nabla^2\phi\ dV\bigg)=\frac{\varepsilon_0}{2}\iiint_V\nabla\phi\cdot\nabla\phi\ dV-\frac{\varepsilon_0}{2}\iiint_V\nabla\cdot(\phi\nabla\phi)\ dV\\

\Rightarrow U_E=\frac{1}{2}\iiint_V\varepsilon_0\vec E\cdot\vec E\ dV+\frac{\varepsilon_0}{2}\iiint_V\nabla\cdot(\phi\vec E)\ dV\\

\Rightarrow U_E=\frac{1}{2}\iiint_V\varepsilon_0\vec E\cdot\vec E\ dV+\frac{\varepsilon_0}{2}\iint_{\partial V}\phi\vec E\cdot\vec{dS}
$$
Como la integral es sobre todo $\R^3$ y las cargas están localizadas por lo que $\phi\rightarrow0$ y $\vec E\rightarrow0$. Entonces, $\iint_{\partial V}\phi\vec E\cdot\vec{dS}=0$:
$$
\boxed{U_E=\frac{1}{2}\iiint_V\vec D\cdot \vec E\ dV}\tag{8}
$$
De la ecuación (8) se deduce que la energía electrostática es **definida positiva**. Y a partir de (8) se define la **densidad volumétrica de energía electrostática**:
$$
\boxed{\mathcal{U}_E=\frac{1}{2}\vec D\cdot \vec E}\tag{9}
$$
Para conseguir estas ecuaciones se supuso que se trataba con un medio lineal, homogéneo e isotrópico, pero valen para medios que no cumplan estas propiedades.

#### Sistema de conductores con cargas fijas 

Si se tienen N conductores con cargas fijas $Q_i$ y potencial $\phi_i$ sobre la superficie (o el interior) , la energía del sistema es:
$$
U_E=\frac{1}{2}\sum_{i=1}^NQ_i\phi_i\tag{10}
$$
 Se puede demostrar que en un sistema se mantiene la linealidad (como en los capacitores):
$$
Q_i=\sum_jC_{ij}\phi_j\\
\phi_i=\sum_jP_{ij}Q_J\tag{11}
$$
Donde los coeficientes $C_{ij}$ de capacitancia, y $P_{ij}$ coeficientes de potencial solamente dependen solamente de la geometría de cada conductor.
Las matrices $[C_{ij}]$ y $[P_{ij}]$ son simétricas, tienen la diagonal definida positiva (por la capacitancia propia), los demás elementos son negativos y se cumple que $\sum_jC_{kj}\geq0$. Además se cumple que $[C_{ij}]^{-1}=[P_{ij}]$.

Usando lo obtenido en (11) y remplazando en (10) se tiene que:
$$
U_E=\frac{1}{2}\sum_i^N\sum_j^NP_{ij}Q_iQ_j
$$
Entonces si quiero mover un conductor un $\vec{dR_1}$ en un sistema de conductores con carga constante:
$$
dU_E=-\vec F_{ext}\vec{dR_1}=-\vec F_{E}\vec{dR_1}\\
\Rightarrow dU_E=\frac{1}{2}\sum_i\sum_jQ_iQ_j\frac{dP_{ij}}{dR_1}\vec{dR_1}\\
$$
En el caso de un sistema con potenciales constantes se debe tener en cuenta la energía dada por las cargas que deben fluir para mantener $\phi$ constante. Por otro lado la expresión para la fuerza que el cuerpo 1 le ejerce al 2:
$$
\vec F_{12}=\iiint_{V_2}\rho_2(\vec x)\vec E_1dV
$$

## Condiciones de empalme

Se utilizarán las ecuaciones de Maxwell $\nabla\cdot\vec D=\rho$ y $\nabla\times\vec E=-\par{\vec B}{t}=0$, en electrostática, si bien esto simplifica las cuentas, no es una condición necesaria y valdrá lo mismo si $\par{\vec B}{t}$ no es nulo. Se toma un cilindro sobre la interfase, suficientemente pequeño para suponer que la superficie que separa los dos medios es plana y el desplazamiento sobre el cilindro es constante.

<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\Empalme1_page-0001.jpg" alt="Empalme1_page-0001" style="zoom:67%;" />
$$
\oiint_{\partial V}\vec D\cdot \vec{dS}=\vec D_1\cdot\vec{\Delta T_1}+\vec D_2\cdot\vec{\Delta T_2}+\sum_i\vec D_1\cdot\vec{\Delta_i S_1}+\sum_i\vec D_2\cdot\vec{\Delta_i S_2}=\iiint_V\rho dV\\

\Rightarrow \vec D_1\cdot\vec{\Delta T_1}+\vec D_2\cdot\vec{\Delta T_2}+\sum_i\vec D_1\cdot\vec{\Delta_i S_1}+\sum_i\vec D_2\cdot\vec{\Delta_i S_2}=\rho_{V_1}\Delta V_1+\rho_{V_2}\Delta V_2+\sigma\Delta T
$$
Donde $\sigma$ es la densidad de carga superficial en ambas partes de la interfase. Ahora tomo límite para el radio y longitud del cilindro, por lo que $\Delta T_i\rightarrow 0$, $\Delta S_i\rightarrow0$ y $\Delta V_i\rightarrow 0$; sabiendo que $\vec{\Delta S}=\Delta S\hat{n}$ se obtiene:
$$
\boxed{\hat{n}\cdot (\vec D_2-\vec D_1)\big|_S=\sigma}\tag{12}
$$
De la igualdad (12) se deduce que las componentes normales a la interfase de los campos solo son continuas si no hay cargas superficiales, en caso contrario existirá una discontinuidad.

Si se realiza un proceso similar utilizando la ley de Ampere con un camino $C$ rectangular, se deduce:

<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\Empalme2_page-0001.jpg" alt="Empalme2_page-0001" style="zoom:67%;" />
$$
\oint_C\vec E\cdot\vec{d\mathscr{l}}=0\\
\Rightarrow \hat{t}\cdot(\vec E_2-\vec E_1)=0 
$$
Donde $\hat{t}$ es el versor tangencial a la trayectoria, y por lo tanto tangente a la interfase. Si se escribe $\hat{t}=\hat{N}\times\hat{n}$ con $\hat{n}$ normal a la superficie:
$$
\boxed{\hat{n}\times(\vec E_2-\vec E_1)\big|_S=0}\tag{13}
$$
Por lo que **la componente tangencial de $\vec E$ siempre será continua**, a pesar de haber un cambio de medio.

## Método de imágenes

Se define **carga imagen** como una carga fuera de la región de interés que representa las cargas inducidas sobre el borde. La cual se relaciona con la función F de la función de Green. La idea del método es colocar cargas fuera de la región en la que se quiere resolver el problema de tal manera que las condiciones del borde se cumplan, y se resuelve el potencial para una carga puntual lo que es equivalente a calcular la función de Green. El potencial se calcula usando superposición, y una vos obtenida $G$ puede ser utilizada par cualquier problema con la misma geometría de borde usando (4) o (5).













#### Función de Green para un plano infinito 

Se toma el problema de una carga $q$ en el semi-espacio delimitado por el plano $xy$, si la carga se encuentra en la posición $\vec x'=(x',y',z')$, y se le impone la condición $\phi|_{z=0}=0$ (condición de Dirichlet sobre lo que mas adelante será $G$). Se puede resolver por método de imágenes suponiendo que hay una carga del otro lado del plano $xy$ en la posición $\vec x''=(x',y',-z')$, por superposición y conociendo el potencial de una carga puntual se tiene que:
$$
\phi(\vec x)=\frac{1}{4\pi\varepsilon_0}\bigg[\frac{q}{\sqrt{(x-x')^2+(y-y')^2+(z-z')^2}}-\frac{q}{\sqrt{(x-x')^2+(y-y')^2+(z+z')^2}}\bigg]
$$
<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\GreenPlanoinf_page-0001.jpg" alt="GreenPlanoinf_page-0001" style="zoom:25%;" />

Este potencial cumple que dentro de la región de interés $\nabla^2\phi=-\frac{q}{\varepsilon_0}\delta(\vec x-\vec x')$ lo cual es similar a lo que debe valer $\nabla^2G=-4\pi\delta(\vec x-\vec x')$. Si se propone que $\frac{q}{\varepsilon_0}=4\pi$ (por lo que $\frac{q}{4\pi\varepsilon_0}=1$) entonces se puede pensar que $G$ con la condición de Dirichlet, es el potencial de este sistema. Entonces para un el semi-espacio $z$ positivo (con borde igual al plano $xy$) la función de Green es:
$$
\boxed{G(\vec x,\vec x')=\bigg[\frac{1}{\sqrt{(x-x')^2+(y-y')^2+(z-z')^2}}-\frac{1}{\sqrt{(x-x')^2+(y-y')^2+(z+z')^2}}\bigg]}\tag{14}
$$
La cual cumple con:
$$
\nabla^2G=-4\pi\delta(\vec x-\vec x')\\
G\big|_S=0
$$
Notar que la función $F(\vec x,\vec x')=-\frac{1}{|\vec x-\vec x''|}$.
Esta solución para la función de Green valdrá para cualquier sistema que tenga como borde el plano $xy$.

Para calcular la densidad de carga que la carga induce sobre el plano se utiliza la condición de empalme (12) y se usa que el campo dentro del conductor $\vec D_2=0$:
$$
\sigma = -\hat{z}\cdot(-\varepsilon_0\vec E_1)=-\varepsilon_0\par{\phi}{z}\bigg|_S
$$























#### Función de Green para un esfera

Si se tiene una esfera con radio $a$ con una carga en su exterior $q$ a una distancia del centro $d$, y la esfera es un conductor conectado a masa, es decir que $\phi|_S=0$, se puede resolver el potencial en todo el espacio fuera de la esfera usando el método de las imágenes. Se supone que hay una carga imagen $q_i$ en el interior sobre el eje formado por el centro de la esfera y la posición de la carga $q$ (es razonable suponer esto por la simetría del problema), y esta carga $q_i $ esta a una distancia $e<a$ del centro de la esfera. 

<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\Green_esf_page-0001.jpg" alt="Green_esf_page-0001" style="zoom: 25%;" />

Utilizando superposición se puede resolver el problema para las dos cargas y usando la condición de contorno se calcula las incógnitas $q_i$ y $e$:
$$
\phi=\frac{1}{4\pi\varepsilon_0}\bigg[\frac{q}{|\vec x-d\hat{z}|}+\frac{q_i}{|\vec x-e\hat{z}|}\bigg]
$$
Sobre la superficie:
$$
\phi|_S=\frac{1}{4\pi\varepsilon_0}\bigg[\frac{q}{|\vec x-d\hat{z}|}+\frac{q_i}{|\vec x-e\hat{z}|}\bigg]=0\tag{15}
$$
Por lo tanto $q_i<0$ entonces escribiremos $-q_i$.

Usando que $|\vec x-d\hat{z}|^2=x^2+d^2-2dx\cos(\theta)$ y despejando de (15) se tiene:
$$
q^2[a^2+e^2-2ae\cos(\theta)]=q_i^2[a^2+d^2-2ad\cos(\theta)]\\
\Rightarrow\begin{cases}
q^2(a^2+e^2)=q_i^2(a^2+d^2)\\
2aeq^2=2adq_i^2
\end{cases}
$$
Del sistema de ecuaciones se calcula que:
$$
e=\frac{a^2}{d}\\
q_i=\frac{a}{d}q
$$
Entonces el potencial en la zona de interés es:
$$
\boxed{\phi(\vec x)=\frac{q}{4\pi\varepsilon _0}\bigg[\frac{1}{|\vec x-d\hat{z}|}-\frac{a}{d|\vec x-\frac{a^2}{d}\hat{z}|}\bigg]}\tag{16}
$$
Usando lo mismo que en el caso del plano $\frac{q}{4\pi\varepsilon_0}=1$, la función de Green para la geometría esférica:
$$
\boxed{G(\vec x,\vec x')=\frac{1}{|\vec x-\vec x'|}-\frac{a}{|\vec x'|}\frac{1}{|\vec x-\frac{a^2}{|\vec x'|^2}\vec x'|}}\tag{17}
$$









## Resolución de la Ecuación de Laplace utilizando separación de variables

Si se tiene la ecuación de Poisson $\nabla^2\phi=-\rho/\varepsilon_0$ con condición de contorno $\phi |_S=\chi(\vec x)$, se puede pensar que la solución será superposición de dos funciones $\phi_q$ y $\phi_p$ tal que $\phi=\phi_q+\phi_p$. El potencial $\phi_q$ corresponderá a la solución del potencial para la distribución de carga $\rho(\vec x)$ en todo el espacio y $\phi_p$ será un **potencial de "perturbación"** que hará cumplir la C.C. Si se piensa así estos dos potenciales cumplirán que:
$$
\phi_q=\frac{1}{4\pi\varepsilon_0}\iiint_V\frac{\rho(\vec x')}{|\vec x-\vec x'|}dV'\\
\Rightarrow \nabla^2\phi_q=-\frac{\rho}{\varepsilon_0}\tag{18}
$$
Por lo tanto:
$$
\nabla^2\phi_p=0\tag{19}
$$
Además $\phi_p$ debe cumplir las condiciones de contorno:
$$
\phi|_S=\phi_q|_S+\phi_p|_S\\
\Rightarrow \phi_p|_S=\phi|_S-\phi_q|_S=\chi-\phi_q|_S=\zeta(\vec x)\tag{20}
$$
Por lo tanto si se quiere resolver la ecuación de Poisson con condiciones de contorno basta con resolver:
$$
\nabla^2\phi=0\\
\phi|_S=\zeta(\vec x)\tag{21}
$$
Esta motivación para resolver la ecuación de Laplace valdrá de la misma forma si se tienen condiciones de Neumann.

### Separación de variables en coordenadas cartesianas

Se tiene que:
$$
\nabla^2\phi=\par{^2\phi}{x^2}+\par{^2\phi}{y^2}+\par{^2\phi}{z^2}=0\tag{22}
$$
Supondremos que $\phi$ tiene las siguiente forma (**método de separación de variables**):
$$
\phi(x,y,z)=X(x)Y(y)Z(z)\tag{23}
$$

$$
\Rightarrow\nabla^2\phi=X(x)Y(y)Z(z)\bigg[\frac{1}{X(x)}\der{^2X}{x^2}+\frac{1}{Y(y)}\der{^2Y}{y^2}+\frac{1}{Z(z)}\der{^2Z}{z^2}\bigg]=0\tag{24}
$$

Como cada sumando depende de una de las variables, cada uno debe ser una constante:
$$
\frac{1}{X(x)}\der{^2X}{x^2}=-\alpha^2\\\tag{25}
\frac{1}{Y(y)}\der{^2Y}{y^2}=-\beta^2\\
\frac{1}{Z(z)}\der{^2Z}{z^2}=\gamma^2
$$
Con la condición:
$$
\alpha^2+\beta^2=\gamma^2\tag{26}
$$
Entonces hay que resolver las tres ecuaciones diferenciales con las condiciones de contorno que le correspondan al problema:
$$
\der{^2X}{x^2}=-\alpha^2X(x)\\
\der{^2Y}{y^2}=-\beta^2Y(y)\\
\der{^2Z}{z^2}=\gamma^2Z(z)\tag{27}
$$


Si bien asumir que se puede hacer separación de variable en $\phi$ no es general nos servirá para primero obtener soluciones a cada ecuación diferencial de (27), con lo que obtendremos infinitas soluciones $X_\alpha(x)$, $Y_\beta(y)$ y $Z_{\alpha\beta}(z)$ ($\gamma$ depende de $\alpha$ y $\beta$ según (26)). A partir de estas soluciones las cuales serán ortogonales, es decir serán base del espacio de funciones en el intervalo de interés, podremos describir $\phi$ como combinación lineal de estas.

Ahora cada ecuación diferencial es un problema de autovalores de **Sturm-Liouville**:
$$
\mathcal L[\chi(x)]=-\alpha^2\chi(x)\tag{28}
$$
Para resolverlo tomaremos funciones que sean de **cuadrado integrable**, es decir que cumplan:
$$
\int_a^b f^*(\xi)f(\xi)d\xi<\infty\tag{29}
$$
También se necesita tener la noción de ortogonalidad entre las funciones, ya que se quiere encontrar una base a partir de los autovectores $\{\chi_\alpha\}$ ortogonal con la cuál se pueda describir $\phi$ y sea solución de la ecuación diferencial. Entonces, se define un **producto punto** y una **norma** asociada tal que:
$$
f(\xi)\cdot g(\xi)=\int_a^bf^*(\xi)g(\xi)d\xi\tag{30}
$$
Así puedo encontrar una base ortogonal, y dividiendo por constante una **base ortonormal** de tal forma que pueda escribir una función arbitraria $f$ en el intervalo $(a,b)$ de la siguiente forma:
$$
f(x)=\sum_{n=1}^\infty a_n\chi_n(x)\tag{31}
$$
**Nota**: si bien la base de los $\chi_\alpha$ tendrá infinitas autofunciones, la cantidad es numerable pues es base de las funciones en un intervalo finito. En el caso de que el intervalo fuese infinito, la base no sería discreta. Este intervalo estará dado por las condiciones de contorno del problema.

Ahora quiero encontrar los coeficientes $a_n$ que aproximen mejor a $f$. Para esto se debe minimizar la diferencia entre la aproximación y la función, entonces se minimiza la expresión:
$$
M_N=\int_a^b\bigg|f(\xi)-\sum_{n=1}^Na_n\chi_n(\xi)\bigg|^2d\xi\tag{32}
$$
 Derivando con respecto a cada $a_n$, y llevando $N\rightarrow\infty$ se obtiene que:
$$
\boxed{a_n=\int_a^bf(\xi)\chi_n^*(\xi)d\xi}\tag{33}
$$
**Nota**: los coeficientes $a_n$ son las proyecciones de $f$ en cada autofunción base.

Así remplazando en (31) se tiene que:
$$
f(x)=\sum_{n=1}^\infty\int_a^bf(\xi)\chi^*_n(\xi)\chi_n(x)d\xi\tag{34}\\
f(x)=\int_a^bf(\xi)\sum_{n=1}^\infty\bigg[\chi_n^*(\xi)\chi_n(x)\bigg]d\xi
$$
Para que la igualdad se cumpla entonces se debe cumplir que:
$$
\boxed{\sum_{n=1}^\infty\chi^*_n(\xi)\chi_n(x)=\delta(x-\xi)}\tag{35}
$$
Esta condición que encontramos para las autofunciones $\chi_n$ es la **relación de completitud**.

Ahora si tenemos una base del espacio de funciones en el intervalo $(a,b)$, por lo que podemos escribir cualquier función como combinación lineal de la base, cuyo elementos cumplirán condiciones de contorno tal que, junto con los coeficientes de la combinación lineal, permitan cumplir las condiciones de la función que queremos describir. Esto se hace para cada ecuación diferencial y tendremos:
$$
\phi_{\alpha\beta\gamma}=X_\alpha(x)Y_\beta(y)Z_\gamma(z)\tag{36}
$$
Así podremos escribir la solución general como combinación lineal de las soluciones de (36):
$$
\phi=\sum_{\alpha\beta}\phi_{\alpha\beta\gamma}\tag{37}
$$

Volviendo a las ecuaciones diferenciales de (27) las autofunciones que describirán el potencial serán:
$$
X_\alpha(x)=A_\alpha e^{i\alpha x}+B_\alpha e^{-i\alpha x}\\
Y_\beta(y)=C_\beta e^{i\beta y}+D_\beta e^{-i\beta y}\\
Z_\gamma(z)=E_\gamma e^{\gamma z}+F_\gamma e^{-\gamma z}\tag{38}
$$
La solución general se escribe remplazando en (37).

##### Problema: Cubo con una cara a potencial V

Si se tiene un cubo con aristas $a$ (en la figura $a=b=c$), tal que todas sus caras están conectadas a tierra, excepto la superior que tiene un potencial $V(x,y)$, y se quiere resolver el potencial dentro del cubo.

<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\Cuboelectro.png" alt="Cuboelectro" style="zoom: 50%;" />

Como quiero que las autofunciones cumplan las condiciones de contorno del problema elijo la forma de cada una de ellas para que así sea:
$$
X_\alpha(x)=D_\alpha\sin(\alpha x)\\
Y_\beta(y)=B_\beta\sin(\beta y)\\
Z_\gamma(z)=C_\gamma\sinh(\gamma z)\tag{39}
$$
Y se tiene la relación $\alpha^2+\beta^2=\gamma^2$.

De las condiciones de contorno:
$$
X_\alpha(a)=0\Rightarrow \alpha=\frac{m\pi}{a}, \ m\in\N\\
Y_\beta(a)=0\Rightarrow \beta=\frac{n\pi}{a},\ n\in\N\tag{40}
$$
La solución general:
$$
\phi=\sum_{n,m}^\infty\bigg[ A_{mn}\sin\bigg(\frac{m\pi}{a}x\bigg)\sin\bigg(\frac{n\pi}{a}y\bigg)\sinh(\gamma_{nm} z)\bigg]\tag{41}
$$
Los coeficientes $A_{mn}$ se obtienen imponiendo las condiciones de contorno. Utilizando las proyecciones de la función que describe a la C.C. (ecuación (33)). Las condiciones sobre todas las caras conectadas a masa ya se cumplen por la forma de las autofunciones. Ahora usando la condición sobre la cara superior:
$$
\phi|_{z=a}=\sum_m\sum_n A_{mn}\sin\bigg(\frac{m\pi}{a}x\bigg)\sin\bigg(\frac{n\pi}{a}y\bigg)\sinh(\gamma_{nm} a)=V(x,y)\tag{42}
$$
Ahora realizo la proyección en cada componente de la base y sustituyo $V$ usando (42):
$$
\int_0^a\int_0^a V(x,y) \sin\bigg(\frac{q\pi}{a}x\bigg)\sin\bigg(\frac{p\pi}{a}y\bigg)dxdy=\\

\sum_m\sum_n A_{mn}\sinh(\gamma_{mn} a) \int_0^a\int_0^a\sin\bigg(\frac{q\pi}{a}x\bigg)\sin\bigg(\frac{p\pi}{a}y\bigg)\sin\bigg(\frac{m\pi}{a}x\bigg)\sin\bigg(\frac{n\pi}{a}y\bigg)dxdy\tag{43}
$$
Se puede comprobar que:
$$
\boxed{\int_0^a\sin\bigg(\frac{q\pi}{a}x\bigg)\sin\bigg(\frac{m\pi}{a}x\bigg)dx=\frac{a}{2}\delta_{qm}}\\
\boxed{\int_0^a\sin\bigg(\frac{p\pi}{a}y\bigg)\sin\bigg(\frac{n\pi}{a}y\bigg)dy=\frac{a}{2}\delta_{pn}\tag{44}}
$$
Usando (44) en la ecuación (43):
$$
\int_0^a\int_0^a V(x,y) \sin\bigg(\frac{q\pi}{a}x\bigg)\sin\bigg(\frac{p\pi}{a}y\bigg)dxdy=\\
\sum_m\sum_n A_{mn}\sinh(\gamma_{mn} a) \bigg(\frac{a}{2}\bigg)^2 \delta_{qm}\delta_{pn}=A_{qp}\sinh(\gamma_{qp}a)\bigg(\frac{a}{2}\bigg)^2\tag{45}
$$






Entonces despejando y usando que $\gamma=\sqrt{\alpha^2+\beta^2}=\frac{\pi}{a}\sqrt{m^2+n^2}$:
$$
A_{mn}=\frac{4}{a^2}\frac{1}{\sinh(\pi\sqrt{m^2+n^2})}\int_0^a\int_0^a V(x,y) \sin\bigg(\frac{m\pi}{a}x\bigg)\sin\bigg(\frac{n\pi}{a}y\bigg)dxdy\tag{46}
$$
La solución final será:
$$
\phi=\sum_m^\infty\sum_n^\infty\bigg[ A_{mn}\sin\bigg(\frac{m\pi}{a}x\bigg)\sin\bigg(\frac{n\pi}{a}y\bigg) \sinh\bigg(\frac{\pi}{a} \sqrt{m^2+n^2}\cdot z\bigg)\bigg]\tag{47}
$$
Con coeficientes $A_{mn}$ escritos en (46).

### Separación de variables en coordenadas cilíndricas con simetría de traslación

En coordenadas cilíndricas:
$$
\nabla^2\phi(r,\varphi)=\frac{1}{r}\par{}{r}\bigg(r\par{\phi}{r}\bigg)+\frac{1}{r^2}\par{^2\phi}{\varphi^2}=0\tag{48}
$$
Se supone que:
$$
\phi=R(r)Q(\varphi)\tag{49}
$$
Remplazando (49) en (48) se obtiene:
$$
\frac{r}{R(r)}\par{}{r}\bigg(r\par{R}{r}\bigg)+\frac{1}{Q(\varphi)}\par{^2Q}{\varphi^2}=0\tag{50}
$$
Como cada sumando depende de una variable, cada término debe ser una constante. Se define que el primer termino es igual a $\nu^2$ y el segundo es $-\nu^2$, así se consiguen las siguientes ecuaciones diferenciales:
$$
\par{}{r}\bigg(r\par{R}{r}\bigg)=\nu^2\frac{R(r)}{r}\\\tag{51}
$$

$$
\par{^2Q}{\varphi^2}=-\nu^2Q(\varphi)\tag{52}
$$

Si $\nu=0$:
$$
Q_0(\varphi)=C+D\varphi\\
R_0(r)=A+B\ln (r)\tag{53}
$$
Si $\nu\neq0$ entonces, se puede resolver las ecuación (51) como una ecuación diferencial dimensionalmente consistente, y (52) tiene como solución una función armónica:
$$
Q_{\nu}(\varphi)=c_{\nu}\sin(\nu\varphi)+d_{\nu}\cos(\nu\varphi)\\
R_{\nu}(r)=a_\nu r^\nu+\frac{b_\nu}{r^\nu}\tag{54}
$$
Por lo tanto, la **solución general** de la ecuación de Laplace para coordenadas cilíndricas con simetría de traslación sobre el eje z es:
$$
\boxed{\phi(r,\varphi)=[A+B\ln (r)]\cdot(C+D\varphi)+\sum_{\nu=1}^\infty \bigg(a_\nu r^\nu+\frac{b_\nu}{r^\nu}\bigg)\cdot[c_{\nu}\sin(\nu\varphi)+d_{\nu}\cos(\nu\varphi)]}\tag{55}
$$

##### Problema:

Se tiene un cascarón cilíndrico infinito de radio $a$, concéntrico al eje $z$, a potencial $V(\varphi)=V_0\cos^2(\varphi)$. Se quiere calcular el potencial en al región interna. Por la simetría del problema se puede utilizar la ecuación (55). Como se requiere que la solución dentro sea regular (no diverja), se debe tener que $b_\nu=0$ siempre y $B=0$. El potencial sobre el cilindro debe ser periódico, por lo que $D=0$ y $\nu=m\in\N $. Entonces, la solución tendrá la forma:
$$
\phi=\sum_{m=0}^\infty r^m[A_m\sin(m\varphi)+B_m\cos(m\varphi)]
$$












Usando las condición de contorno:
$$
\phi\bigg|_{r=a}=V_0\cos^2(\varphi)=\sum_{m=0}^\infty a^m[A_m\sin(m\varphi)+B_m\cos(m\varphi)]\\
=\frac{V_0}{2}+\frac{V_0}{2}\cos(2\varphi)=\sum_{m=0}^\infty a^mA_m\sin(m\varphi)+\sum_{m=0}^\infty a^mB_m\cos(m\varphi)
$$
Por lo que $A_m=0\ \forall m$, y $B_m=0$ excepto para:
$$
B_0=\frac{V_0}{2}\\
a^2B_2=\frac{V_0}{2}
$$
Entonces:
$$
\phi=\frac{V_0}{2}+r^2\frac{V_0}{2a^2}\cos(2\varphi)
$$

### Separación de variables es coordenadas esféricas 

La ecuación de Laplace en esféricas:
$$
\nabla^2\phi=\frac{1}{r}\par{^2}{r}(r\phi)+
\frac{1}{r^2\sin(\theta)}\par{}{\theta}\bigg(\sin(\theta)\par{\phi}{\theta}\bigg)+
\frac{1}{r^2\sin^2(\theta)}\par{^2\phi}{\varphi^2}=0\tag{56}
$$
Si se supone:
$$
\phi=\frac{U(r)}{r}Q(\varphi)P(\theta)\tag{57}
$$
Remplazando (57) en (56):
$$
\nabla^2\phi=\frac{PQ}{r}\par{^2U}{r^2}+
\frac{UQ}{r^3\sin(\theta)}\par{}{\theta}\bigg(\sin(\theta)\par{P}{\theta}\bigg)+
\frac{UP}{r^3\sin^2(\theta)}\par{^2Q}{\varphi^2}=0\\

\Rightarrow0=\nabla^2\phi=\frac{1}{R\ r}\par{^2U}{r^2}+
\frac{1}{Pr^3\sin(\theta)}\par{}{\theta}\bigg(\sin(\theta)\par{P}{\theta}\bigg)+
\frac{1}{Qr^3\sin^2(\theta)}\par{^2Q}{\varphi^2}\\

\Rightarrow0=\nabla^2\phi=\frac{r^2\sin^2(\theta)}{R}\par{^2U}{r^2}+
\frac{\sin(\theta)}{P}\par{}{\theta}\bigg(\sin(\theta)\par{P}{\theta}\bigg)+
\frac{1}{Q}\par{^2Q}{\varphi^2}\\

\Rightarrow0=\nabla^2\phi=r^2\sin^2(\theta)\bigg[\frac{1}{R}\par{^2U}{r^2}+
\frac{1}{Pr^2\sin(\theta)}\par{}{\theta}\bigg(\sin(\theta)\par{P}{\theta}\bigg)\bigg]+
\frac{1}{Q}\par{^2Q}{\varphi^2}\\
$$
Entonces si:
$$
\frac{1}{Q}\par{^2Q}{\varphi^2}=-m^2\\
\Rightarrow r^2\sin^2(\theta)\bigg[\frac{1}{R}\par{^2U}{r^2}+
\frac{1}{Pr^2\sin(\theta)}\par{}{\theta}\bigg(\sin(\theta)\par{P}{\theta}\bigg)\bigg]=m^2\tag{58}
$$
Así se puede definir:
$$
\frac{m^2}{\sin^2(\theta)}-\frac{1}{P\sin(\theta)}\par{}{\theta}\bigg(\sin(\theta)\par{P}{\theta}\bigg)=l(l+1)\\
\Rightarrow \frac{r^2}{R}\par{^2U}{r^2}=l(l+1)\tag{59}
$$
Usando (58):
$$
P\bigg[l(l+1)-\frac{m^2}{\sin^2(\theta)}\bigg]+\frac{1}{\sin(\theta)}\par{}{\theta}\bigg(\sin(\theta)\par{P}{\theta}\bigg)\tag{60}=0
$$
Se realiza el cambio de variable $x=\cos(x)$ se puede demostrar que se obtiene:
$$
\der{}{x}\bigg((1-x^2)\der{P(x)}{x}\bigg)+\bigg[l(l+1)-\frac{m^2}{1-x^2}\bigg]P(x)\tag{61}=0
$$
Esta ecuación tiene como solución a los polinomios de Legendre $P_m^l(x)$.

#### Simetría acimutal

Si se tiene simetría acimutal $m=0$, entonces las soluciones son los polinomios de Legendre de a forma $P_l(x)$

**Polinomios de Legendre**:

Estos polinomios cumplen:

+ Si 𝑙 es par el polinomio es par.
+ Si $l$ es impar el polinomio es impar.

Los primeros polinomios de Legendre son:
$$
P_0(x)=1\\
P_1(x)=x\\
P_2(x)=\frac{1}{2}(3x^2-1)\\
P_3(x)=\frac{1}{2}(5x^3-3x)\\
P_4(x)=\frac{1}{8}(35x^4-30x^2+3)
$$


Fórmula de Rodrigues:
$$
P_l(x)=\frac{1}{2^ll!}\der{^l}{x^l}[(x^2-1)^l]\tag{62}
$$
Son ortogonales:
$$
\boxed{\int_{-1}^1P_l(x)P_n(x)dx=\frac{2}{2l+1}\delta_{lm}}\tag{63}
$$
Cumplen la siguiente relación de completitud:
$$
\boxed{\sum_l^\infty\frac{2l+1}{2}P_l(x)P_l(x')=\delta(x-x')}\tag{64}
$$
Cumplen que:
$$
P_{2k+1}(0)=0\\\tag{65}
P_{2k}(0)=(-1)^k\frac{(2k)!}{2^{2k}(k!)^2}
$$

$$
P_l(1)=1
$$

Se puede demostrar que para situaciones con simetría acimutal, la solución general para la ecuacion de Laplace es:
$$
\boxed{\phi(r,\theta)=\sum_{l=0}^\infty \bigg(a_l\ r^l+\frac{b_l}{r^{l+1}}\bigg) P_l[\cos(\theta)]}\tag{66}
$$

####  Solución general de la ecuación de Laplace en coordenadas esféricas

$$
\boxed{\phi(r,\theta,\varphi)=\sum_{l=0}^\infty\sum_{m=-l}^l \bigg(a_{lm}\ r^l+\frac{b_{lm}}{r^{l+1}}\bigg) \mathcal Y_{lm}(\theta,\varphi)}\tag{67}
$$

Tal que los **armónicos esféricos** son:
$$
\boxed{\mathcal Y_{lm}(\theta,\varphi)=\sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}}\ P_l^m[\cos(\theta)]\ e^{im\varphi}}\tag{68}
$$
Cumple que:
$$
\boxed{\mathcal Y_{l(-m)}(\theta,\varphi)=(-1)^m\mathcal Y^*_{lm}(\theta,\varphi)}\tag{69}
$$

**Relación de ortogonalidad:**
$$
\boxed{\iint \mathcal Y^*_{lm}(\theta,\varphi)\mathcal Y_{l'm'}(\theta,\varphi)\sin(\theta)d\theta d\varphi=\delta_{ll'}\delta_{mm'}}\tag{70}
$$
**Relación de completitud:**
$$
\boxed{\sum_{lm}^\infty\mathcal Y^*_{lm}(\theta',\varphi')\mathcal Y_{lm}(\theta,\varphi)=\delta(\varphi-\varphi')\delta(\cos(\theta)-\cos(\theta'))}\tag{71}
$$

#### Expansión de la función de Green en coordenadas esféricas

Se puede demostrar a través de calcular el potencial de una carga puntual usando separación de variables en coordenadas esféricas que:
$$
\boxed{\frac{1}{|\vec x-\vec x'|}=4\pi\sum_{l=0}^\infty\sum_{m=-l}^l\frac{1}{2l+1}\frac{r^l_<}{r^{l+1}_>}\mathcal Y_{lm}(\theta',\varphi')\mathcal Y_{lm}(\theta,\varphi)}\tag{72}
$$
Donde $r_>$ y $r_<$ son el mayor y el menor, respectivamente, entre $r$ y $r'$.

Usando la ecuación (17) y remplazando por la serie (72) se obtiene que la función de Green expandida en serie para coordenadas esféricas:
$$
G(\vec x,\vec x')=4\pi\sum_{l,m}\frac{1}{2l+1}\bigg[\frac{r^l_<}{r^{l+1}_>}-\frac{1}{a}\bigg(\frac{a^2}{rr'}\bigg)^{l+1}\bigg]\mathcal Y_{lm}(\theta',\varphi')\mathcal Y_{lm}(\theta,\varphi)\tag{73}
$$

### Ecuación de Laplace en coordenadas cilíndricas; funciones de Bessel

En coordenadas cilíndricas la ecuación de Laplace se puede escribir:
$$
\nabla^2\phi(r,\varphi,z)=\par{^2\phi}{r^2}+\frac{1}{r}\par{\phi}{r}+\frac{1}{r^2}\par{^2\phi}{\varphi^2}+\par{^2\phi}{z^2}=0\tag{74}
$$
Si se supone que:
$$
\phi(r,\varphi,z)=R(r)Q(\varphi)Z(z)\tag{75}
$$
Y se remplaza en (74):
$$
\frac{1}{r^2}\bigg(\frac{r^2}{R}\par{^2R}{r^2}+\frac{r}{R}\par{R}{r}+\frac{1}{Q}\par{^2Q}{\varphi^2}\bigg)+\frac{1}{Z}\par{^2Z}{z^2}\tag{76}=0
$$
Si se define:
$$
\frac{1}{Z}\par{^2Z}{z^2}=k^2\\
\frac{1}{Q}\par{^2Q}{\varphi^2}=-\nu^2\tag{77}
$$
Se obtiene la siguiente ecuación diferencial:
$$
\par{^2R}{r^2}+\frac{1}{r}\par{R}{r}+\bigg(k^2-\frac{\nu^2}{r^2}\bigg)R=0\tag{78}
$$
Claramente las ecuaciones de (77) tienen como solución:
$$
Z(z)=e^{\pm kz}\\
Q(\varphi)=e^{\pm i\nu\varphi}\tag{79}
$$
La ecuación (78) se puede llevar a la siguiente expresión:
$$
\der{^2R}{x^2}+\frac{1}{x}\der{R}{x}+\bigg(1-\frac{\nu^2}{x^2}\bigg)R=0\tag{80}
$$
Tiene como solución las funciones de Bessel que se construyen de la siguiente forma:
$$
R(x)=x^\alpha\sum_{J=0}^\infty a_jx^j\tag{81}
$$
Con $\alpha=\pm\nu$ y coeficientes con una relación de recurrencia:
$$
a_{2j}=\frac{(-1)^j\ \Gamma(\alpha+1)}{2^{2j }j!\ \Gamma(j+\alpha+)}a_0\tag{82}
$$
Se elije que $a_0=[2^\alpha\Gamma(\alpha+1)]^{-1}$, por lo que queda:
$$
a_{2j}=\frac{(-1)^j\ }{2^{2j }j!\ \Gamma(j+\alpha+)}\frac{1}{2^\alpha}\tag{83}
$$
Entonces, las funciones de Bessel de primera especie son:
$$
J_\nu(x)=\bigg(\frac{x}{2}\bigg)^\nu\sum_{j=0}^\infty\frac{(-1)^j}{j!\ \Gamma(j+\nu+1)}\bigg(\frac{x}{2}\bigg)^{2j}\\
J_{-\nu}(x)=\bigg(\frac{x}{2}\bigg)^{-\nu}\sum_{j=0}^\infty\frac{(-1)^j}{j!\ \Gamma(j-\nu+1)}\bigg(\frac{x}{2}\bigg)^{2j}\tag{84}
$$
Esas funciones son linealmente independientes si $\nu$ no es entero, si lo es ($\nu=m\in\Z$) son linealmente dependientes, de hecho se cumple:
$$
J_{-m}(x)=(-1)^mJ_m(x)\tag{84}
$$




Se debe encontrar una solución que sea LI para todo $\nu$. Esta es la función de Neumann:
$$
N_\nu(x)=\frac{J_\nu(x)\cos(\nu\pi)-J_{-\nu}(x)}{\sin(\nu\pi)}\tag{85}
$$
Por costumbre se usa la función de Neumann junto con la función de Bessel de primera especie para describir la solución a la ecuación diferencial (80) aunque $\nu$ no sea entero.

Para describir soluciones, también se definen las funciones de Henkel como combinación lineal de $J_\nu$ y $N_\nu$:
$$
H_\nu^{(1)}(x)=J_\nu(x)+iN_\nu(x)\\
H_\nu^{(2)}(x)=J_\nu(x)-iN_\nu(x)\tag{86}
$$
La función de Bessel, la de Neumann y las de Henkel cumplen la siguiente relaciones de recurrencia:
$$
\Omega_{\nu-1}(x)+\Omega_{\nu+1}(x)=\frac{2\nu}{x}\Omega_{\nu}(x)\\
\Omega_{\nu-1}(x)-\Omega_{\nu+1}(x)=2\der{}{x}\Omega_\nu(x)\tag{87}
$$
Si $\nu$ es real no negativo, el comportamiento de las funciones de Bessel y Neumann es el siguiente:

Si $x<<1$:
$$
J_\nu(x)\rightarrow\frac{1}{\Gamma(\nu+1)}\bigg(\frac{x}2\bigg)^\nu\\
N_\nu\rightarrow\begin{cases}\frac{2}{\pi}[\ln(\frac{x}{2})+...]\ \ \text{si }\ \nu=0\\ 
-\frac{\Gamma(\nu)}{\pi}(\frac{2}{x})^\nu\ \ \text{si }\ \nu\neq0
\end{cases}\tag{88}
$$
Si $x>>1$:
$$
J_\nu(x)\rightarrow\sqrt{\frac{2}{\pi x}}\cos(x-\frac{\nu\pi}{2}-\frac{\pi}{4})\\
N_\nu(x)\rightarrow\sqrt{\frac{2}{\pi x}}\sin(x-\frac{\nu\pi}{2}-\frac{\pi}{4})\tag{89}
$$
Las funciones de Bessel tienen infinitos ceros:
$$
J_\nu(x_{\nu n})=0\tag{90}
$$
Es el 0 número n. Para n muy grandes se cumple:
$$
x_{\nu n}\simeq n\pi+\bigg(\nu-\frac{1}{2}\bigg)\frac{\pi}{2}\tag{91}
$$
A partir de estos ceros se puede generar una familia de autofunciones ortogonales que pueden expandir el espacio de funciones, la familia de las $\{J_\nu(x_{\nu n} \frac{r}{a}\}$. De igual forma se puede hacer con las demás funciones definidas.

Existe una **relación de ortogonalidad** para estas autofunciones, la cual se puede luego extender de forma similar a las demás funciones:
$$
\boxed{\int_0^a J_\nu\bigg(x_{\nu n'}\frac{r}{a}\bigg)J_\nu\bigg(x_{\nu n}\frac{r}{a}\bigg)rdr=\frac{a^2}{2}[J_{\nu+1}(x_{\nu n})]^2\delta_{nn'}}\tag{92}
$$
Por lo que se puede expandir cualquier función en el intervalo $(0,a)$ como:
$$
f(r)=\sum_{n=1}^\infty A_{\nu n}J_\nu\bigg(x_{\nu n}\frac{r}{a}\bigg)\\
A_{\nu n}=\frac{2}{a^2J^2_{\nu+1}(x_{\nu n})}\int_0^arf(r)J_\nu\bigg(x_{\nu n}\frac{r}{a}\bigg)dr\tag{93}
$$
También cumplen la siguiente propiedad:
$$
\int_0^\infty xJ_m(kx)J_m(k'x)dx=\frac{1}{k}\delta(k-k')\tag{94}
$$
En caso de que las condiciones de contorno del problema requieran que haya senos o cosenos en la descripción del potencial en el eje z, se tiene que pedir la condición que $k^2<0$, por lo que $k$ será imaginario. Para este caso se deben usar las funciones $I$ y $K$ de Bessel:
$$
I_\nu(x)=i^{-\nu}J_\nu(ix)\\
K_\nu(x)=\frac{\pi}{2}i^{\nu+1}H^{(1)}_\nu(ix)\tag{95}
$$

## Desarrollo multipolar 

Si se desarrolla por serie de Taylor la función $|\vec r-\vec r'|^{-1}$. Si se desarrolla una función $f(x)$:
$$
f(x)=\sum_{n=0}^{\infty }\frac{f^{(n)}(x')}{n!}(x-x')^{(n)}\\
\Rightarrow\bigg[1+(x-x')\par{}{x}+(x-x')^2\par{^2}{x^2}+...\bigg]f(x)\bigg|_{x=x'} \\
$$
Se puede pensar como el operador:
$$
\sum_{n=0}^{\infty}\frac{1}{n!}\bigg(\varepsilon\par{}{x}\bigg)^n=e^{\varepsilon\par{}{x}}
$$
En tres dimensiones:
$$
f(\vec x+\vec \varepsilon)=e^{\vec \varepsilon\cdot \nabla}f(\vec x)\\\Rightarrow
f(\vec r-\vec r')=\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}(\vec r'\cdot\nabla)^nf(\vec r)
$$
Para lo cual $\varepsilon$ debe ser pequeño, por lo que $\vec r'=\varepsilon$ debe ser mucho mas pequeño que $\vec r$.  Utilizando esto se desarrolla:
$$
\frac{1}{|\vec r-\vec r'|}=\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}(\vec r'\cdot\nabla)^n\frac{1}{r}
$$
Así el potencial electrostático:
$$
\phi(\vec r)=\frac{1}{4\pi\varepsilon_0}\int _V\frac{\rho(\vec r')}{|\vec r-\vec r'|}d^3r'\\
\Rightarrow \phi(\vec r)=\frac{1}{4\pi\varepsilon_0}\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}\int_V\rho(\vec r')(\vec r'\cdot \nabla )^n\frac{1}{r}d^3r'
$$
Con esto se definen los multipolos:
$$
Q_{1..m}=\int_V\rho(\vec r')r_1'...r_m'd^3r'
$$
El primero llamada monopolo es la carga total:
$$
\int \rho d^3r=Q
$$
El segundo llamado dipolo:
$$
\vec p=\int_V\rho(\vec r')\vec r'd^3r'
$$

# Hoja de ecuaciones Electromagnetismo I

## Ecuaciones de Maxwell 

**Ecuaciones de vinculo (o estáticas)**: $\newcommand{par}[2]{\frac{\partial #1}{\partial #2}}$

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

$\bullet $ Tanto para coordenadas esféricas como para coordenadas cilíndricas, la matriz inversa es la **transpuesta**.

$\bullet$ $\boxed{\nabla \cdot \vec F(r,\theta,z)=\frac{1}{r}\par{}{r}(rF_r)+\frac{1}{r}\par{}{\theta}(F_\theta)+\par{}{z}(F_z)}$
$\bullet$ $\boxed{\nabla\times\vec F(r,\theta,z)=\frac{1}{h_1h_2h_3}
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

\Rightarrow\ \phi(\vec x)=\frac{1}{4\pi}\iiint_V\frac{\rho(\vec x')}{\varepsilon_0}G(\vec x,\vec x')dV'-\frac{1}{4\pi}\oiint_{\partial V}\phi(\vec x')\nabla'G(\vec x,\vec x')\cdot \vec{dS'}+\frac{1}{4\pi}\oiint_{\partial V}{\partial V}G(\vec x,\vec x')\nabla'\phi(\vec x')\cdot \vec{dS'} \tag{3}
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


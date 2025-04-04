# Hoja de ecuaciones Física General III

## Electrostática 

### Ley de Coulomb 

$$
\begin{align}
& \boxed{\vec{F}_{1,2}=\frac{k\cdot q_1\cdot  q_2}{r_{1,2}^2}\cdot \hat{r}_{1,2} }
&& \vec{F}_{1,2}=\text{Fuerza que el cuepo 1 le ejerce al cuerpo 2.}\\
&&& q_i=\text{cargas de los cuerpos.}  \\
&&& \vec{r}_{1,2}=\text{vector de posición de 1 a 2.} \\ 
\end{align}
$$

$\bullet \ k \equiv \text{constante de Coulomb}$.$\newcommand{dif}[1]{\mathrm{d}#1}$
$\bullet \ k=8,98755\cdot 10^{9}\frac{Nm^2}{C^2}=\large \frac{1}{4\pi \varepsilon_0}$
$\bullet \ \varepsilon_0\equiv \text{perimitividad en el vacío}$.
$\bullet \ \varepsilon_0= 8,85419\cdot 10^{-12}\frac{C^2}{Nm^2}$
$\bullet\ C\equiv Coulomb$. 

<img src="D:\Administrador\Escritorio\Typora\Typora Images\Coulombimg-page-001.jpg" alt="Coulombimg-page-001" style="zoom:67%;" />

##### Principio de superposición 

$\bullet$ En un sistema con múltiples cargas , la fuerza ejercida sobre una partícula ($X$), es la suma de las fuerzas $\vec{F}_{i,X}$:
$$
\vec{F}_{T}=k\cdot \sum_{i=0}^{n}\frac{q_X\cdot q_i}{r_{i,X}^2}\cdot \hat{r}_{i,X}
$$

##### Constantes 

$\bullet$ Las cargas están cuantizadas de la forma $q=ne : n\in \Z$ , tal que $e=1,6022\cdot 10^{-19}C$

$\bullet$ Carga del protón: $p^+=e$
$\bullet$ Carga del electrón: $e^-=-e$
$\bullet$ Carga del neutrón: $N^0=0$

$\bullet$ Masa del protón: $m_{p^+}=1,673\cdot 10^{-27}kg$
$\bullet$ Masa del electrón: $m_{e^-}=9,109\cdot 10^{-31}kg$
$\bullet$ Masa del neutrón: $m_{N^0}=1,675\cdot 10^{-27}kg$

#### Campo eléctrico

$\bullet$ $\vec{F}=q\cdot \vec{E}$
$\bullet$ $\vec{E}\equiv \text{Campo eléctrico},\ [E]=\large\frac{N}{C}$

##### Principio de superposición del campo

$$
\vec{E}_T(\vec{r})=k\cdot \sum_i\frac{q_i}{r_{i,0}^2}\cdot \hat{r}_{i,0}=k\cdot \sum_i\frac{q_i\cdot(\vec{r}_0-\vec{r}_i)}{|\vec{r}_0-\vec{r}_i|^3}
$$

<img src="D:\Administrador\Escritorio\Typora\Typora Images\SupDeE-page-001.jpg" alt="SupDeE-page-001" style="zoom:50%;" />

##### Líneas de campo 

$\bullet$ Son líneas continuas tangentes al campo, tal que la cantidad de líneas de campo por unidad de área esta asociada a la magnitud de $\vec{E}$. Estas tienen sentido de forma que apuntan desde cargas positivas hacia cargas negativas.

##### Campo de una densidad de carga 

$\bullet$ $\rho \equiv$ densidad de carga volumétrica.
$\bullet$ $\sigma \equiv$ densidad de carga superficial.
$\bullet$ $\lambda \equiv$ densidad de carga lineal.
$$
\begin{align}
\vec{E}=\iiint_V\frac{k\cdot \rho\cdot \hat{r}_p}{r_p^2}dV &&&& \vec{r}_p \equiv \text{vector desde el dV hasta la posición en la que se calcula el campo}
\end{align}
$$
<img src="D:\Administrador\Escritorio\Typora\Typora Images\esfera-page-001.jpg" alt="esfera-page-001" style="zoom:50%;" />

#### Flujo de campo eléctrico y Ley de Gauss

$\bullet$ $\Phi_E= \iint_S\vec{E}\cdot\vec{dA}$  
$\bullet$ Ley de Gauss para el campo eléctrico:
$$
\boxed{\large\Phi_E= \oiint \vec{E}\cdot \vec{dA}=\frac{q_{in}}{\varepsilon_0}} \\
\boxed{\large\Phi_E= \oiint \vec{E}\cdot \vec{dA}=\iiint_V \frac{\rho}{\varepsilon_0}\cdot dV} \\
$$
$\bullet$ De forma diferencial $\rightarrow \ \large \boxed{\nabla\cdot\vec{E}=\frac{\rho}{\varepsilon_0}}$

####  Energía y potencial eléctrico

$\bullet\ dW=q\cdot \vec{E}\cdot \vec{dS}=-dU$
$\bullet\ \Delta U=-q\cdot\int_i^f\vec{E}\cdot\vec{dS}$
$\bullet$ Se define el potencial eléctrico como $\large V=\frac{U}{q}, \ [V]=\frac{J}{C}=V\equiv Voltio$ 
$\bullet\ \boxed{\Delta V=-\int_i^f\vec{E}\cdot\ \vec{dS}}\ \Rightarrow\big[\vec{E}\big]=\large\frac{V}{m}$
$\bullet$ Se define el Electronvoltio como la energía de un electrón al moverse 1 voltio: $1\ eV=q_{e^-}\cdot1V=1,602\cdot 10^{-19}J$

$\bullet$ Potencial de una carga puntual: $V(\vec r)=\frac{kq}{r}$
$\bullet$ Potencial para N cargas: $V(\vec r)= k\sum_{i}^{N}\frac{q_i}{r_i}$
$\bullet$ Energía potencial para N cargas: $\large U_N=k\sum_{i=1}^N\sum_{j>i}^{N}\frac{q_iq_j}{r_{ij}}=\frac{k}{2}\sum_{i\neq j}^N\frac{q_iq_j}{r_{ij}} $

$\bullet$ Potencial para una densidad de carga:
$$
\boxed{V(\vec p)=k\iiint_V \frac{\rho \cdot dV}{r_p}}
$$
$\bullet$ Se cumple que: $\large \boxed{\vec E=-\nabla V}\ \Rightarrow \vec E$  es un campo conservativo $\Rightarrow\nabla\times\vec E=0$

#### Ecuación de Laplace y de Poisson

$\bullet$ Si en un punto del espacio $\vec p$ no hay carga se cumple la ecuación de Laplace $\rightarrow \ \boxed{\nabla^2V(\vec p)=0}$
$\bullet$ Si en un punto del espacio $\vec p$ hay una densidad de carga $\rho$ se cumple la ecuación de Poisson $\rightarrow\ \boxed{\nabla^2V(\vec p)=-\frac{\rho}{\varepsilon_0}}$

#### Capacitores/Condensador 

$\bullet$ $\large \boxed{Q=C\cdot \Delta V}$
$\bullet$ $C\equiv$ capacitancia o capacidad del condensador; $\big[C\big]=F=\frac{C}{V},\ F\equiv$ Faradio.

<img src="D:\Administrador\Escritorio\Typora\Typora Images\Capacitor_page-0001.jpg" alt="Capacitor_page-0001" style="zoom:50%;"/> 

$\bullet$ Notación en circuitos:

<img src="D:\Administrador\Escritorio\Typora\Typora Images\PartesdeCircuito_page-0001.jpg" alt="PartesdeCircuito_page-0001" style="zoom:67%;" />p .md-image:only-child{    width: auto;    text-align: inherit; } p >  

$\bullet$ Capacitancia de un capacitor de placas paralelas: $C=\frac{A\ \varepsilon _0}{d}$


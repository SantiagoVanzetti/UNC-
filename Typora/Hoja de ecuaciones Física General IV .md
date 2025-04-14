# Hoja de ecuaciones Física General IV

### Ondas

$\bullet$  Onda unidimensional cumple: $\psi(x,t)=f(x,t)=f(x\mp tv)$ (- en caso de que se propague en sentido positivo). $\newcommand{par}[2]{\frac{\partial #1}{\partial #2}}$

#### Ondas armónicas

$\bullet$ Son de la forma:
$$
\psi(x,t)=A\sin[k(x\mp vt)] \\ 
\psi(x,t)=A\cos[k(x\mp vt)]
$$
$\bullet$ $k\equiv$ número de onda, $[k]=m^{-1}$ (cantidad de ondas por unidad de longitud).
$\bullet$ $v\equiv$ velocidad de propagación, $[v]=m/s$ .
$\bullet$ $A\equiv$ amplitud (sus unidades dependen de la onda).

$\bullet$ $\lambda \equiv$ longitud de onda/ periodo espacial (distancia que recorre una perturbación en un ciclo).
$\bullet$ $\tau\equiv $ periodo temporal, $[\tau]=s$ (tiempo en el que la onda recorre una longitud de onda).
$\bullet$ $\nu\equiv$ frecuencia temporal, $[\nu]=s^{-1}=Hz$ (cantidad de perturbaciones que pasan por unidad de tiempo).
$\bullet$ $\omega\equiv $frecuencia angular, $[\omega]=\frac{rad}{s}$ .
$\bullet$ Estas definiciones valen para todas las ondas periódicas.

$\bullet$ Igualdades:
$$
\boxed{\lambda=\frac{2\pi}{k}}\\
\boxed{v=\frac{\lambda}{\tau}}\\
\boxed{v=\lambda\cdot\nu}\\
\boxed{v=\frac{\omega}{k}}\\
\boxed{\nu=\frac{1}{\tau}}\\
\boxed{\omega=2\pi\cdot\nu}\tag{1}
$$
$\bullet$ Usando las igualdades se puede escribir la función de una onda armónica como $\psi(x,t)=A\sin(kx\mp \omega t)$

##### Fase y velocidad de fase

$\bullet$ Se define $\phi\equiv$ fase como el argumento dentro del seno (o coseno): $\large{\phi=kx\mp\omega t+\varepsilon}$. Tal que $\varepsilon\equiv$ fase inicial.

$\bullet$ $\big( \par{\phi}{t}\big)_x=\mp\omega$

$\bullet$ $\big{(} \par{\phi}{x}\big)_t=k$

$\bullet$ $\big{(} \par{x}{t}\big)_\phi=\mp v$

#### Ecuación de onda 

$$
\boxed{\par{^2\psi}{t^2}=v^2\cdot\par{^2\psi}{x^2}}\tag{2}
$$



#### Superposición de ondas

$\bullet$ Superposición de ondas de igual frecuencia y velocidad, con $\alpha_i=k_ix+\varepsilon_i$ :
$$
E_1=E_{01}\cdot e^{i(\alpha_1-\omega t)}\\
E_2=E_{02}\cdot e^{i(\alpha_2-\omega t)}\\
E(x,t)=E_0\cdot e^{i(\alpha-\omega t)}=E_1+E_2\\
\Rightarrow\ \boxed{E_0^2=E_{01}^2+E_{02}^2+2E_{01}E_{02}\cdot\cos(\alpha_2-\alpha_1)}\\
\boxed{\tan(\alpha)=\frac{E_{01}\sin(\alpha_1)+E_{02}\sin(\alpha_2)}{E_{01}\cos(\alpha_1)+E_{02}\cos(\alpha_2)}}\tag{3}
$$



$\bullet$ Si $\alpha_1-\alpha_2=2\pi m$ están en fase y la interferencia es constructiva.
$\bullet$ Si $\alpha_1-\alpha_2=(2k+1)\pi$ es una interferencia destructiva.
$\bullet$ Si $\varepsilon_1-\varepsilon_2=cte$ las ondas son coherentes.

#### Ondas estacionarias

$\bullet$ Un punto de agarre, CC: $E_0[\sin(kx+\omega t)+\sin(kx-\omega t+\varepsilon_d)]_{x=0}=0\ \forall t \Rightarrow\ \varepsilon_d=2\pi m$.
$\bullet$ Nodo espacial $x_m=m\frac{\lambda}{2}$.
$\bullet$ Nodo temporal $t_m=(2m+1)\frac{\tau}{4}$ .

$\bullet$ Onda en una cavidad, CC: $E_0[\sin(kx+\omega t)+\sin(kx-\omega t+\varepsilon_d)]_{x,L =0}=0\ \forall t\Rightarrow \lambda_n=\frac{2L}{n}$ .

#### Ondas tridimensionales

$\bullet$ $\psi(\vec r,t)=A\sin(\vec k\cdot\vec r\mp \omega t)$, donde $\vec k\equiv$ vector de propagación de la onda.
$\bullet$ $|\vec k|\equiv$ número de onda, $|\vec k|=\frac{2\pi}{\lambda}$.
$\bullet$ Velocidad de fase o velocidad de propagación del frente de onda $\frac{dr_k}{dt}=\pm\frac{\omega}{t}=\pm v$.
$\bullet$ Ecuación de onda tridimensional:
$$
\large \boxed{\nabla^2 \psi=\frac{1}{v^2}\cdot \par{^2\psi}{t^2}}\tag{4}
$$

$\bullet$ Onda esférica $\psi(r,t)=(\frac{A}{r})\cdot e^{ik(r\mp vt)}$.

$\bullet$ El plano de vibración de una onda esta formado por la dirección de propagación y la dirección de la vibración.

### Ondas electromagnéticas

$\bullet$ $\large v=\frac{1}{\sqrt{\varepsilon\mu}}$, en el vacío $\large c=\frac{1}{\sqrt{\varepsilon_0\mu_0}}\approx 3\cdot 10^8m/s$.
$\bullet$ Constantes: $\varepsilon_0=8.854\cdot 10^{-12}\frac{C}{Vm},\ \mu_0=1,257\cdot 10^{-6}\frac{N}{A^2}$.

$\bullet$ Polarización lineal: si la onda no cambia de dirección de vibración.

Para una onda electromagnética con cualquier polarización vale que:

$\bullet$ $\vec E$ y $\vec B$ están en fase en todos lo puntos del espacio.
$\bullet$ $\vec E \perp \vec B$.
$\bullet$ $\vec E \times \vec B$ apunta en la dirección de propagación de la onda $\vec k$.
$\bullet$ $\boxed{E_0=v\cdot B_0}$

$\bullet$ Si $\vec E(x_i)\ (\vec B(x_i))$ $\Rightarrow\ E_{x_i}=0\ (B_{x_i}=0)$.

#### Energía y vector de Poynting

$\bullet$ Densidad de energía de los campos: $U_E=\frac{\varepsilon_0 E^2}{2}=U_B=\frac{B^2}{2\mu_0}$.
$\bullet$ Densidad de energía de la onda: $U=\varepsilon_0E^2=\frac{B^2}{\mu_0}$
$\bullet$ **Vector Poynting**: $\vec S=c^2\varepsilon_0\cdot \vec E\times\vec B$ (cantidad de energía por unidad de tiempo y área), $[|\vec S|]=\frac{W}{m^2s}$.
$\bullet$ **Irradiancia**: $I=\langle S\rangle_T=\frac{c^2\varepsilon_0}{2}\cdot \langle |\vec E\times \vec B|\rangle_T=\varepsilon_0c\cdot\langle E^2\rangle $ (vale solo para ondas polarizadas linealmente). $[I]=\frac{W}{m^2}$.
$\bullet$ Para cualquier medio: $I=v\varepsilon\langle E^2\rangle_T$

#### Presión de radiación

$\bullet$ Superficie perfectamente absorbente: $\lang P(t)\rang_T=\frac{I}{c}$.
$\bullet$ Superficie perfectamente reflectante: $\lang P(t)\rang_T=\frac{2I}{c}$

#### Luz en la materia

$\bullet$ $v=\frac{1}{\sqrt{\mu\varepsilon}}$.
$\bullet$ Índice de refracción absoluto: $n=\frac{c}{v}\geq 1$.
$\bullet$ Relación de Maxwell: (para $\mu=\mu_0$) $n=\sqrt{\frac{\varepsilon}{\varepsilon_0}}=\sqrt{K_E}$ .

### Propagación de la luz

$\bullet$ **Ley de reflexión**: el rayo incidente, la normal a la superficie y el rayo reflejado se encuentran en el mismo plano, llamado plano de incidencia. Además, se cumple $\sin(\theta_i)=\sin(\theta_r)$. 
$\bullet$ **Ley de refracción**: el rayo incidente, la normal a la superficie y el rayo refractado se encuentran en el mismo plano, llamado plano de incidencia. Además, se cumple la **Ley de Snell** $n_i\sin(\theta_i)=n_t\sin(\theta_t)$.
$\bullet$ Principio de reversibilidad: en un sistema da igual la dirección del rayo se mantienen los mismo ángulos.
$\bullet$ Al pasar de medio, la luz mantiene su frecuencia ($\nu=cte$). Entonces se cumple $\lambda_1=\frac{n_2}{n_1}\lambda_2$ .
$\bullet$ **Principio de Fermat**: los rayos de luz siguen la trayectoria que minimiza el tiempo o,equivalentemente, la trayectoria que minimiza la longitud del camino óptico.

$\bullet$ $LCO\equiv$ **Longitud de camino óptico**, se define como:
$$
LCO=\sum_{j=1}^N n_js_j\\
LCO=\int_S^Pn(s)ds
$$
Donde $n_j$ es el índice de refracción de las distintas fases y $s_j$ es la longitud que recorre en cada medio. La longitud de camino óptico se corresponde a la distancia que recorrería la luz en el vacío en el tiempo en que paso a través de los distintos medios, es decir, $LCO=ct$. También se puede ver como la longitud tal que en el vacío hay la misma cantidad de longitud de ondas que en el sistema. 

$\bullet$ La ley de reflexión y de Snell pueden ser deducidas a partir de las ecuaciones de Maxwell.

#### Ecuaciones de Fresnel

Las ecuaciones estarán dadas teniendo en cuenta la dirección del campo eléctrico en el punto de incidencia con respecto al plano de incidencia, y se supone que los medios son de permeabilidad magnética $\mu_0$. Además, los signos de las ecuaciones se relacionan con la dirección en la que se eligieron los campos (ver la deducción en el Hecht).

Si $\vec E$ es perpendicular al plano de incidencia:
$$
\boxed{r_\perp\equiv \bigg(\frac{E_{0r}}{E_{0i}}\bigg)_\perp=\frac{n_i\cos(\theta_i)-n_t\cos(\theta_t)}{n_i\cos(\theta_i)+n_t\cos(\theta_t)}=-\frac{\sin(\theta_i-\theta_t)}{\sin(\theta_i+\theta_t)}}\\

\boxed{t_\perp\equiv \bigg(\frac{E_{0t}}{E_{0i}}\bigg)_\perp=\frac{2n_i\cos(\theta_i)}{n_i\cos(\theta_i)+n_t\cos(\theta_t)}=\frac{2\sin(\theta_t)\cos(\theta_i)}{\sin(\theta_i+\theta_t)}}\tag{5}
$$
Donde $r$ es el **coeficiente de reflexión para la amplitud** y $t$ es el **coeficiente de transmisión para la amplitud**.

Si $\vec E$ es paralelo al plano de incidencia:
$$
\boxed{r_\parallel\equiv \bigg(\frac{E_{0r}}{E_{0i}}\bigg)_\parallel=\frac{n_t\cos(\theta_i)-n_i\cos(\theta_t)}{n_t\cos(\theta_i)+n_i\cos(\theta_t)}=\frac{\tan(\theta_i-\theta_t)}{\tan(\theta_i+\theta_t)}}\\

\boxed{t_\parallel\equiv \bigg(\frac{E_{0t}}{E_{0i}}\bigg)_\parallel=\frac{2n_i\cos(\theta_i)}{n_t\cos(\theta_i)+n_i\cos(\theta_t)}=\frac{2\sin(\theta_t)\cos(\theta_i)}{\sin(\theta_i+\theta_t)\cos(\theta_i-\theta_t)}}\tag{6}
$$
Si $n_t>n_i\Rightarrow\theta_i>\theta_t$. Cuando la incidencia es normal $\theta_i\sim0\Rightarrow \theta_t\sim0$, así se cumple:
$$
[r_\parallel]_{\theta_i=0}=[-r_\perp]_{\theta_i=0}=\frac{n_t-n_i}{n_t+n_i}
$$
Se cumple que:

+ $r_\perp<0\ \forall\ \theta_i\Rightarrow$ $E_{0r}$ y $E_{0i}$ están desfasadas en 180°.
+ $r_{\perp}>0$ para $\theta_i<\theta_p$.
+ $r_{\perp}<0$ para $\theta_i>\theta_p$.

Entonces en $\theta_i+\theta_t=90°\Rightarrow\ r_\parallel(\theta_p)=0$. Donde $\theta_p$ es el **ángulo de polarización o de Brewster**. Se puede demostrar:

+ $t_\perp-r_\perp=1\ \forall\theta_i$.
+ $t_\parallel+r_\parallel=1$ para $\theta_i=0$.

Si $n_t<n_i\Rightarrow\theta_i<\theta_t$. Entonces, se cumple:

+ $r_\perp>0\ \forall \theta_i\Rightarrow$ $E_{0r}$ y $E_{0i}$ están en fase.
+ $r_\perp(\theta_c)=1\ (\theta_t=90°)$.
+ $r_\parallel<0$ para $\theta_i<\theta'_p$.
+ $r_\parallel>0$ para $\theta_i>\theta'_p$.
+ $r_\parallel(\theta_c)=1$.
+ $\theta_p+\theta'_p=90°$.

#### Transmitancia y reflectancia

$\bullet$ Reflectancia $R\equiv\frac{I_r}{I_i}=\big(\frac{E_{0r}}{E_{0i}}\big)^2=r^2$
$\bullet$ Transmitancia $T\equiv\frac{I_t\cos(\theta_t)}{I_i\cos(\theta_i)}=\frac{n_t\cos(\theta_t)}{n_i\cos(\theta_i)}\big(\frac{E_{0r}}{E_{0i}}\big)^2=\frac{n_t\cos(\theta_t)}{n_i\cos(\theta_i)}t^2$

Por conservación de energía:
$$
T+R=1
$$
Se tiene además:

+ $R\perp=r^2_\perp$
+ $R\parallel=r^2_\parallel$
+ $T_\perp=\frac{n:t'cos(\theta_t)}{n_i\cos(\theta_i)}t^2_\perp$
+ $T_\parallel=\frac{n:t'cos(\theta_t)}{n_i\cos(\theta_i)}t^2_\parallel$

Si $\theta_i=0$:
$$
R=R\perp=R\parallel=\bigg(\frac{n_t-n_i}{n_t+n_i}\bigg)^2\\
T=T\perp=T\parallel=\frac{4n_tn_i}{(n_t+n_i)^2}
$$

## Óptica geométrica

$\bullet$ **Objeto**: cualquier cuerpo desde donde se irradia luz.
$\bullet$ **Imagen**: figura formada por los rayos emitidos por un objeto luego de interactuar con el sistema óptico. Puede ser **real**, si es formada por rayos que emite el objeto que se intersecan; o **virtual** si se forma desde donde parecen venir los rayos. 

### Espejos

#### Espejos planos

+ Imagen virtual: $s_i<0\ \Rightarrow\ s_i=-s_0$
+ Magnificación transversal $M_T=\frac{y'}{y}=1$

#### Espejos esféricos cóncavos o convergentes

+ Objeto e imagen reales $s_i, s_0>0$
+ $R>0$

Se utilizara la aproximación paraxial tal que el ángulo de incidencia sea muy pequeño. Así se puede deducir la ecuación para espejos, que vale para espejos convexos y cóncavos:
$$
\boxed{\frac{1}{s_0}+\frac{1}{s_i}=\frac{2}{R}}\tag{7}
$$
Tal que $R>0$ en cóncavos y $R<0$ en convexos.

Se define la **distancia focal objeto**:
$$
f_0=lim_{s_i\rightarrow\infty}s_0=\frac{R}{2}
$$
Y **distancia focal imagen**:
$$
f_i=lim_{s_0\rightarrow\infty}s_i=\frac{R}{2}
$$
Entonces:
$$
\boxed{\frac{1}{s_0}+\frac{1}{s_i}=\frac{1}{f}}\tag{8}
$$
Con $f>0$ para espejos cóncavos y $f<0$ para espejos convexos. Además $M_T=-\frac{s_i}{s_0}$, si $M_T>0$ la imagen es derecha y si $M_T<0$ la imagen estará invertida.

Para *espejos **cóncavos*** se tiene que:

+ Si $s_0>2f$ entonces $s_i>0$ , $f<s_i<2f$ y $-1<M_T<0\ \Rightarrow$ la imagen será ***real***, ***invertida*** y ***disminuida*** de tamaño.
+ Si $s_0=2f$ entonces $s_i=s_0$ y $M_T\ \Rightarrow$ imagen ***real***, ***invertida*** y del **mismo tamaño**.
+ Si $f<s_i<2f$ entonces $s_i>0$, $2f<s_i<\infty$ y $M_T<-1\ \Rightarrow$ imagen ***real***, ***invertida*** y ***aumentada***.
+ Si $s_0=f$ entonces no se forma imagen ya que $s_i=\pm\infty$.
+ Si $s_0<f$ entonces $s_i<0$, $|s_i|>s_0$ y $M_T>1\ \Rightarrow$ imagen **virtual**, ***derecha*** y ***aumentada***.

Para espejos ***convexos*** la imagen es siempre ***virtual*** ($s_i<0$), ***derecha*** y **disminuida**.

### Imágenes por refracción

Para un rayo que incide en una esfera de radio $R$ que cambia de un medio $n_1$ a $n_2$ se cumple que:
$$
\boxed{\frac{n_1}{s_0}+\frac{n_2}{s_i}=\frac{n_2-n_1}{R}}\tag{9}
$$
$$
\boxed{M_T=-\frac{n_1s_i}{n_2s_0}\tag{10}}
$$



Se usa la siguiente **convención de signo para superficies esféricas refractoras**:

+ $s_0>0$ objeto real.
+ $s_0<0$ objeto virtual.
+ $s_i>0$ imagen real.
+ $s_i<0$ imagen virtual.
+ $y, y'>0$, por encima del eje óptico.





Para **luz proveniente desde la izquierda**:

+  $R>0$ si el centro de curvatura ($C$) está a la derecha del vértice.
+  $R<0$ si el centro de curvatura ($C$) está a la izquierda del vértice.

Se define distancia focal objeto y distancia focal imagen como:
$$
\boxed{f_0=\frac{n_1}{n_2-n_1}R}\\
\boxed{f_i=\frac{n_2}{n_2-n_1}R}\tag{11}
$$

#### Superficies refractoras planas

+ $R\rightarrow\infty\ \Rightarrow s_i=-\frac{n_2}{n_1}s_0$
+ $s_i<0\ \forall s_0$, por lo que la imagen será virtual.
+ $M_T=1$

### Lentes

Un lente es un dispositivo refractor (un discontinuidad en el medio dominante) que reconfigura la distribución de energía emitida.

#### Tipos de lentes

Lente **simple**: dos superficies refractoras, una de ellas curva. La categoría opuesta es lente compuesta. 
Lente **delgada**: el espesor de la lente es despreciable con respecto a las demás dimensiones. La categoría opuesta es lente gruesa, en este caso se trata como dos superficies refractoras.
**Sistemas centrados de superficies esféricas**: las superficies son rotacionalmente simétricas alrededor de un eje.

Lentes **convexas**, convergentes o **positivas**.
Lentes **cóncavas**, divergente o **negativa**.

#### Ecuación de lentes delgadas

Esta ecuación se deduce a partir de tratar una lente convexa (con cóncava también sale) como dos superficies refractoras de radios $R_1$ y $R_2$, con un espesor $d$ y coeficientes del medio $n_m$ y del lente $n_l$. Se resuelve primero una superficie, y se toma la imagen formada como objeto de la segunda superficie y se resuelve, teniendo en cuenta la separación entre los vértices de ambas curvas.

Para la primer superficie usando (9) se obtiene:
$$
\frac{n_m}{s_{01}}+\frac{n_l}{s_{i1}}=\frac{n_l-n_m}{R_{1}}\tag{12}
$$
Para la segunda superficie describiendo las distancias desde $V_2$, tal que $s_{02}=d-s_{i1}$:
$$
\frac{n_l}{d-s_{i1}}+\frac{n_m}{s_{i2}}=\frac{n_m-n_l}{R_2}\tag{13}
$$
Si se suma (12) y (13) y $d\rightarrow0$ (pues es un lente delgado) se llega a la **ecuación de lentes delgadas** o formula del constructor de lentes:
$$
\boxed{\frac{1}{s_0}+\frac{1}{s_i}=\bigg(\frac{n_l}{n_m}-1\bigg)\bigg(\frac{1}{R_1}-\frac{1}{R_2}\bigg)}\tag{14}
$$

![image-20250401221859232](C:\Users\Administrador\AppData\Roaming\Typora\typora-user-images\image-20250401221859232.png)

#### Puntos y planos focales

Se llega a que el foco imagen y objeto son iguales $f=f_i=f_0$ con:
$$
\boxed{\frac{1}{f}=(n_{lm}-1)\bigg(\frac{1}{R_1}-\frac{1}{R_2}\bigg)}\tag{15}
$$
Con $n_{lm}=\frac{n_l}{n_m}$. A partir de (14) se puede escribir la **fórmula gaussiana para lentes delgadas**:
$$
\boxed{\frac{1}{s_0}+\frac{1}{s_i}=\frac{1}{f}}\tag{16}
$$
Se define potencia $P$ con unidades de Dioptrías $[P]=D$ y $P=\frac{1}{f}$

#### Lentes convergentes 

Este tipo de lente cumple que $f>0$:

+ Lente biconvexa: $R_1>0$ y $R_2<0$.
+ Lente plano-convexa: $R_1=\infty$ y $R_2<0.$
+ Lente menisco-convexa: $R_1>0$ y $R_2>0$ con $R_1<R_2$.













#### Lentes divergentes

Este tipos de lentes cumple que $f<0$:

+ Lente bicóncava: $R_1<0$ y $R_2>0$.
+ Lente plano-cóncava: $R_1=\infty$ y $R_2>0$.
+ Lente menisco-cóncava: $R_1>0$ y $R_2>0$ con $R_1>R_2$.

<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\types-of-lenses-based-on-the-curvature-of-two-optical-surfaces-including-converging-and-diverging-lenses-physics-illustration-vector.jpg" alt="types-of-lenses-based-on-the-curvature-of-two-optical-surfaces-including-converging-and-diverging-lenses-physics-illustration-vector" style="zoom:33%;" />

Hay que notar que debido a la fórmula (15) una lente que en un medio es convergente ($f>0$) si se cambia de medio esta puede llegar a comportarse como una lente divergente.

#### Convención de signos

<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\Convencion de signos.png" alt="Convencion de signos" style="zoom:67%;" />

#### Formación de imágenes con trazado de rayos

Para una lente **convergente**:

+ Un rayo paralelo al eje óptico pasa por el foco imagen.
+ Un rayo que pasa por el foco objeto pasa paralelo al eje óptico.
+ Un rayo que pasa por el vértice no cambia de dirección.







Para una lente **divergente**:

+ Un rayo paralelo al eje óptico parece venir del foco imagen.
+ Un rayo que va a pasar por el foco objeto pasa paralelo al eje óptico.
+ Un rayo que pasa por el vértice no cambia de dirección.

#### Imágenes formadas por lentes delgadas de objetos reales

<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\Captura de pantalla 2025-04-02 180544.png" alt="Captura de pantalla 2025-04-02 180544" style="zoom:150%;" />

#### Magnificación transversal

$$
\boxed{M_T=\frac{y_i}{y_o}=-\frac{s_i}{s_o}}\tag{17}
$$

Usando trigonometría se puede deducir la **fórmula de Newton**, definiendo $x_o=s_o-f$ y $x_i=s_i-f$ se cumple que:
$$
\boxed{x_ox_i=f^2}\tag{18}
$$

#### Magnificación longitudinal

Se define:
$$
M_L\equiv \frac{dx_i}{dx_o}\tag{19}
$$
Usando (18) y que $M_T=\frac{f}{s_i-f}$:
$$
\boxed{M_L=-\frac{x_i}{x_o}=-\frac{f^2}{x_o^2}=-\frac{x_i^2}{f^2}=-M_T^2}\tag{20}\\
\boxed{M_T=-\frac{f}{x_o}=-\frac{x_i}{f}}
$$

#### Objetos virtuales 

Para trazar los rayos en un sistema con un objeto virtual los rayos no salen del objeto si no que apuntan a él en un principio y luego cambian de dirección.

#### Aberraciones 

+ Aberraciones cromáticas: están dadas debido a que el coeficiente $n$ depende la longitud de onda.
+ Aberraciones monocromáticas: hay de dos tipos, primero aquellas que deterioran la imagen haciendo que esta pierda definición (aberración esférica, coma, astigmatismo); y aberraciones que deforman la imagen (campo de curvatura de Petzval y distorsión).

#### Combinación de lentes delgadas

Para resolver un sistema de varias lentes se resuelve una lente y se utiliza la imagen formada como objeto (real o virtual) de la siguiente lente. Para dos lentes se puede demostrar que:
$$
s_{i2}=\frac{f_2d-f_2\frac{s_{o1}f_1}{(s_{01}-f_1)}}{d-f_2-\frac{s_{o1}f_1}{(s_{01}-f_1)}}
$$
Usando que la distancias entre los lentes es $d$ y que por lo tanto la distancia imagen del 1 será el objeto de la siguiente lente de la siguiente forma:
$$
\boxed{s_{o2}=d-s_{i1}}\tag{21}
$$

#### Como graficar combinación de lentes

![Captura de pantalla 2025-04-06 184631](D:\Administrador\Escritorio\UNC-\Typora\Typora Images\Captura de pantalla 2025-04-06 184631.png)

Se extiende el rayo hasta el plano formado por el foco del siguiente lente, se une el punto de intersección con el vértice del siguiente lente y el rayo que saldrá de la segunda lente será paralelo a esta recta que une $A_i$ con $O$ .

#### Distancia focal posterior y frontal 

**Distancia focal frontal** ($dff$): es la distancia del vértice de la primer superficie hasta el primer punto focal.
$$
dff=lim_{s_{i2}\rightarrow\infty}s_{o1}
$$
Es la distancia la que se debe colocar el objeto para que los rayos salgan paralelos de la segunda lente.

**Distancia focal posterior** ($dfp$): es la distancia desde el vértice de la última superficie hasta el segundo punto focal.
$$
dfp=lim_{s_{o1}\rightarrow\infty}s_{i2}
$$
Es la distancia a la que se formara la imagen de la segunda lente si llegan rayos paralelos.

Se tiene que:
$$
\boxed{dfp=\frac{f_2(d-f_1)}{d-(f_1+f_2)}}\tag{22}
$$

$$
\boxed{dff=\frac{f_1(d-f_2)}{d-(f_1+f_2)}}\tag{23}
$$

Si $d=f_1+f_2$ entonces $dff$ y $dfp \rightarrow\infty$.

#### Lentes en contacto

En este caso se tiene que $d=0$, entonces:
$$
dff=dfp=\frac{f_1f_2}{f_1+f_2}
$$
En este caso la distancia focal efectiva del sistema es:
$$
\boxed{\frac{1}{f}=\frac{1}{f_1}+\frac{1}{f_2}}\tag{24}
$$
Se puede decir que se dos lentes están en contacto el sistema se comporta como una sola lente con distancia focal según la ecuación (24).

Si se generaliza el resultado para $N$ lentes en contacto con distancias focales $f_j$:
$$
\frac{1}{f}=\sum_{j=1}^N \frac{1}{f_j}
$$

#### Magnificación lateral en un sistema de dos lentes

Es el producto de las magnificaciones de cada lente
$$
M_T=M_{T1}M_{T2}\\
\Rightarrow M_T=\bigg(-\frac{s_{i1}}{s_{o1}}\bigg)\bigg(-\frac{s_{i2}}{s_{o2}}\bigg)\\
\Rightarrow M_T=\bigg(-\frac{f_1}{s_{o1}-f_1}\bigg)\bigg(-\frac{s_{i2}}{d-s_{i1}}\bigg)\\
\Rightarrow M_T=\frac{f_1s_{i2}}{d(s_{o1}-f_1)-s_{o1}f_1} 
$$

#### Diafragma de apertura y de campo

Diafragma de apertura (DA)(AS): determina la cantidad de luz que llega a la imagen.

Diafragma de campo (DC)(FS): determina el campo de visión de un instrumento.

#### Cámara fotográfica

Una cámara fotográfica forma una imagen real, invertida. y en general disminuida de tamaño.

La imagen adecuada es la energía por unidad de área que llega al detector la cuál debe de estar dentro de unos límites. Se puede demostrar que la irradiancia es proporcional a $\big(\frac{D}{f}\big)^2$ donde $D$ es el tamaño del diafragma y $f$ es el foco. Se define $\frac{D}{f}\equiv$ **apertura relativa**. Entonces:
$$
I\propto\bigg(\frac{D}{f}\bigg)^2\tag{25}
$$
También se define $f/\#=\frac{f}{D}$. Así una fotografía bien expuesta, es tal que le llega la cantidad de energía necesaria al sensor para formar una imagen:
$$
E=I\Delta t\propto\frac{\Delta t}{(f/\#)^2}\tag{26}
$$

#### Ojo humano

El ojo humano tiene dos elementos refractores, la cornea y el cristalino, y es equivalente a una lente delgada convexa de foco variable. Algunos conceptos importante relacionados con el ojo:

+ Acomodación: es el enfoque fino que realiza el cristalino.
+ Punto próximo: es el punto más cercano al que un ojo puede enfocar.

#### Miopía-Lente negativa

El ojo forma la imagen antes de la retina cuando los rayos le llegan paralelos. El punto lejano es el punto para el cual el ojo ya no puede enfocar, entonces se necesita que la lente forme una imagen virtual a una distancia menor. Para una lente de contacto se realiza el cálculo directo para la potencia que necesita la lente para formar una imagen antes del punto lejano. En el caso de lentes aéreos se toma como un sistema de dos lentes delgadas separadas por $d=16mm$.

#### Hipermetropía-Lente positiva

En este caso el punto próximo esta mas lejos de lo normal, por lo que se utiliza una lente positiva para formar una imagen virtual mas lejana, Usando los datos de $s_o$ y $s_i$ se calcula la potencia que debe tener la lente.













### Instrumentos ópticos

#### Lupa 

Es un instrumento que consiste de una **lente convergente** que aumenta el poder de refracción del ojo. Proporciona un **imagen virtual** de objetos más cercanos que el foco de la lente ($s_o<f$), lo que **genera una imagen derecha y aumentada**. Se define para la lupa el **aumento angular** ($M_A$) como el cociente entre el ángulo $\alpha_a$, sobre el ojo formado por la distancia hasta el ojo de la imagen y su altura, y $\alpha_u$ que sería el ángulo generado por el objeto y su distancia al ojo si no estuviese la lente, es decir:
$$
\boxed{M_A=\frac{\alpha_a}{\alpha_u}}
$$
Con ángulos tal que con aproximación paraxial:
$$
\tan(\alpha_a)\sim\alpha_a=\frac{y_i}{L}\\
\tan(\alpha_u)\sim\alpha_a=\frac{y_o}{d_o}\\
\Rightarrow M_A=-\frac{s_iL}{s_od_0}
$$
Con $L$ la distancia desde el ojo hasta la imagen formada y $d_0$ es la distancia al punto cercano del ojo.

Entonces, usando la ecuación para las lentes y que $l$ es la distancia del ojo a la lupa se obtiene:
$$
\boxed{M_A=\frac{d_0}{L}\bigg[1+\frac{1}{f}(L-l)\bigg]}\tag{27}
$$
Usando (27) se pueden ver tres casos interesantes:

+ Si la distancia del ojo a la lente es la misma que el foco de la lupa $f=l\Rightarrow M_A=\frac{d_0}{f}$.
+ Si la lupa esta pegada al ojo $l=0\Rightarrow M_A=d_0(\frac{1}{L}+\frac{1}{f})$, además si $L=d_0\Rightarrow M_A=1+\frac{d_0}{f}$ es el **máximo valor**.
+ Si el objeto esta sobre el foco de la lente $s_o=f\Rightarrow L=\infty \Rightarrow M_A=\frac{d_0}{f}\ \forall l$.

#### Microscopio compuesto

Es un instrumento que consiste de dos lentes colocadas sobre el mismo eje óptico, el primer lente al que entra luz desde el objeto se llama **lente objetivo** y el segundo **lente ocular**, y su objetivo es aumentar objetos cercanos a la lente objetivo (los rayos incidentes al sistema no serán paralelos). El lente objetivo crea una imagen necesariamente entre el foco de la lente ocular y la lente ocular para que este funcione como una lupa y termine magnificando el objeto. Por esto es que la magnificación de un microscopio es la magnificación transversal de la lente objetivo por el aumento angular de la lente ocular:
$$
\boxed{M_P=M_{To}M_{Ae}\tag{28}}
$$






En el caso en que la imagen de la primer lente se forme en el foco de la segunda $s_{oe}=f_e$ entonces por lo visto en la lupa $M_A=\frac{d_0}{f_e}$. Además, usando la ecuación (20) obtenida de la ecuación de Newton se tiene que si $L=x_{io}$ (como la imagen se forma sobre el segundo foco $L$ es la distancia entre los focos de ambas lentes), entonces $M_T=-\frac{L}{f_o}$. Para este caso:
$$
M_P=-\frac{Ld_0}{f_of_e}
$$

#### Telescopio 

Existen dos tipos de telescopios, los **telescopios refractores** los cuales son similares a los microscopios y utilizan un combinación de lentes, y los telescopios reflectores que usan un espejo curvo y una lente. La idea del telescopio es poder observar objetos grandes y distantes, por lo que **los rayos incidentes** al sistema serán siempre **paralelos**.

Para un telescopio refractor las lentes se llaman igual que las de un microscopio. En un **telescopio afocal** los rayos que inciden y salen del sistema son paralelos, solamente los cambia de dirección para poder magnificar la imagen. En este caso se cumple que $d=f_o+f_e$ donde $d$ es la distancia entre los lentes y es llamada la longitud del telescopio. 

Se define el aumento de manera similar al de un microscopio:
$$
\boxed{M_P=\frac{\alpha_a}{\alpha}}\tag{29}
$$
Donde $\alpha$ es el ángulo de incidencia de los rayos sobre el lente objetivo con respecto al eje óptico y $\alpha_a$ es el ángulo de salida de los rayos (salen paralelos) con respecto al eje óptico.

![Telescopio](D:\Administrador\Escritorio\UNC-\Typora\Typora Images\Telescopio.png)

Utilizando aproximación paraxial $\alpha=-\frac{\overline{BC}}{f_o}$ y $\alpha_a=\frac{\overline{DE}}{f_e}$, como $\overline{BC}=\overline{DE}$ se llega a:
$$
\boxed{M_P=-\frac{fo}{f_e}}\tag{30}
$$

#### Prismas 

Los prismas sirven como divisores de haces de luz, polarizadores e interferómetros. Hay dos tipos de prismas:

+ **Prisma dispersivo**: separa frecuencias constituyentes de la luz.
+ **Prisma reflectivo**: produce cambios en la orientación de la imagen o en la dirección de la luz.

#### Prisma dispersivo

Para un rayo de luz que atraviesa un prisma se define la **desviación angular** $\delta$ como el ángulo de diferencia entre el rayo incidente y el rayo que sale del prisma. Haciendo uso de geometría y la ley de Snell se tiene que:
$$
\delta=\theta_{i1}+\arcsin\bigg[\sin(\alpha)\sqrt{n^2-\sin^2(\theta_{i1})}-\cos(\alpha)\sin(\theta_{i1})\bigg]-\alpha\tag{31}
$$
<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\PrismaDispersor.png" alt="PrismaDispersor" style="zoom:50%;" />

Se puede demostrar que existe un ángulo de incidencia que minimiza $\delta$. Si se deriva (31) se iguala la derivada a 0 y se remplaza se obtiene que:
$$
\delta_m=2\cdot \arcsin\bigg[n\sin\bigg(\frac{\alpha}{2}\bigg)\bigg]-\alpha\tag{32}
$$
De (32) se deduce que para un prisma con índice $n$ y ángulo $\alpha$ sumergido en un medio $n'$ se tiene que:
$$
\boxed{\frac{n}{n'}=\frac{\sin\bigg[\frac{(\delta_m+\alpha)}{2}\bigg]}{\sin(\frac{\alpha}{2})}}\tag{33}
$$
En caso que $\delta$ sea mínimo se cumple que:
$$
\theta_{t1}=\theta_{i2}=\frac{\alpha}{2}
$$
Es decir el rayo cuya desviación es la mínima atraviesa el prima de forma paralela a la base.

Existen los llamados prismas de desviación constante que para cada $\lambda$ saldrá del prisma con una deviación distinta. 

#### Prisma reflector

El haz se hace incidir en el prisma de tal forma que se produzca al menos una reflexión total interna, con el propósito de cambiar la dirección de la luz.

Para un prisma isósceles se tiene que:
$$
\delta=2\theta_{i1}+\alpha	
$$
Por lo que la desviación angular no dependerá ni del índice del prisma ni de la longitud de onda de la luz, es un prisma acromático.

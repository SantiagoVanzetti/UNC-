# Hojas de ecuaciones de Métodos Matemáticos de la Física I

### Números complejos

$\bullet \ \large \mathbb{C}=\{ a,b \in \mathbb{R},\ a+i\cdot b \} \\$ 
$\bullet \ Re(z)=a$
$\bullet \ Im(z)=b$$\newcommand{der}[2]{\frac{\partial #1}{\partial #2}}$ 

#### Representación polar

$\bullet$ Módulo de un número complejo: $|a+i\cdot b|=\sqrt{a^2+b^2}$ 
$\bullet$ Argumento principal: $Arg(z)\in [-\pi ,\pi]$
$\bullet$ Representación polar: sea $Arg(z)=\alpha \Rightarrow \ z=|z|\cdot [\cos(\alpha)+i\cdot \sin(\alpha)]$ 
$\bullet$ Argumento: $arg(z)=\{ Arg(z)+2\pi \cdot n;\ n\in \mathbb{N} \}$

#### Propiedades de módulo y argumento

$\bullet \ -|z| \leq Re(z); Im(z) \leq |z|$
$\bullet \ |\bar{z}|=|z|$
$\bullet \ |z\cdot w|=|z|\cdot |w|$
$\bullet\ ||z_1|-|z_2||\leq |z_1\pm z_2|\leq |z_1|+|z_2|$
$\bullet \ |z_1 -z_2|\leq |z_1-z_3|+|z_2-z_3|$
$\bullet\ \sqrt{2} \cdot |z|\leq |Re(z)|+|Im(z)|$

$\bullet$ Conjugado: $\bar{z}=a-i\cdot b$ 
$\bullet \ z\cdot \bar{z}=|z|^2$
$\bullet \ arg(\bar{z})=arg(z)$
$\bullet\ arg(z_1\cdot z_2)=arg(z_1)+arg(z_2)$
$\bullet\ arg(\bar{z}\cdot z)=0$

$\bullet$ Exponencial: $exp(x+i\cdot y)=e^x\cdot (\cos(y)+i\cdot \sin(y))$

#### Raíces de números complejos 

$\bullet$ Lema: $\forall z \neq 0$  y  $\forall \ q\in \mathbb{N} ; \ q\geq 1, \ \ \exist q$ números complejos $w_k\ (0\leq k\leq q-1)$ tal que : 
$w_k^q=z$  con $|w_k|=\sqrt[q]{z}\ \ $y $$\large \ arg(w_k)=\frac{arg(z)+2\pi k}{q}$$ 

### Ecuaciones de Cauchy-Riemann

$\bullet \newcommand{der}[2]{\frac{\partial #1}{\partial #2}}$ Sea $f(z)=u+i\cdot v$ con $z=x+i\cdot y\ \Rightarrow \ u(x,y)\ \and \ v(x,y)$:
Las ecuaciones de Cauchy-Riemann son: $$\boxed{\der{u}{x}=\der{v}{y}\ ;\ \der{u}{y}=-\der{v}{x}}$$
$\bullet$ Si <u>no</u> se cumplen la ecuaciones en un abierto $\Rightarrow \ f$  no analítica en el abierto.
$\bullet$ Si se cumplen y las derivadas parciales son continuas en un abierto $\Rightarrow \ f$  es analítica en el abierto.
$\bullet$ Si se cumplen las ecuaciones pero las derivadas parciales no son continuas $\Rightarrow \ f$  no analítica.

#### Cauchy-Riemann en coordenadas polares

$\large\bullet\ \der{u}{x}=\der{v}{y}\ \and \der{u}{y}=-\der{v}{x}\Longleftrightarrow \der{u}{r}=\frac{1}{r}\cdot \der{v}{\theta} \and \frac{1}{r}\der{u}{\theta}=\der{v}{r}$ 

#### Laplaciano

$\large \bullet\ \nabla ^2f(x,y)=\der{^2f}{x^2}+\der{^2f}{y^2}$
$\large \bullet \ \nabla^2f(r,\theta)=r^2\cdot \der{^2f}{r^2}+r\cdot \der{f}{r}+\der{^2f}{\theta ^2}$

### Función exponencial

$\bullet$ Definición: $\large \exp(z)=\sum _{n=0}^{\infty}\frac{z^n}{n!}$

### Funciones trigonométricas 

$\bullet\ \large \sin(z)=\frac{e^{iz}-e^{-iz}}{2i}$
$\bullet \ \large \cos(z)=\frac{e^{iz}+e^{-iz}}{2}$

#### Inversas

$\bullet \ \sin^{-1}(z)=-i\cdot \ln(iz+(1-z^2)^{\frac12})$
$\bullet \ \cos^{-1}(z)=-i\cdot \ln(z+i\cdot (1-z^2)^{\frac12})$
$ \bullet \large \ \frac i2\cdot \ln(\frac{i+z}{i-z})$

### Funciones hiperbólicas 

$\bullet \large\ \large \sinh(z)=\frac{e^{z}-e^{-z}}{2}$
$\bullet \large \ \cosh(z)=\frac{e^{z}+e^{-z}}{2}$

### Integrales 

$\bullet$ Sea $f(t)=u(t)+i\cdot v(t), \ t \in \mathbb{R}\ \Rightarrow \ \int_a^bf(t)dt=\int_a^bu(t)dt+i\cdot \int_a^bv(t)dt$.
$\bullet$ Integración compleja: sea  $\gamma$ un camino suave tal que $\gamma =\{t\in [a,b]\rightarrow\ z(t)\}$ y una función $f$ a valores complejos, definida y continua sobre $[\gamma ]$ se define: $ \boxed{\int_\gamma f(z)\ dz= \int_a^bf(z(t))\ z'(t)\ dt}$ 

$\bullet$ Largo del camino: $\mathscr{l} (\gamma)= \int_{\gamma}|dz|$
$\bullet \ \boxed{\bigg|\int_{\gamma}f(z)\ dz\bigg|\leq max_{[z\in \gamma]}\big(|f(z|\big)\cdot \mathscr{l}(\gamma)}$ 

#### Primitiva 

$\bullet$ Teorema: si $\gamma$  es un camino cerrado con punto inicial $z_1$ y punto final $z_2$. Sea $f$ una función que admite primitiva $F$ en un abierto que contiene $[\gamma]\ \Rightarrow \boxed{\int_{\gamma}f(z)\ dz=F(z_2)-F(z_1)}$
$\bullet$ Proposición: sean $\gamma_1$ y $\gamma_2$ caminos cerrados simples, $[\gamma_1],\ [\gamma_2] \in D$ (Disco), $[\gamma_1]\sub D_1$ (Dominio encerrado por $[\gamma_1]$). Sea $A\sub D_1$ tal que su frontera es $[\gamma_1]\ \cup [\gamma_2]$. Si f es analítica en $A$ y su frontera $\Rightarrow \ \large \oint_{\gamma_1}f(z)\ dz=\oint_{\gamma_2}f(z)\ dz $.

#### Representación integral de Cauchy 

$\bullet$ Teorema: sea $f$ analítica en un disco $A$, y $\gamma$ un camino cerrado simple orientado positivamente, con $[\gamma]\sub A$. $\forall z_0\in \text{Dominio encerrado por } \gamma \Rightarrow \boxed{f(z_0)=\frac{1}{2\pi i}\cdot \oint_{\gamma}\frac{f(z)}{z-z_0}\ dz}$ ; y  $ \boxed{f^{(n)}(z_0)=\frac{n!}{2\pi i}\cdot \oint_{\gamma}\frac{f(z)}{(z-z_0)^{n+1}}\ dz}$ 
$\bullet$ Cotas de Cauchy: Sea $C$ un camino circular de radio $R$ tal que $f$ es analítica dentro de $C \Rightarrow$  $\big|f^{(n)}(z)\big|\leq \frac{n!}{R^n}\cdot max_{z\in C}(\big|f(z)\big|)$.

### Series de Laurent 

$\bullet$ Definición (serie de Laurent): 
$$
f(z)=\sum_{n=-\infty}^{\infty}c_n (z-z_0)^n=\sum_{n=1}^{\infty}c_{-n}(z-z_0)^{-n}+\sum_{n=0}^{\infty}c_n(z-z_0)^n \\
\ c_n= \frac{1}{2\pi i}\cdot \oint_{\gamma}\frac{f(z)}{(z-z_0)^{n+1}}\ dz
$$

#### Tipos de singularidades 

$\bullet$ Singularidad evitable: si $lim_{z\rightarrow z_0}f(z)\ \exist$.
$\bullet$ Polo de orden n: si  $lim_{z\rightarrow z_0}(z-z_0)^n\cdot f(z)\neq 0,\ \pm \infty$.
$\bullet$ Singularidad esencial: si la parte principal de la serie de Laurent es infinita.

#### Principio del argumento 

$\bullet$ Si f analítica y no se anula sobre la curva cerrada simple $\gamma \ \Rightarrow\large \frac{1}{2\pi i}\cdot \oint_{\gamma}\frac{f'(z)}{f(z)}\ dz=N_c(f)-N_p(f)$.
Tal que $N_c(f),\ N_p(f)$ son respectivamente la cantidad de ceros contando su orden y la cantidad de polos contando su orden que encierra $[\gamma]$.

#### Residuos 

$\bullet$ Definición:
$$
\bullet \ f(z)=\sum_{n=-\infty}^{\infty}c_n(z-z_0)^n\ \Rightarrow\ Res[f,z_0]=\frac{1}{2\pi i}\cdot \oint_Cf(z)\ dz= c_{-1}
$$
$\bullet$ Proposición: si en $z_0$ hay una singularidad aislada de $f$ de orden $n\ \Rightarrow$ $\boxed{Res[f,z_0]=lim_{z\rightarrow z_0}\frac{1}{(n-1)!}\cdot \frac{d^{n-1}}{dz^{n-1}}\bigg((z-z_0)^n\cdot f(z)\bigg)}$  

$\bullet$ Teorema de los residuos: $\boxed{\oint_{\gamma} f(z)\ dz=2\pi i\cdot \sum_{j=1}^{n}Res[f,z_j]}$

### Ecuaciones diferenciales ordinarias

#### Ecuaciones separables

$\bullet$ Se escriben de la forma: $A(x)\cdot dx+B(y)\cdot dy=0$
$\bullet$ Solución: se integran ambos términos.

#### Ecuaciones exactas 

$\bullet$ Se pueden escribir de la forma: $A(x,y)\cdot dx+B(x,y)\cdot dy=0$ con $A(x,y)=\lambda(x)\cdot \mu(y)\ \and\ B(x,y)=\alpha(x)\cdot\beta(y)\Rightarrow$ la ecuación es exacta.
$\bullet$ Si se cumple que $\large\der{A}{y}=\der{B}{x}\Rightarrow $ la ecuación es exacta.
$\bullet$ Solución: se integra como un campo en cualquier camino (la integral del campo obtenido no depende del camino).

#### Factor integrante 

$\bullet$ Si $A(x,y)\cdot dx+B(x,y)\cdot dy=0$  no es exacta puede $\exist\lambda(x,y)$ tal que $\lambda(x,y)\cdot A(x,y)\cdot dx+\lambda(x,y)\cdot B(x,y)\cdot dy=0$ <u>si</u> es exacta.
$\bullet$ Para una ecuación lineal de primer orden de la forma $y'+f(x)\cdot y=g(x)\Rightarrow \boxed{\large\lambda(x)=e^{\int f(x)\ dx}}$  

#### Cambios de variable 

###### Ecuación de Bernoulli: 

$$
y'+f(x)\cdot y=g(x)\cdot y^n \rightarrow \boxed{v=y^{1-n}}
$$

###### Ecuación de Clairaut:

$$
y-xy'=f(y')\rightarrow\text{se deriva con respecto a }x\rightarrow y''[f'(y')+x]=0
$$

###### Homogeneidad: 

$\bullet$ $f(x,y)$ es homogénea de grado $r$ si $f(ax,ay)=a^r\cdot f(x,y)\ \forall a$. 
$\bullet$ Una ecuación diferencial $A(x,y)\cdot dx+B(x,y)\cdot dy=0$ si $A$ y $B$ son homogéneas del mismo grado.
$\bullet$ Se remplaza en este caso $\boxed{y=vx}$

###### Generalización de la homogeneidad:

$\bullet$ Si $A(x,y)\cdot dx+B(x,y)\cdot dy=0$ es dimensionalmente consistente con:
$$
A(ax,a^my)=a^r\cdot A(x,y)\\
B(ax,a^my)=a^{r-m+1}\cdot B(x,y)
$$
$\bullet$ Se sustituye $\boxed{y=vx^m}$

#### Ecuaciones lineales a coeficientes constantes

$\bullet$ $a_ny^{(n)}+a_{n-1}y^{(n-1)}+...+a_1y^{(1)}+a_0y=f(x)$ 

###### Homogénea

$\bullet$ $a_ny^{(n)}+a_{n-1}y^{(n-1)}+...+a_1y^{(1)}+a_0y=0$. Este tipo de ecuaciones tienen $n$ soluciones $y_i$ linealmente independientes entre ellas  tal que la solución general es combinación lineal de las $y_i\rightarrow y=c_ny_n+c_{n-1}y_{n-1}+...+c_1y_1$. 





$\bullet$ Para resolver se propone $y=e^{mx}$ 
$$
\rightarrow a_nm^n+a_{n-1}m^{n-1}+...+a_1m+a_0=0 \\
\rightarrow\text{Se obtienen } m_i:\ i=1,...,n
$$
Si $m_i$ son todos distintos $\rightarrow y=c_ne^{m_nx}+c_{n-1}e^{m_{n-1}x}+...+c_1e^{m_1x}$
Si hay $m_i$ iguales se puede multiplicar por $x$ hasta que todas las soluciones $y_i$ sean $LI$ entre ellas.

$\bullet$ Para ver si dos funciones son $LI$ se define el Wronskiano:
$$
w(y_1,y_2)=det\bigg(\begin{bmatrix}y_1 & y_2\\ y'_1 & y'_2\end{bmatrix}\bigg)
$$
Si $w(y_1,y_2)\neq0 \Rightarrow y_1, y_2$ son $LI$.
Si $w(y_1,y_2)=0 \Rightarrow y_1, y_2$ son $LD$.

###### No homogénea 

$\bullet$ Se resuelve la ecuación homogénea, y luego se propone una solución particular $y_p$ dependiendo de la forma de $f(x)$.
$$
\begin{array}{|c|c|}\hline
f(x) & y_p\\ \hline
c & A\\ \hline
ax+b & Ax+b\\ \hline
ax^2+bx+c & Ax^2+Bx+C \\ \hline
ax^3+bx^2+cx+d & Ax^3+Bx^2+Cx+D\\ \hline
\sin(\mu x) & A\sin(\mu x)+B\cos(\mu x)\\ \hline
\cos(\mu x) & A\sin(\mu x)+B\cos(\mu x)\\ \hline
e^{\mu x} & Ae^{\mu x}\\ \hline
(ax+b)\cdot e^{\mu x} & (Ax+B)\cdot e^{\mu x}\\ \hline
(ax^2+bx+c)\cdot e^{\mu x} & (Ax^2+Bx+C)\cdot e^{\mu x}\\ \hline
e^{\lambda x}\cdot \sin(\mu x) & Ae^{\lambda x}\cdot\sin(\mu x)+Be^{\lambda x}\cdot\cos(\mu x)\\ \hline
\end{array}
$$

#### Variación de parámetros 

$\bullet$ Si se conocen las soluciones homogéneas de la ecuación $p(x)y''+q(x)y'+r(x)y=s(x)$, $y_1,\ y_2$:
$$
\boxed{y_p=A\cdot y_1+B\cdot y_2} \\
\boxed{A=-\int \frac{y_2(x)\cdot s(x)}{w(y_1,y_2)\cdot p(x)}\ dx}\\
\boxed{B=\int \frac{y_1(x)\cdot s(x)}{w(y_1,y_2)\cdot p(x)}\ dx}
$$

#### Reducción de orden

$\bullet$ Si se conoce una solución $y_1$ de la ecuación diferencial homogénea $y''+f(x)\cdot y'+g(x)\cdot y=0 \Rightarrow\ \boxed{y_2=z(x)\cdot y_1}$

#### Ecuaciones notables

$\bullet$ Ecuación de Legendre: $(1-x^2) y''-2x y'+\mathscr{l} (\mathscr{l}+1) y=0$
$\bullet$ Ecuación de Bessel: $x^2 y''+x y'+(x^2-\nu^2) y=0$
$\bullet$ Ecuación de Laguerre: $xy''+(1-x)y'+ay=0$
$\bullet$ Ecuación de Hermite: $y''-2xy'+2\alpha y=0$

#### Puntos singulares de una ecuación diferencial de segundo orden

$\bullet$ Dada la ecuación diferencial de segundo orden $y''+p(x)y'+q(x)y=0$
$\bullet$ Si $p(x_0)$  y  $q(x_0)$ son finitas $\Rightarrow x_0$ es un punto regular de la ecuación.
$\bullet$ Si $p(x)$  o  $q(x)$ divergen para $x \rightarrow x_0\ \Rightarrow x_0$ es un punto singular de la ecuación.
$\bullet$ Si $x_0$ es un punto singular y se cumple que  $lim_{x\rightarrow x_0} (x-x_0)\cdot p(x)\ \exist \ \and\ lim_{x\rightarrow x_0} (x-x_0)^2\cdot q(x) \ \exist \Rightarrow x_0$  es un punto singular regular.
$\bullet$ Si $x_0$ es un punto singular y $lim_{x\rightarrow x_0} (x-x_0)\cdot p(x)\ \nexists \ \or\ lim_{x\rightarrow x_0} (x-x_0)^2\cdot q(x) \ \nexists \Rightarrow x_0$ es un punto singular irregular.

### Método de Frobenius, solución en forma de serie

$\bullet$ Sea la ecuación diferencial de la forma $L[y]=x^2y''+x[x\ p(x)]y'+[x^2q(x)]y=0$ , tal que:
$$
\boxed{[x\ p(x)]=\sum_{n=0}^{\infty}p_nx^n}\\
\boxed{[x^2q(x)]=\sum_{n=0}^{\infty}q_n x^n}\\
\text{Se propone como solución: } \boxed{\phi=x^r\cdot \sum_{n=0}^{\infty}a_nx^n}
$$
$\bullet$ Para resolver, se plantea:
$$
\boxed{L[\phi]=\sum_{n=0}^{\infty}\big[(r+n)\cdot(r+n-1)\cdot a_n\cdot x^{n+r}\big]+\Bigg(\sum_{k=0}^{\infty}p_kx^k\Bigg)\cdot\Bigg[\sum_{n=0}^{\infty}(r+n)\cdot a_n\cdot x^{n+r}\Bigg]+
\Bigg(\sum_{k=0}^{\infty}q_kx^k\Bigg)\cdot\Bigg(\sum_{n=0}^{\infty}a_n\cdot x^{n+r}\Bigg)=0} \\
\rightarrow \boxed{L[\phi]=F(r)x^r+\sum_{n=1}^{\infty}\Bigg\{F(n+r)a_n+\sum_{k=0}^{n-1}a_k\bigg[(r+k)\cdot p_{n-k}+q_{n-k}\bigg]\Bigg\}\cdot x^{n+r}=0} \ \ (1)\\ \\
\text{Se define:}\ \ \boxed{F(r+n)=(r+n)(r+n-1)+p_0\cdot (r+n)+q_0}
$$


$\bullet$ Para calcular se plantea que por $(1)$ cada término debe ser idénticamente igual a 0.  
$\bullet$ Para $n=0 \Rightarrow F(r)=0$, asi se calculan $r_1$  y  $r_2$ , con  $\boxed{r_1 \leq r_2}$. 
$\bullet$ Con los demás términos se obtiene la siguiente relación de recurrencia, con la cuál se obtienen los $a_n$ :
$$
\boxed{a_n(r_1)=-\frac{\sum_{k=0}^{n-1}a_k\cdot \Big[(r_1+k)\cdot p_{n-k}+q_{n-k}\Big]}{F(r_1+n)}}
$$
$\bullet$ Así la primera solución obtenida es $\large y_1=x^{r_1}\cdot \sum_{n=0}^{\infty}a_nx^n$.

#### Segunda solución 

$$
\bullet \ \text{Si}\ \ r_1=r_2\Rightarrow \boxed{y_2=y_1\cdot ln(x)+x^{r_1}\cdot \sum_{n=0}^{\infty}b_nx^n}\\
\bullet \ \text{Si}\ \ r_1-r_2\in\N\Rightarrow\ \boxed{y_2=y_1\cdot\gamma\cdot ln(x)+x^{r_2}\cdot \sum_{n=0}^{\infty}b_nx^n}\\
\bullet\ \text{Si}\ \ r_1-r_2\notin\N \Rightarrow \boxed{y_2=x^{r_2}\cdot \sum_{n=0}^{\infty}b_nx^n}
$$

$\bullet$ Se remplazan estas expresiones en la ecuación y se calculan $\gamma$  y  $b_n$ .

### Series de Fourier

$$
\boxed{f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\big[a_n\cdot \cos (nx)+b_n\cdot \sin(nx)\big]}\\
\boxed{a_n=\frac{1}{\pi}\int_0^{2\pi}f(x)\cdot \cos(nx)\ dx}\\
\boxed{b_n=\frac{1}{\pi}\int_0^{2\pi}f(x)\cdot \sin(nx)\ dx}
$$

#### Condiciones de Dirichlet

$\bullet$ La serie de Fourier converge a $f$ si cumple las siguiente condiciones:
$\bullet$ $f(x)$ tiene un número finito de discontinuidades finitas en el intervalo de periodicidad.
$\bullet$ $f(x)$ tiene un número finito de valores extremos (máximos y mínimos) en el intervalo de periodicidad.





$\bullet$ Las sumas parciales convergen en media:
$$
lim_{n\rightarrow \infty}S_n(x_0)=\frac{f(x_0^+)+f(x_0^-)}{2}\\
\text{con}\ f(x_0^{\pm})=lim_{\delta\rightarrow0^{\pm}}f(x_0+\delta)
$$
$\bullet$ Se puede escribir el desarrollo de Fourier haciendo uso de números complejos:
$$
\boxed{f(x)=\sum_{n=-\infty}^{\infty}c_ne^{inx}} \\
\ \ \ \ \ \ \ \text{con}\ \ \boxed{c_n=\frac{1}{2}(a_n-i\cdot b_n)} \ \ \text{si} \ n>0\\
\boxed{c_{-n}=\frac{1}{2}(a_n+i\cdot b_n)}\\
\boxed{c_0=\frac{a_0}{2}}
$$
$\bullet$ Teorema de Abel: sea $f(x)=\sum_{n=0}^{\infty}c_nz^n=\sum_{n=0}^{\infty}c_nr^ne^{in\theta}$ con parte real e imaginaria $u(r,\theta)=\sum_{n=0}^{\infty}c_nr^n\cos(n\theta)$ y $v(r,\theta)=\sum_{n=0}^{\infty}c_nr^n\sin(n\theta)$, si $u(1,\theta)$ y $v(1,\theta)$ son convergentes para un dado $\large\theta \Rightarrow\ u(1,\theta)+i\cdot v(1,\theta)= lim_{r\rightarrow1}f(r\cdot e^{i\theta})=lim_{r\rightarrow 1}\sum_{n=1}^{\infty}c_nr^ne^{in\theta}$ .

$\bullet$ Para una función analítica el desarrollo de Laurent coincide con el desarrollo de Fourier.

#### Cambio de intervalo

$$
[0,2\pi]\rightarrow[-L,L]\\
\boxed{f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\bigg[a_n\cos\Big(\frac{n\pi}{L}x\Big)+b_n\sin\Big(\frac{n\pi}{L}x\Big) \bigg]}\\
\boxed{a_n=\frac{1}{L}\int_{-L}^{L}f(x)\cos\Big(\frac{n\pi}{L}x\Big)\ dx}\\
\boxed{b_n=\frac{1}{L}\int_{-L}^{L}f(x)\sin\Big(\frac{n\pi}{L}x\Big)\ dx}
$$


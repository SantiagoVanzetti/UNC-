# Hoja de ecuaciones Electromagnetismo I

## Ecuaciones de Maxwell 

**Ecuaciones estáticas**: $\newcommand{par}[2]{\frac{\partial #1}{\partial #2}}$

+ $\nabla\cdot \vec D=\rho$, Ley de Gauss para el campo eléctrico.

+ $\nabla\cdot\vec B=0$, Ley de Gauss para el campo magnético.

**Ecuaciones dinámicas**:

+ $\nabla\times\vec E=-\par{\vec B}{t}$, Ley de Faraday.
+ $\nabla\times \vec H=\vec J+\par{\vec D}{t}$, Ley de Ampere-Maxwell.

**Ecuaciones constitutivas**:

+ $\vec D=\varepsilon\vec E$ asociado con $\vec P$.
+ $\vec H=\frac{1}{\mu}\vec B$ asociado con $\vec M$.

**Fuerza de Lorentz**

+ $\vec F=q\vec E+q\vec v\times\vec B$

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
\end{array}
=\frac{1}{r\sin(\theta)}\bigg[\par{}{\theta}(\sin(\theta)F_\varphi)-\par{}{\varphi}(F_\theta)\bigg]\hat{r}+\frac{1}{r}\bigg[ \frac{1}{\sin(\theta)}\par{}{\varphi}(F_r)-\par{}{r}(rF_\varphi)\bigg]\hat{\theta}+\frac{1}{r}\bigg[\par{}{r}(rF_\theta)-\par{}{\theta}(F_r)\bigg]\hat{\varphi}}$

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

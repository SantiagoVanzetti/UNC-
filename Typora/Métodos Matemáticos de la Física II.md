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

Las componentes de un vector $\vec x$ en una base son los coeficientes $x^i$ tal que:
$$
x=x^i\vec e_i
$$

#### Subespacios lineales 

$W$ es subespacio de $V$ si $\forall\vec x\in W\Rightarrow \vec x \in V$, y $W$ es un EV.

#### Suma directa

Si se tiene una colección finita de subespacios $V_i$ de $V$ **disjuntos** y $\forall \vec x \in V\ \exists!\vec x_i/\vec x=\vec x_i$, entonces $V$ es suma directa de los subespacios $V_i$:
$$
V=\oplus_{i=1}^rV_i\\
\text{dim}(V)=\sum\text{dim}(V_i)
$$

Donde la suma direct se define como $U\oplus W=\{\vec x+\vec y /\vec x \in U \and \vec y \in W\}$ y $U\cap W=\{\vec 0\}$.

### Operadores lineales 

Los **operadores lineales** son aplicaciones que llevan a cada elemento de un EV $V$ a otro EV $W$, y es lineal. Es decir:
$$
V\ni\vec x\overset{\mathcal A}\rightarrow \mathcal A(\vec x)\in W\\
 \mathcal A(\lambda\vec x+\mu\vec y)=\lambda \mathcal A(\vec x)+\mu \mathcal A(\vec y)
$$
El **kernel** de un operador lineal es:
$$
ker(\mathcal A)=\{\vec x\in V/\mathcal A(\vec x)=0\}
$$
Si se tiene un operador lineal $\mathcal A: V\rightarrow W$ la **imagen** de un $\vec x$ bajo $\mathcal A$ es $\vec y=\mathcal A\vec x$ y $\vec x $ es la **preimagen** de $\vec y$ sobre $\mathcal A$. Para un operador lineal la imagen es única para cada $\vec x $, pero la preimagen puede no ser única para cada $\vec y$.

Un subespacio $W$ de $V$ es **invariante** bajo el operador $\mathcal A:V\rightarrow V$ si $\forall\vec x\in W\Rightarrow \mathcal A \vec x\in W $. Así se puede definir una restricción del operador sobre el subespacio si se piensa $\mathcal A/W:W\rightarrow W$ (esto solo se puede hacer si $W$ es invariante bajo $\mathcal A$). $\mathcal A/W:=\mathcal A\mathcal P_W$, donde $\mathcal P_W$ es la proyección sobre $W$.

#### Componentes de un operador

Si $\vec e_i$ base de $V$ y $\vec f_j$ base de $W$ entonces existen únicos coeficientes $A_i^j$, que son las componentes del operador, tal que:
$$
\mathcal A\vec e_i=A_i^j\vec f_j
$$
Nota: las operaciones elementales entre operadores se comportan como las operaciones entre matrices.

#### Inversa

Sea $\mathcal A:V\rightarrow W$ si existe $\mathcal B:W\rightarrow V$ tal que $\mathcal B\mathcal A=\mathcal I$, entonces $\mathcal B$ es la inversa de $\mathcal A$.

Propiedad: la inversa existe $\Leftrightarrow$ dim($W$)$\geq$dim($V$).

Propiedad: un operador $\mathcal A$ es invertible $\Leftrightarrow$ dim(ker($\mathcal A$))=0.

#### Conmutatividad

$\mathcal A$ y $\mathcal B$ conmutan si $\mathcal A\mathcal B= \mathcal B\mathcal A$, y se define el conmutador $[\mathcal A,\mathcal B]=\mathcal A\mathcal B- \mathcal B\mathcal A$ 

#### Funciones de operadores

Se puede definir:
$$
f(\mathcal A)=\sum_{n=0}^\infty a_n\mathcal A^n\\
f(\mathcal A)\vec v=\sum_{n=0}^\infty a_n\mathcal A^n\vec v
$$

### Matrices 

El producto de matrices se define como $[AB]_i^j=A_i^kB_k^j$. $i $ mapea columnas y $j$ filas.

#### Tipos de matrices 

Si la matriz $A$ tiene componentes $A_i^j$:

+ Conjugada $A^*/[A^*]_i^j=(A_i^j)^*$.
+ Traspuesta $A^t/[A^t]_i^j=A_j^i$.
+ Adjunta $A^{\dagger}/[A^{\dagger}]_i^j=(A_j^i)^*$
+ Inversa $A^{-1}/[A^{-1}]_i^j=\frac{cofA_j^i}{det (A)}$. Donde $cofA_i^j=(-1)^{i+j}\cdot det(A \text{ sin su fila j y columna i})$.

#### Matrices notables 

+ Real $A^*=A$.
+ Simétrica $A^t=A$.
+ Antisimétrica $A^t=-A$.
+ Autoadjunta o Hermitiana $A^{\dagger}=A$.
+ Ortogonal $A^{-1}=A^t$.
+ Unitaria $A^{-1}=A^{\dagger}$.
+ Diagonal $A^j_i=0\ \forall i\neq j$.
+ Idempotente $A^2=A$.
+ Nilpotente $\exist k\in \N /A^k=0$

**Nota**: las matrices para realizar productos se pueden trabajar por bloques tal que tenga sentido multiplicarlos (mismo numero de filas y columnas). Así para el proceso de diagonalización es útil.

#### Funciones de matrices 

$$
f(A)=\sum_{n=0}^\infty a_n A^n
$$

### Transformaciones de coordenadas

Para dos bases de $V$, $\vec e_i$ y $\vec e_j'$, como la base primada es un vector de $V$ se puede escribir como combinación de la base no primada:
$$
\boxed{\vec e_j'=\gamma_j^i\vec e_i}
$$
Los coeficientes $\gamma_j^i$ se pueden ver como elementos de una matriz cuadrada $\gamma$. Si se acomodan los vectores de la base como columnas de una matriz $E$ y $E'$ para cada base:
$$
E'=E\gamma
$$

#### Covarianza y contravarianza

Todo elemento que ante un cambio de base cambie como los vectores base se denomina **covariante**, y se colocan sus índices como subíndices. Si lo hace de forma inversa se llama **contravariante** y sus índices se colocan como superíndices.

#### Transformación de un componente de un vector

$$
\boxed{x'^j=[\gamma^{-1}]^j_ix^i}
$$

#### Componentes de un operador 

Si un operador va de $V$ con matriz de cambio de base $\gamma$ ($\vec e_j'=\gamma_j^i\vec e_i$), a $W$ con matriz de cambio de base $\delta$ ($\vec f_l'=\delta_j^i\vec f_k$).
$$
\boxed{A'^k_j=[\delta^{-1}]_l^kA_i^l\gamma_j^i}
$$

#### Transformaciones de semejanza 

Una transformación de semejanza es toda transformación lineal tal que $A'=S^{-1}AS$. Cumplen que:

+ $det(A')=det(A)$

+ $Tr(A')=Tr(A)$

+ $f(A')=S^{-1}f(A)S$

+ $A=A^{\dagger}\Rightarrow A'=A'^{\dagger}$ si $S$ es unitaria.

+ $A^{-1}=A^{\dagger}\Rightarrow A'^{-1}=A'^{\dagger}$ si $S$ es unitaria.

+ $A^{-1}=A^t\Rightarrow A'^{-1}=A'^t$ si $S$ es ortogonal.

+ $AB=BA\Rightarrow A'B'=B'A'$.

+ $B=A^{-1}\Rightarrow B'=(A')^{-1}$

  

### Formas y espacio dual

#### Forma 

Una n-forma es una aplicación tal que $V\oplus V\oplus...\oplus V\ni(\vec x_1,\vec x_2,...,\vec x_n)\overset{\phi}\rightarrow\phi(\vec x_1,\vec x_2,...,\vec x_n)\in \C$. Es una forma lineal si $\phi(\lambda\vec x+\mu\vec y)=\lambda\phi(\vec x)+\mu\phi(\vec y)$.

#### Espacio dual 

Se define el espacio dual $V^*$ de $V$ como el espacio de todas las formas lineales definidas sobre $V$.
$$
V^*=\{\phi :V\rightarrow\C/\phi \text{ lineal}\}
$$

#### Componentes de una forma 

Se define $\phi_i:=\overleftarrow{\phi}(\vec e_i)$, entonces $\overleftarrow{\phi}(\vec x)=\phi_ix^i$. Se define también, la base dual de una base $\vec e_i$ de $V$ tal que:
$$
\overleftarrow{e^i}(\vec e_j)=\delta_j^i\\
\Rightarrow \ \overleftarrow{\phi}=\phi_i\overleftarrow{e^i}
$$

#### Transformaciones de coordenadas en $V^*$ 

Las componentes de las formas $\phi_i$ son covariantes, es decir:
$$
\boxed{\phi'_j=\phi_i\gamma_j^i}
$$
Y los vectores base son contravariantes:
$$
\boxed{\overleftarrow{e'^j}=[\gamma^{-1}]_i^j\overleftarrow{e^i}}
$$

### Producto interno, métrica y norma

#### Producto interno 

El producto interno es una 2-forma tal que $\Phi:V\oplus V\rightarrow\C$, y satisface:

+ $\Phi(\vec a,\vec b)=\Phi(\vec b,\vec a)$.
+ $\Phi(\vec a,\lambda\vec b)=\lambda\Phi(\vec a,\vec b); \ \Phi(\lambda\vec a,\vec b)=\lambda^*\Phi(\vec a,\vec b)$.
+ $\Phi(\vec a,\vec a)\geq0\ \forall\vec a$ y $\Phi(\vec a,\vec a)=0 \Leftrightarrow \vec a=0$

#### Métrica

Se define la métrica como $g_{ij}=\Phi(\vec e_i,\vec e_j)$. Y la matriz métrica $g=[g_{ij}]$.

Se puede aplicar:
$$
\vec x\cdot \vec y=\mathbb x^{\dagger}g\mathbb y
$$
La métrica es hermitiana y definida positiva.

#### Norma

Se puede definir la norma a partir del producto interno:
$$
||\vec x||=\sqrt{\vec x\cdot\vec x}=\sqrt{x^{*i}g_{ij}x^j}
$$
Se puede pensar el producto interno de la siguiente forma:
$$
\overleftarrow{\phi_{\vec x}}:=\Phi(\vec x,\cdot)
$$
Se puede deducir que:
$$
\phi_{\vec x j}=x^{*i}g_{ij}
$$
Por lo que la métrica lleva las componentes de un vector a las componentes de la correspondiente forma $V\ni\vec x\overset{g}\rightarrow\overleftarrow{\phi_{\vec x}}\in V^*$.

### Autovalores y autovectores

#### Autovectores a derecha

Si se tiene un operador lineal con una matriz asociada $A: V\rightarrow V \Rightarrow\ \exist \vec v \in V/ A\vec v=\lambda\vec v,\ \vec v\neq 0$.
$$
\boxed{A\vec v=\lambda \vec v}\\
\Rightarrow (A-\lambda I)\vec v=0\\
\Rightarrow \mathcal P(\lambda)=det(A-\lambda I)=\sum_{j=0}^n\alpha_j\lambda^{n-j}
$$
Donde los $\lambda$ son los invariantes algebraicos.

Teorema: si se tienen n autovalores distintos con dim($V$)=n, entonces los autovectores asociados forman base de $V$. 

A partir de los autovalores de una matriz se puede definir una noción de norma para las matrices, llamada **norma espectral**:
$$
||A||_2=\sqrt{\lambda_{max}(A^{\dagger}A)}
$$
Si la norma es menor al radio de convergencia de una serie, entonces la serie converge. Puede ser que a pesar, de que la norma sea mayor la serie converja, ya que la matriz puede ser nilpotente y se trunca la serie.

#### Autovalores a izquierda

Los autovalores a izquierda cumplen que $A^{\dagger}\vec u=\mu\vec u$, y se puede demostrar que:


$$
\boxed{\mu_i\equiv \lambda_i^*}
$$
Los autovectores a izquierda cumplen que si los $\mu_i$ son distintos (si los $\lambda_i$ son distintos), forman base de $V$. Para calcularlos se utiliza que:
$$
A^{\dagger}\vec u_i=\lambda_i^*\vec u_i\\
\boxed{\vec u^{i\dagger}A=\lambda_i\vec u^{i\dagger}}
$$

#### Diagonalización de un operador

Si se tiene un operador lineal $A:V\rightarrow V$, n=dim($V$), con autovalores distintos entonces:
$$
\mathbb v=\begin{bmatrix}
\vec v_1\ \vec v_2\ ...\vec v_n
\end{bmatrix}\\
\mathbb u=\begin{bmatrix}
\vec u_1^{\dagger}\\ \vec u_2^{\dagger}\\  .\\.\\.\\\vec u_n^{\dagger}
\end{bmatrix}
$$
Se cumple que:
$$
\mathbb u\mathbb v=I\\
\mathbb uA \mathbb v=D
$$
Con $D$ matriz diagonal con los autovalores en orden en la diagonal.

#### Operadores Hermitianos

Teorema: si se tiene un operador tal que $\mathcal P_A(\lambda)=(\lambda-\lambda_1)^{q_1}(\lambda-\lambda_2)^{q_2}...(\lambda-\lambda_r)^{q_r}$, donde $q_i$ es la multiplicidad, si $A$ hermitiana $A\vec v=\lambda_i\vec v $ tiene $q_i$ soluciones LI, por lo que los autovectores generan un subespacio de dimensión$q_i$. Y $A$ **diagonalizable**.

Teorema: si $A$ y $B$ hermitianas, $\exist S/S^{-1}AS=D_A$ y $S^{-1}BS=D_B\Leftrightarrow[A,B]=0$.

#### Operadores normales 

$A$ es **normal** si cumple:
$$
AA^{\dagger}=A^{\dagger}A
$$
Si $A$ es normal $\Rightarrow$ $A$ es diagonalizable.

### Formas de Jordan

Falta el teorema de descomposición primaria.

Si se tiene una matriz $A$, se realiza la descomposición primaria (ya viene descompuesta), se calculan $(A-\lambda I)^n$, hasta llegar a una matriz nula. En una tabla se coloca la potencia n, la dim(ker($(A-\lambda I)^n$)) y se calcula $n_p$:
$$
n_{p_i}=2dim(ker(A-\lambda _iI)^p)-dim(ker(A-\lambda _iI)^{p-1})-dim(ker(A-\lambda _iI)^{p+1})
$$
Este $n_p$ da el numero de filas y columnas de los bloques de Jordan, y se acomodan de cualquier forma. Ver apunte para saber la forma de estos bloques. Es en la diagonal el autovalor y en la diagonal superior todos 1, el tamaño depende de la multiplicidad del autovalor.

La forma de Jordan es independiente de la base en la que se expresa $A$.

## Tensores 

Un tensor es una aplicación tal que $T:\Pi_r^s = V^*\times V^*\times...V^*\times V\times V\times...\times V\rightarrow \C$ (r veces el dual y s veces $V$).

Un espacio tensorial es el conjunto de tensores $V_r^s=\{T:\Pi_r^s\rightarrow\C\}$.

+ Suma de tensores: $T,S:\Pi_r^s\rightarrow\C, (T+S)(\vec w^1,...,\vec w^r,\vec u_1,...,\vec u_s )=T(\vec w^1,...,\vec w^r,\vec u_1,...,\vec u_s )+S(\vec w^1,...,\vec w^r,\vec u_1,...,\vec u_s )$.
+ Producto por una escalar: $(\lambda T)(\vec w^1,...,\vec w^r,\vec u_1,...,\vec u_s )=\lambda\cdot T(\vec w^1,...,\vec w^r,\vec u_1,...,\vec u_s )$.

#### Producto tensorial 

$T\in V_{r_1}^{s_1},\ S\in V_{r_2}^{s_2}$ entonces $T\otimes S\in V_{r_1+r_2}^{s_1+s_2}$ se define como:
$$
(T\otimes S)(\vec w^1,...,\vec w^{r_1},\vec \tau^1,...,\vec \tau^{r_2},\vec u_1,...,\vec u_{s_1},\vec v_1,...,\vec v_{s_2} )=\\
=T(\vec w^1,...,\vec w^{r_1},\vec u_1,...,\vec u_{s_1})\cdot S(\vec \tau^1,...,\vec \tau^{r_2}
\vec v_1,...,\vec v_{s_2} )
$$

#### Base y componente de un tensor 

Las componentes de un tensor $S\in V_r^s$ para una base de $V^*$ $\vec e^j$, y una base de $V$ $\vec e_i$ son:
$$
S^{i_1...i_r}_{j_1...j_s}=S(\vec e^{i_1},...\vec e^{i_r},\vec e_{j_1},...,\vec e_{j_s})
$$
Y la base de $V_r^s$ es el producto tensorial:
$$
\vec e_{i_1}\otimes...\otimes\vec e_{i_r}\otimes\vec e^{j_1}\otimes...\otimes\vec e^{j_s}
$$
Entonces el tensor $S$ se puede escribir como:
$$
S=S^{i_1...i_r}_{j_1...j_s}\vec e_{i_1}\otimes...\otimes\vec e_{i_r}\otimes\vec e^{j_1}\otimes...\otimes\vec e^{j_s}
$$

#### Cambio de base de un tensor

Para un tensor $S\in V_r^s$ con componentes $S^{i_1...i_r}_{j_1...j_s}$. Si la base de $V$, $\vec e_i$ cambia a la base $\vec e'_j$ con el operador $A$ $\vec e'_j=A_j^i\vec e_i$. Por lo tanto, las bases de $V^*$ cambian como $\vec e'^j=[A^{-1}]_i^j\vec e^i$. El tensor $S$ cambia de base de la siguiente forma:
$$
\boxed{S'^{k_1...k_r}_{l_1...l_s}=[A^{-1}]^{k_1}_{i_1}[A^{-1}]^{k_2}_{i_2}...[A^{-1}]^{k_r}_{i_r}
\ A_{l_1}^{j_1}A_{l_2}^{j_2}...A_{l_s}^{j_s}\ S^{i_1...i_r}_{j_1...j_s}}\tag{1}
$$
Se dice que $S$ es r veces contravariante y s veces covariante.

A partir de ver como cambia de base un tensor, se puede definir tensor como cualquier objeto con $r+s$ índices que van de 1 a n=dim(V), y que ante un cambio de base transforma como (1). Lo llamaremos tensor de **rango** $r+s$ del **tipo** (r,s).

#### Contracción de índices 

Si se tiene un tensor $S\in V_r^s$ con componentes $S^{i_1...i_r}_{j_1...j_s}$, el contraído de $S$ con respecto a los índices $i_n$ y $j_m$ como:
$$
S^{i_1...i_{n-1}\ k\ i_{n+1}...i_r}_{j_1...j_{m-1}\ k\ j_{m+1}...j_s}=S^{i_1...i_r}_{j_1...j_s}\delta_{i_n}^{j_m}
$$
Se obtiene un tensor de tipo ($r-1,s-1$). 

Nota: un contraído se un tensor es un tensor, si y solo si se contraen índices de a pares, uno covariante y otro contravariante.

#### Simetría

Un tensor $S\in V_r^s$ es **simétrico** respecto a los índices $i_n$ e $i_m$ si:
$$
S^{i_1...i_{m}... i_{n}...i_r}_{j_1...j_s}=S^{i_1...i_{n}... i_{m}...i_r}_{j_1...j_s}
$$
Equivalentemente se define para índices covariantes.

Si un tensor es simétrico respecto a cualquier par de índices, se dice que el tensor es **simétrico**.

Un tensor $S\in V_r^s$ es **antisimétrico** respecto a los índices $i_n$ e $i_m$ si:
$$
S^{i_1...i_{m}... i_{n}...i_r}_{j_1...j_s}=-S^{i_1...i_{n}... i_{m}...i_r}_{j_1...j_s}
$$
Equivalentemente se define para índices covariantes.

$S\in V_r^0$ es **totalmente antisimétrico** si:
$$
S^{\Pi(i_1...i_r)}=sgn(\Pi)S^{(i_1...i_r)}
$$
Donde $\Pi(i_1...i_r)$ es una permutación de los índices y $sgn(\Pi)$ es 1 si es un número de permutaciones es par y -1 si es impar. De igual modo se define para índices covariantes.

#### Simetrización y antisimetrización de tensores

Dado un tensor $T\in V_r^0$ su **parte simétrica** es $\mathcal S T\in V_r^0$ con componentes:
$$
(\mathcal ST)^{i_1...i_r}=\frac{1}{r!}\sum_\Pi T^{\Pi(i_1...i_r)}
$$
La **parte antisimétrica**, $\mathcal AT\in V_r^0$, con componentes:
$$
(\mathcal A T)^{i_1...i_r}=\frac{1}{r!}\sum_\Pi sgn(\Pi)T^{\Pi(i_1...i_r)}
$$
De manera análoga se define para tensores covariantes.

+ $\{\}$ denota la simetrización.
+ $[\ ]$ denota la antisimetrización.

#### Producto exterior 

Sean tensores $S\in V_0^s$ con componentes $S_{j_1...j_s}$ totalmente antisimétrico, y $T\in V_0^t$ con componentes $T_{j_1...j_t}$ totalmente antisimétrico. Se define su producto exterior:
$$
S\and T=\frac{(s+t)!}{s!t!}\mathcal A(S\otimes T)
$$
Tal que $S\and T\in V_0^{s+t}$ totalmente antisimétrico con componentes $S_{[j_1...j_s}T_{l_1...l_t]}$.

Este producto cumple:

+ $S\and(T_1+T_2)=S\and T_1+S\and T_2$.
+ $(S\and T)\and R=S\and (T\and R)=S\and T\and R$.
+ $S\and T=(-1)^{st}T\and S$

#### Densidades tensoriales 

Una densidad tensorial de peso p es un objeto tal que transforma tal que:
$$
\boxed{S'^{k_1...k_r}_{l_1...l_s}=det(A)^p\cdot [A^{-1}]^{k_1}_{i_1}[A^{-1}]^{k_2}_{i_2}...[A^{-1}]^{k_r}_{i_r}
\ A_{l_1}^{j_1}A_{l_2}^{j_2}...A_{l_s}^{j_s}\ S^{i_1...i_r}_{j_1...j_s}}
$$

#### Símbolo de Levi-Civita

$$
\varepsilon_{i_1...i_s}=\begin{cases}1\text{ si se tiene una permutación par de }i_1...i_s\\ -1\text{ si se tiene una permutación impar de }i_1...i_s\\ 0 \text{ si se repite índice}\end{cases}
$$

Este símbolo es una densidad tensorial de peso -1.

+ $\varepsilon^{ijk}\varepsilon_{klm}=\delta^i_l\delta^j_m-\delta^i_m\delta^j_l$.

#### Tensor adjunto 

Se define al tensor adjunto como:
$$
\overline T_{i_1...i_{n-r}}=\varepsilon_{i_1...i_{n-r}j_1...j_r}T^{j_1...j_r}
$$
Se cumple para el producto vectorial que: $\newcommand{par}[2]{\frac{\partial #1}{\partial #2}}$
$$
\vec u\times \vec v=\overline{\vec u\and \vec v}
$$

### Coordenadas curvilíneas

#### Cambio de coordenadas locales 

Ante un cambio de coordenadas las ecuaciones para calcular componentes en unas coordenadas con respecto a los componentes en otras puede ser altamente complicado, ya que las ecuaciones pueden ser no lineales. Pero, la relación entre los diferenciales siempre es lineal y homogénea:
$$
dx'^i=\par{x'^i}{x^j}dx^j
$$
Esto hace que se tome la matriz Jacobiana como la matriz de cambio de base entre coordenadas.
$$
\boxed{J=\bigg[\par{x^i}{x'^j}\bigg]_{ij}}\\
\boxed{J^{-1}=\bigg[\par{x'^i}{x^j}\bigg]_{ij}}
$$
Donde i son las filas y j las columnas.

#### Base tangente o covariante 

Una curva coordenada es una curva producida por mantener todas las coordenadas de la nueva base constantes, excepto por una, la cual varia:
$$
\vec x(x'^i)=x^j(x'^1=cte,...,x'^i,...,x'^n=cte)\vec e_j
$$
La **base covariante o tangente** para el cambio de coordenadas es:
$$
\boxed{\vec e'_j=\par{\vec x}{x'^j}=\par{x^i}{x'^j}\vec e_i}
$$

#### Vectores contravariantes

Un vector covariante se define como cualquier vector con componentes $u^i$ que transforme de acuerdo a:
$$
\boxed{u'^i=\par{x'^i}{x^j}u^j}
$$

#### Vectores covariantes

Un vector covariante se define como cualquier objeto con componentes $u_i$ que ante cambio de coordenadas transforme de acuerdo a:
$$
\boxed{u'_i=\par{x^j}{x'^i}u_j}
$$

#### Base dual o contravariante

Para calcular la base dual se puede aplicar la métrica a la base covariante o utilizando la regla de transformación y aplicándose la a la base dual de las coordenadas que ya se tenían. La regla de transformación de la base contravariante es:
$$
\boxed{\vec e'^j=\par{x'^j}{x^i}\vec e^i}
$$

#### Tensores en curvilíneas

Análogo a las definiciones anteriores un objeto con componentes $S^{i_1...i_r}_{j_1...j_s}$, que ante cambios de coordenadas transforme como:
$$
S'^{k_1...k_r}_{l_1...l_s}=\par{x'^{k_1}}{x^{i_1}}...\par{x'^{k_r}}{x^{i_r}}\ \par{x^{j_1}}{x'^{l_1}}...\par{x^{j_s}}{x'^{l_s}}\ S^{i_1...i_r}_{j_1...j_s}
$$

#### Densidades tensoriales 

Un objeto con componentes $S^{i_1...i_r}_{j_1...j_s}$ que ante cambios de coordenadas transforma de acuerdo a:
$$
S'^{k_1...k_r}_{l_1...l_s}=det(\mathbb J)^p\par{x'^{k_1}}{x^{i_1}}...\par{x'^{k_r}}{x^{i_r}}\ \par{x^{j_1}}{x'^{l_1}}...\par{x^{j_s}}{x'^{l_s}}\ S^{i_1...i_r}_{j_1...j_s}
$$
Se denomina densidad tensorial de peso $p$.

#### Tensor métrico

La métrica se puede obtener a partir de plantear un diferencial de arco, y expresarlo en ambas coordenadas:
$$
ds^2=dx^i\delta_{ij}dx^j=dx'^k\par{x^i}{x'^k}\delta_{ij}\par{x^j}{x'^l}dx'^l\\
ds^2=dx'^k\par{x^i}{x'^k}\par{x^i}{x'^l}dx'^l=dx'^kg_{kl}dx'^l
$$
Entonces se define la métrica:
$$
\boxed{g_{ij}:=\par{x^k}{x'^i}\par{x^k}{x'^j}}
$$
En notación matricial:
$$
\mathbb g:=[g_{ij}]=J^tJ
$$
Y se tiene que:
$$
\mathbb g'=J^t\mathbb gJ
$$
Se define la inversa de la métrica como:
$$
[g^{ij}]=\mathbb g^{-1}
$$
El determinante de la métrica es un pseudoescalar de peso 2, $g'=J^2g$.

Para coordenadas ortogonales se definen los **factores de escala** como:
$$
h_i^2:=g'_{\underline{ii}}
$$
Si las coordenadas son ortogonales:
$$
g'=h_1^2...h_n^2\\
\Rightarrow J=h_1h_2...h_n
$$
Aunque $J$ no sea diagonal.

#### Ascenso y descenso de índices

Para un vector contravariante se definen sus componentes covariantes como:
$$
u_i:=g_{ij}u^j
$$
Para un vector covariante se definen sus componentes contravariantes como:
$$
v^i:=g^{ij}v_j
$$
Esto se extiende a tensores $T^i_j=g_{jk}T^{ik}$.

#### Producto escalar y norma 

Usando la norma para subir y bajar índices se puede definir un producto escalar para dos vectores contravariantes o covariantes:
$$
\vec u\cdot \vec v=u^iv_i=g_{ij}u^iv^j=g^{ij}u_iv_j
$$
Usando que $||\vec u||^2=\vec u\cdot \vec u  $ sale la norma.

La métrica permite traducir de la base covariante a la base contravariante y viceversa:
$$
\boxed{\vec e^i=g^{ij}\vec e_j}\\
\boxed{\vec e_i=g_{ij}\vec e^j}
$$
En un sistema de coordenadas ortogonales se pueden extender estas ideas haciendo uso de los factores de escala (pág. 96).

### Integración en coordenadas curvilíneas

#### Integral de volumen

El diferencial de volumen es una densidad escalar de peso -1:
$$
\boxed{dV=JdV'}
$$
En cualquier sistema de coordenadas:
$$
\boxed{dV:=J det(\begin{bmatrix}d\vec x_1...d\vec x_n\\ \downarrow\ \ \ \ \ \  \ \downarrow\end{bmatrix})}
$$
Donde $d\vec x_i=dx^{\underline i}\vec e_{\underline i}$.

#### Integral de superficie

Sea $\vec S(u^1,u^2)$ la parametrización de la superficie, se define la métrica inducida:
$$
\tilde{g}_{ij}=\par{\vec S}{u^i}\cdot \par{\vec S}{u^j}
$$




Tal que los diferenciales en cada dirección quedan:
$$
d\vec S_1=\par{\vec S}{u^1}du^1\\
d\vec S_2=\par{\vec S}{u^2}du^2
$$
Entonces los diferenciales de área quedan:
$$
\boxed{dA=\sqrt{\tilde g}\ du^1du^2}\\
\boxed{\vec {dA}=d\vec S_1\times d\vec S_2}
$$

#### Diferencial de línea

Si se tiene una curva $\vec c(t)=c^i(t)\vec e_i$, el largo de la curva es:
$$
\boxed{\mathscr l(c)=\int_a^b\sqrt{\frac{dc'^i}{dt}g_{ij}\frac{dc'^j}{dt}}dt}
$$

### Derivación en coordenadas curvilíneas

#### Conexión de Levi-Civita

Son coeficientes tal que:
$$
\vec e_{j,k}=\Gamma^i_{jk}\vec e_i
$$
Entonces la derivada de un vector:
$$
\vec u_{,k}=(u^i_{,k}+\Gamma_{jk}^iu^j)\vec e_i
$$
Estos son los elementos de conexión afín de Levi-Civita. Y son tal que:
$$
\Gamma_{jk}^i=\vec e^i\vec e_{j,k}
$$
Además, cumplen que:
$$
\Gamma_{jk}^i=\Gamma_{kj}^i
$$




















#### Derivada covariante 

Si $u^i$ es un vector contravariante su derivada covariante es:
$$
u^i_{;k}:=u^i_{,k}+\Gamma^i_{jk}u^j
$$
Se pueden definir las derivadas covariantes de tensores de rango arbitrario:

<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\Cuadrommf.png" alt="Cuadrommf" style="zoom: 50%;" />



Los elementos de conexión afín pueden calcularse usando la métrica:
$$
\boxed{\Gamma_{jk}^m=\frac{1}{2}g^{mi}(g_{ij,k}+g_{ik,j}-g_{kj,i})}
$$
<img src="D:\Administrador\Escritorio\UNC-\Typora\Typora Images\log-martin.png" alt="log-martin" style="zoom:50%;" />

#### Gradiente 

Se define el gradiente $\nabla \varphi$ de una escalar como el vector covariante:
$$
\boxed{\nabla\varphi=\varphi_{;i}\vec e^i=\varphi_{,i}\vec e^i}
$$

#### Rotor

Se define para un vector covariante (si se quiere para un contravariante usar la métrica):
$$
\boxed{\nabla\times \vec u=\sqrt{g^{-1}}\varepsilon^{ijk}u_{i,j}\vec e_k}
$$

#### Divergencia

Se define para un vector contravariante (si se quiere para uno covariante usar la métrica):
$$
\boxed{\nabla\cdot\vec u=\frac{1}{\sqrt g}(\sqrt gu^i)_,i}
$$

#### Laplaciano

$$
\boxed{\nabla^2\varphi=\frac{1}{\sqrt g}(\sqrt g\ g^{ij}\varphi_{,\ j})_{,i}}
$$











#### Componentes físicas

Si se tienen coordenadas ortogonales (la métrica es diagonal), defino:
$$
\hat{e_i}:=\frac{\vec e_i}{||\vec e_i||}=\frac{\vec e^i}{||\vec e^i||}
$$
Con coordenadas ortogonales y componentes físicas, los operadores diferenciales vectoriales quedan:
$$
\boxed{\nabla\varphi=\frac{1}{h_i}\varphi_{,i}\hat{e_i}}\\
\boxed{\nabla \times \vec u=\varepsilon_{ijk}\frac{h_i}{J}(h_ku_k)_{,j}\hat{e_i}}\\
\boxed{\nabla\cdot \vec u=\frac{1}{J}\bigg(\frac{J}{h_i}u_i\bigg)_{,i}}\\
\boxed{\nabla^2\varphi=\frac{1}{J}\bigg(\frac{J}{h_i^2}\varphi_{,i}\bigg)_{,i}}
$$

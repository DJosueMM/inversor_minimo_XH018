# inversor_minimo_XH018
Tarea_1_Introducción al diseño de circuitos integrados

## Parte 1. Estimación de salida base de las características RC del proceso XH018


### Parte1.a Determinación de las resistencias de canal de transistores mínimos NMOS y PMOS para el proceso XH018
#### Fórmula de la resistencia cuando el transistor esta saturado
$$R_{eff} = \frac{3In(2)}{4} \frac{V_{DD}}{I_{sat}}  \quad(1)$$ 

#### Fórmula de la resistencia cuando el transistor esta en transición
$$R_{eff} = \frac{V_{DD}}{I_{H}+I_{L}}  \quad(2)$$
\
\
Los valores para los siguientes cáculos se tomaron de los parámetros para transistores 1.8V (ne,pe) de un proceso XH018 - 0.18 µm
Los cálculos se mutiplicaron por el ancho para obtener el valor de las resistencias en terminos de $\ohm$.
### Cáculos para transistor NMOS
A continuación se presentan los cálculo con la ecuación (1).
$$R_{eff} = \frac{3In(2)}{4} \frac{1.8V}{475 \times 10^{-6} A/{\micro m} \cdot 0.36{\micro m}} \approx 5.5 k\ohm $$ 

Ahora con la ecuación (2).
$$R_{eff} = \frac{1.8V} {(475 \times 10^{-6} + 3 \times 10^{-12}) \cdot 0.36{\micro m}} \approx 10.53 k\ohm$$




### Cáculos para transistor PMOS



### Parte1.b Determinación de las capacitancias equivalentes que tiene el transistor de tamaño mínimo y constante RC para el proceso
### Transistor NMOS
#### Cálculo de la capacitancia 

#### Cálculo de la constante RC


### Transistor PMOS
#### Cálculo de la capacitancia 

#### Cálculo de la constante RC




## Parte 2. Diseño deun inversor mínimo de tamaño óptimo 
### Parte 2.a 


### Parte 2.b


### Parte 2.c




## Análisis
### Incluir figuras 

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
Los valores para los siguientes cáculos se tomaron de los parámetros para transistores 1.8V (ne,pe) de un proceso XH018 - 0.18 µm. Además para los cáculos realizados, se desprecia $I_{L}$, ya que su valor en comparación con otras corrientes en el circuitos es muy pequeña. También es importante destacar que para obtener los valores de las resistecias en términos de ohmios se multipicaron las ecuaciones (1) y (2) por el ancho de los transistores. 

### Cáculos para transistor NMOS
A continuación se presentan los cálculo con la ecuación (1).
$$R_{eff} = \frac{3In(2)}{4} \frac{1.8V}{475 \times 10^{-6} A/{\micro m} \cdot 0.36{\micro m}} \approx 5.5 k\ohm $$  

Ahora con la ecuación (2).
$$R_{eff} = \frac{1.8V} {(475 \times 10^{-6} A/{\micro m}) \cdot 0.36{\micro m}} \approx 10.6 k\ohm$$
\
Para determinar la resistencia unitaria de un transistor NMOS para el proceso XH018 - 0.18 µm se realiza de la siguiente forma.
$$R_{nueff} = \frac{1.8V} {(475 \times 10^{-6} A/{\micro m})} \approx 3.8 k\ohm/{\micro m}$$


### Cáculos para transistor PMOS
A continuación se presentan los cálculo con la ecuación (1).
$$R_{eff} = \frac{3In(2)}{4} \frac{1.8V}{170 \times 10^{-6} A/{\micro m} \cdot 0.72{\micro m}} \approx 7.7 k\ohm $$ 

Ahora con la ecuación (2).
$$R_{eff} = \frac{1.8V} {(170 \times 10^{-6} A/{\micro m}) \cdot 0.72{\micro m}} \approx 14.7 k\ohm$$
\
Para determinar la resistencia unitaria de un transistor PMOS para el proceso XH018 - 0.18 µm se realiza de la siguiente forma.
$$R_{pueff} = \frac{1.8V} {(170 \times 10^{-6} A/{\micro m})} \approx 10.6 k\ohm$$


### Parte1.b Determinación de las capacitancias equivalentes que tiene el transistor de tamaño mínimo y constante RC para el proceso
Los valores para los siguientes cáculos se tomaron de los parámetros para transistores 1.8V (ne,pe) de un proceso XH018 - 0.18 µm.

#### Fórmula de la capacitancia parásita si se considera pesimista 
$$C_{gs} = W_{dib} L_{dib}C_{ox} +  W_{dib}  C_{ov}  \quad(3)$$

#### Fórmula de la constante RC ($\tau$) 
$$\tau = 3RC  \quad(4)$$

### Transistor NMOS
#### Cálculo de la capacitancia 
A continuación se presentan los cálculo con la ecuación (3).
$$C_{gn} = 0.36\micro m \cdot 0.18\micro m \cdot 8.46 fF/\micro{m}^{2} +  0.36\micro m \cdot 0.33 fF/\micro m $$
$$C_{gn} \approx 0.67 fF$$

#### Cálculo de la constante RC ($\tau$)
Para determinar la constante RC para el transistor NMOS se utlizó la ecuación (4), el desarollo de la misma se presenta a continuación.
$$\tau = 3 \cdot 10.6 k\ohm \cdot 0.67 fF = 21.31 ps$$


### Transistor PMOS
#### Cálculo de la capacitancia 
A continuación se presentan los cálculo con la ecuación (3).
$$C_{gp} = 0.72\micro m \cdot 0.18\micro m \cdot 8.91 fF/\micro{m}^{2} +  0.72\micro m \cdot 0.32 fF/\micro m $$
$$C_{gp} \approx 1.39 fF$$

#### Cálculo de la constante RC ($\tau$)
Para determinar la constante RC para el transistor PMOS se utlizó la ecuación (4), el desarollo de la misma se presenta a continuación.
$$\tau = 3 \cdot 14.7 k\ohm \cdot 1.39fF = 60.88 ps$$



## Parte 2. Diseño deun inversor mínimo de tamaño óptimo 
### Parte 2.a 


### Parte 2.b


### Parte 2.c




## Análisis
### Incluir figuras 

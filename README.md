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

### Análisis empírico
Para determinar de forma empírica el valor de resistencia del transistor NMOS para el proceso XH018 se montó el siguiente deck https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/spice_decks/nmos_test.sp y luego se exportaron en un archivo .csv para gráficarlas en python y se obtuvieron las siguientes gráficas.

![NMOS_Ids_Vds](https://github.com/DJosueMM/inversor_minimo_XH018/assets/125601912/79e5fc9f-8c60-49d7-87f3-55c9065d06c1)

![NMOS_Ids_Vgs](https://github.com/DJosueMM/inversor_minimo_XH018/assets/125601912/2201089d-fc23-433e-aa93-48ea43aab2c2)


Para determinar la resistencia mediante la ecuación (1) se utilizó la gráfica de la función de transferencia de NMOS, con esta se aproximo el valor de $I_{sat}$ y se realizó el cálculo que se presenta a continuación. 

$$R_{eff} =\frac{3In(2)}{4} \frac{1.8V} {213.7 \micro A} \approx 4.4 k\ohm$$

Con ayuda de la gráfica de la curva característica del transistor NMOS se extrajeron los datos de $I_H$ e $I_L$, estos dieron como resultado $199 \micro A$ y $29.07 \micro A$ respectivamente, una vez obtenidos los datos se procedió a resolver la ecuación (2), el resultado se presenta a continuación. 

$$R_{eff} =  \frac{1.8V}{199 \micro A  + 29.07 \micro A}  \approx 7.9 k\ohm $$  

Con los valores obtenido anteriormente se determinó la resistencia unitaria para un transistor NMOS, el cual se obtuvo el siguiente resultado. 
$$R_{nueff} = \frac{7.9 k\ohm} {{0.36 \micro m}} \approx 22 k\ohm/\micro m$$


### Cáculos para transistor PMOS
A continuación se presentan los cálculo con la ecuación (1).
$$R_{eff} = \frac{3In(2)}{4} \frac{1.8V}{170 \times 10^{-6} A/{\micro m} \cdot 0.72{\micro m}} \approx 7.7 k\ohm $$ 

Ahora con la ecuación (2).
$$R_{eff} = \frac{1.8V} {(170 \times 10^{-6} A/{\micro m}) \cdot 0.72{\micro m}} \approx 14.7 k\ohm$$
\
Para determinar la resistencia unitaria de un transistor PMOS para el proceso XH018 - 0.18 µm se realiza de la siguiente forma.
$$R_{pueff} = \frac{1.8V} {(170 \times 10^{-6} A/{\micro m})} \approx 10.6 k\ohm/{\micro m}$$

### Análisis empírico
Una manera muy parecida se realizó para determinarlo los valores de resistencia de PMOS pero en este caso se uso el siguiente deck https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/spice_decks/pmos_test.sp, para posteriomente realizar el mismo procedimiento que el nmos, a continuación se presenta las gráficas y los cálculos realizados. 

![PMOS_Ids_Vds](https://github.com/DJosueMM/inversor_minimo_XH018/assets/125601912/1cccd635-e6b7-4593-b39b-c3e37863f585)

![PMOS_Ids_Vgs](https://github.com/DJosueMM/inversor_minimo_XH018/assets/125601912/81328b36-2d41-40da-9319-c40e7a9983ee)

Primero se presenta los cálculos con la ecuación (1).
$$R_{eff} =\frac{3In(2)}{4} \frac{1.8V} {180.5 \micro A} \approx 5.2 k\ohm$$

Ahora con la ecuación (2) donde con ayuda de la gráfica se determinó que $I_H=161.7\micro A$ e $I_L=20.83\micro A$.

$$R_{eff} =  \frac{1.8V}{161.7 \micro A  + 20.83 \micro A}  \approx 9.9 k\ohm $$  

Para determinar la resistencia unitaria de un transistor PMOS para el proceso XH018 - 0.18 µm se realiza de la siguiente forma.
$$R_{pueff} = \frac{9.9 k\ohm} {{0.36 \micro m}} \approx 27.5 k\ohm/\micro m$$
\
\
Si se comparan los datos obtenidos con los teóricos se pueden apreciar diferencias de alrededor de 3 k\ohm máximo esto se debe a que el analísis teórico realizado se cálculo con valores de $W/L= (10/0.18) \micro m/\micro m$, esto influye mucho en los valores ya que no se considera el valor que se nesecita de W que es $0.36 \micro m$, por lo que al tenes ese parámetro mal se considera que los valores teóricos generados tiene una pequeña falla con respecto a los experimentales.  



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








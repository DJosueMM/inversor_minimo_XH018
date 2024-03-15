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
Al comparar los datos obtenidos con los valores teóricos, se aprecian diferencias de alrededor de $4 k\ohm$ máximo. Esto se debe a que el analísis teórico realizado se cálculo con valor de $W/L= (10/0.18) \micro m/\micro m$, ya que el parámetros porporcionados para la tecnología XH018 mostraban ese valor, lo cual implica un gran impacto en los valores debido a que no se considera el valor mínimo de ancho necesario para esta tecngología que es $0.36 \micro m$. Por lo que, al tenes este parámetro diferente al requerido, se puede considerar que los valores teóricos generados tiene una pequeña discrepancia con respecto a los datos experimentales.  


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



## Parte 2. Diseño de un inversor mínimo de tamaño óptimo 
### Parte 2.a 

#### Inversor de tamaño mínimo 

Se diseñó a nivel de esquemático el inversor que se muestra en la siguiente figura:

![Esquemático del inversor](https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/Imagenes/sch_inversor.png)

Este cuenta con un NMOS de tamaño mínimo permitido por las reglas escalables con contactos en las difusiones para la tecnología utilizada. Teniendo un valor de lambda de 90 nm, la expresión del transistor mínimo 4/2 lambda resulta en un ancho de NMOS de 360 nm.

Para obtener un inversor sin sesgo con márgenes de ruido totalmente simétricos, se debe cumplir que al tener VDD/2 en la entrada, su salida sea también VDD/2. Esto implica que los parámetros Beta tendrán una relación Bp/Bn = 1. Para lograr esto, se diseñó el deck de HSPICE `inverter_transfer.sp`, donde se obtienen las funciones de transferencia para diferentes relaciones de anchos de transistor P/N. Al simular estos datos, se obtuvo la siguiente gráfica:

![Función de transferencia del inversor](https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/Imagenes/tf_inv_ra.png)

De estos datos, se concluye que para una relación de aproximadamente 3.1 : 1 se logran márgenes de ruido simétricos. No se llega a la simetría total debido a que se muestrearon ratios discretos, sin embargo, estas aproximaciónes son suficientes para un análisis del peor caso.

En cuanto a la corriente de cortocircuito, que ocurre cuando ambos transistores están encendidos en el punto donde Vout = VDD/2, se obtuvo la siguiente gráfica de corriente de cortocircuito en función de la relación P/N:

![Corriente de cortocircuito](https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/Imagenes/FO4_opt_isc.png)

Para una relación cercana a la que proporciona márgenes de ruido simétricos, se tiene aproximadamente una corriente instantánea de 0.90 A.

Los análisis anteriores se realizaron para una esquina de variabilidad del proceso "tm typical medium", que representa el comportamiento neutral. No obstante, se pueden realizar análisis en otras esquinas de variabilidad donde se sesga el inversor, haciendo más rápido el PMOS o el NMOS. Se llevó a cabo este análisis en las siguientes esquinas:

- WP: worst case power; NMOS rápido y PMOS rápido
- WS: worst case speed; NMOS lento y PMOS lento
- WO: worst case one; NMOS rápido y PMOS lento
- WZ: worst case zero; NMOS lento y PMOS rápido

Se simuló el inversor para cada esquina de variabilidad para obtener los tiempos de transición:

![inv_corners](https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/Imagenes/transient_inv_esquinas.png)

De estos datos, se obtuvieron los respectivos tiempos de propagación de subida y de caída para cada esquina:

![Esquinas de variabilidad](https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/Imagenes/corners_const.png)


### Parte 2.b

#### FO4

Se montó el FO4 que propone el libro [1], este se encuentra en `fo4_ratios.sp`. Con una ratio P/N de 2:1 se obtuvieron las señales en cada etapa del FO4:

Se obtuvo un tpdr = 80.76 ps, un tpdf = 70.34 ps y un tpd = 75.55 ps.

![fo4](https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/Imagenes/FO4.png)

#### Optimización manual
Después se modificó el deck para probar distintos ratios P/N automáticamente, este se encuentra en `fo4_ratios.sp`. Se obtuvieron las siguietes gráficas:

Para los tiempos de propagación para los distintos ratios P/N:

![tpd_ratios](https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/Imagenes/FO4_opt_t.png)

Para la potencia promedio para los distintos ratios P/N:

![pwr_ratios](https://github.com/DJosueMM/inversor_minimo_XH018/blob/main/Imagenes/FO4_opt_pwr.png)

#### Optimización de hspice


| p1      | bestratio | tpdr     | tpdf     | tpd      | diff     | Temperatura|
|---------|-----------|----------|----------|----------|----------|------------|
| 13.2009 | 3.3002    | 86.52 ps | 85.11 ps | 85.81 ps | 14.11 ps | 70.0000 C  |





### Parte 2.c








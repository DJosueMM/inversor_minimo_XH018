import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV omitiendo la primera fila
df = pd.read_csv("datos_sim\corners_trans.csv", skiprows=1)

# Escalar el tiempo a picosegundos
df['TIME '] *= 1e12  # Multiplicar por 1e12 para convertir de segundos a picosegundos

# Definir un diccionario para asignar nombres personalizados a cada valor de ALTER
alter_names = {1: 'tm', 2: 'wp', 3: 'ws', 4: 'wo', 5: 'wz'}

plt.plot(df['TIME '], df['v(in):ALTER=1 '], label='vin')

# Graficar la tensión v(out) en función del tiempo para cada ALTER
for alter in range(1, 6):
    plt.plot(df['TIME '], df[f'v(out):ALTER={alter} '], label=f'{alter_names[alter]}')

# Configuraciones adicionales
plt.title('Análisis del inversor para cada esquina del proceso')
plt.xlabel('Tiempo (ps)')
plt.ylabel('Tensión (V)')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

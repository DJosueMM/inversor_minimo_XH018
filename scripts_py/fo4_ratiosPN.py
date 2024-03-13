import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos desde el archivo CSV
df = pd.read_csv('datos_sim/fo4_ratios.mt0.csv', delimiter=',', skiprows=3)

# Convertir potencia a mW
df['pwr_mW'] = df['pwr'] * 1e3

# Convertir tiempos a picosegundos
df['tpdr_ps'] = df['tpdr'] * 1e12
df['tpdf_ps'] = df['tpdf'] * 1e12
df['tpd_ps'] = df['tpd'] * 1e12
df['diff_ps'] = df['diff'] * 1e12

# Encontrar cuando diff es más cercana a cero
punto_diff_cercano_cero = df.loc[np.abs(df['diff']).idxmin()]

# Encontrar el punto en ra = 2
punto_ra_2 = df.loc[(df['ra']-2).abs().idxmin()]

# Configurar estilo de Seaborn
sns.set(style="whitegrid")

# Graficar tpdr, tpdf, tpd y diff
plt.figure(figsize=(10, 6))
sns.lineplot(x='ra', y='tpdr_ps', data=df, label='tpdr')
sns.lineplot(x='ra', y='tpdf_ps', data=df, label='tpdf')
sns.lineplot(x='ra', y='tpd_ps', data=df, label='tpd')
sns.lineplot(x='ra', y='diff_ps', data=df, label='diff')

plt.scatter(punto_diff_cercano_cero['ra'], punto_diff_cercano_cero['tpd_ps'], color='red', marker='o', zorder=5)
plt.scatter(punto_diff_cercano_cero['ra'], punto_diff_cercano_cero['diff_ps'], color='red', marker='o', zorder=5)
plt.scatter(punto_ra_2['ra'], punto_ra_2['tpd_ps'], color='green', marker='o', zorder=5)
plt.scatter(punto_ra_2['ra'], punto_ra_2['diff_ps'], color='green', marker='o', zorder=5)

plt.text(punto_diff_cercano_cero['ra'], punto_diff_cercano_cero['tpd_ps']+ 5, f"{punto_diff_cercano_cero['tpd_ps']:.2f} ps", fontsize=10, ha='right')
plt.text(punto_diff_cercano_cero['ra'], punto_diff_cercano_cero['diff_ps']- 5, f"{punto_diff_cercano_cero['diff_ps']:.2f} ps", fontsize=10, ha='right')
plt.text(punto_ra_2['ra'], punto_ra_2['tpd_ps']+ 5, f"tpd: {punto_ra_2['tpd_ps']:.2f} ps", fontsize=10, ha='right')
plt.text(punto_ra_2['ra'], punto_ra_2['diff_ps']- 5, f"{punto_ra_2['diff_ps']:.2f} ps", fontsize=10, ha='right')

plt.xlabel('Relación $\\frac{W_P}{W_N}$')
plt.ylabel('Tiempo (ps)')
plt.title('Optimización manual del FO4')
plt.legend()
plt.grid(True)
plt.show()

# Graficar potencia (pwr)
plt.figure(figsize=(10, 6))
sns.lineplot(x='ra', y='pwr_mW', data=df, label='pwr')
plt.scatter(punto_diff_cercano_cero['ra'], punto_diff_cercano_cero['pwr_mW'], color='red', marker='o', zorder=5)
plt.scatter(punto_ra_2['ra'], punto_ra_2['pwr_mW'], color='green', marker='o', zorder=5)

plt.text(punto_diff_cercano_cero['ra'], punto_diff_cercano_cero['pwr_mW'] + 0.2, f"{punto_diff_cercano_cero['pwr_mW']:.2f} mW", fontsize=10, ha='right')
plt.text(punto_ra_2['ra'], punto_ra_2['pwr_mW']+ 0.2, f"{punto_ra_2['pwr_mW']:.2f} mW", fontsize=10, ha='right')

plt.xlabel('Relación $\\frac{W_P}{W_N}$')
plt.ylabel('Potencia (mW)')
plt.title('Potencia promedio del FO4 en función de la relación $\\frac{W_P}{W_N}$')
plt.grid(True)
plt.show()

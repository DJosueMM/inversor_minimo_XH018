import matplotlib.pyplot as plt

# Datos
tpdr_sec = [1.76E-11, 1.81E-11, 1.37E-11, 2.17E-11, 1.69E-11]
tpdf_sec = [1.62E-11, 1.47E-11, 1.32E-11, 2.00E-11, 1.80E-11]
corners = ['tm', 'wo', 'wp', 'ws', 'wz']

# Escalar a picosegundos
tpdr_ps = [x * 1E12 for x in tpdr_sec]
tpdf_ps = [x * 1E12 for x in tpdf_sec]

# Graficar
plt.scatter(tpdf_ps, tpdr_ps)

# Anotar las esquinas
for i, corner in enumerate(corners):
    plt.annotate(corner, (tpdf_ps[i], tpdr_ps[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Ajustes del gráfico
plt.title('Esquinas del proceso')
plt.xlabel('TPDF (ps)')
plt.ylabel('TPDR (ps)')
plt.grid(True)

# Extender los ejes para centrar los puntos
plt.xlim(min(tpdf_ps) - 2, max(tpdf_ps) + 2)
plt.ylim(min(tpdr_ps) - 2, max(tpdr_ps) + 2)

# Mostrar el gráfico
plt.show()

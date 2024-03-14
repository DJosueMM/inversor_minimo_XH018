import matplotlib.pyplot as plt

# Datos
ra = [1.0000, 1.5000, 2.0000, 2.5000, 3.0000, 3.5000, 4.0000, 4.5000, 5.0000, 5.5000, 6.0000]
isc = [0.8286, 0.8515, 0.8695, 0.8846, 0.8973, 0.9084, 0.9183, 0.9271, 0.9352, 0.9425, 0.9490]

# Graficar
plt.plot(ra,isc, marker='o', linestyle='-')
plt.title('Gráfico de Isc vs Ratio P/N')
plt.xlabel('Ratio P/N')
plt.ylabel('Isc (A)')
plt.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 1. DEFINIR LA FUNCIÓN
def f(x):
    return x**2 + 1

# 2. PARÁMETROS
a = 0          # Límite inferior
b = 2          # Límite superior
n = 4          # Número de rectángulos
delta_x = (b - a) / n

# 3. SUMATORIA DE RIEMANN (por la derecha)
x_riemann = np.linspace(a + delta_x, b, n)  # Puntos de la derecha
y_riemann = f(x_riemann)
area_riemann = np.sum(y_riemann * delta_x)

# 4. INTEGRAL DEFINIDA (exacta)
area_exacta, error = quad(f, a, b)

# 5. CREAR LA GRÁFICA
x_vals = np.linspace(a - 0.2, b + 0.2, 1000)
y_vals = f(x_vals)

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar la curva
ax.plot(x_vals, y_vals, 'b-', linewidth=2.5, label=f'$f(x) = x^2 + 1$')

# Dibujar los rectángulos de Riemann
for i in range(n):
    x_left = a + i * delta_x
    x_right = a + (i + 1) * delta_x
    # Altura: valor en el extremo derecho
    height = f(x_right)
    # Dibujar rectángulo
    ax.add_patch(plt.Rectangle(
        (x_left, 0), delta_x, height,
        facecolor='lightblue', edgecolor='blue', alpha=0.6
    ))
    # Marcar el punto de evaluación (extremo derecho)
    ax.plot(x_right, height, 'ro', markersize=6)

# Agregar línea en y=0
ax.axhline(y=0, color='black', linewidth=0.8)

# Configurar ejes y etiquetas
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)
ax.set_title('Suma de Riemann vs Integral Definida', fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend()

# Mostrar los valores en la gráfica
texto_info = (
    f'Riemann (derecha, n={n}): {area_riemann:.4f}\n'
    f'Integral exacta: {area_exacta:.4f}\n'
    f'Diferencia: {abs(area_exacta - area_riemann):.4f}'
)
ax.text(0.05, 0.95, texto_info, transform=ax.transAxes,
        fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

# 6. IMPRIMIR RESULTADOS EN CONSOLA
print("=" * 50)
print("RESULTADOS")
print("=" * 50)
print(f"Intervalo: [{a}, {b}]")
print(f"Número de rectángulos: {n}")
print(f"Delta x: {delta_x:.3f}")
print()
print(f"Suma de Riemann (por la derecha): {area_riemann:.6f}")
print(f"Integral definida (exacta):      {area_exacta:.6f}")
print(f"Diferencia (error):              {abs(area_exacta - area_riemann):.6f}")
print("=" * 50)

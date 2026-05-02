import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos
    
    # Regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    
    return integral

# Parámetros físicos
k = 0.5  # W/m·K

# Función derivada de la temperatura: dT/dx
def dTdx(x):
    return -100*x  # Derivada de T(x) = 300 - 50x^2

# Intervalo de integración
a, b = 0, 2
n_values = [6, 10, 20, 30]

# Solución analítica
# ∫ dT/dx dx = T(b) - T(a)
T = lambda x: 300 - 50*x**2
Q_exact = k * (T(b) - T(a))

# Calcular aproximaciones y errores
results = []
for n in n_values:
    Q_approx = k * simpson_rule(dTdx, a, b, n)
    error = abs(Q_exact - Q_approx)
    results.append((n, Q_approx, error))
    print(f"n={n}: Flujo aproximado = {Q_approx:.6f} W, Error = {error:.6e}")

# Graficar errores en función de n
plt.figure(figsize=(8,5))
plt.plot([r[0] for r in results], [r[2] for r in results], marker='o', linestyle='-', color='red')
plt.yscale("log")
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error absoluto")
plt.title("Error de la regla de Simpson en función de n (Flujo de calor)")
plt.grid()
plt.savefig("simpson_errores_calor.png")
plt.show()

# Graficar la función dT/dx y área aproximada
x_vals = np.linspace(a, b, 200)
y_vals = dTdx(x_vals)

plt.plot(x_vals, y_vals, label=r"$dT/dx = -100x$", color="blue")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(a, b, max(n_values)+1), dTdx(np.linspace(a, b, max(n_values)+1)), 
            color="red", label="Puntos de interpolación")
plt.xlabel("x (m)")
plt.ylabel("dT/dx (K/m)")
plt.legend()
plt.title("Aproximación de la integral con la regla de Simpson")
plt.grid()
plt.savefig("simpson_calor.png")
plt.show()

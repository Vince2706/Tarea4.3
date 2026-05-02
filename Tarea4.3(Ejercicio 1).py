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

# Constante del resorte
k = 200

# Función del resorte
def funcion(x):
    return k * x

# Parámetros de integración
a, b = 0.1, 0.3  # Intervalo
n_values = [6, 10, 20, 30]  # Subintervalos solicitados

# Solución exacta de la integral
# W = ∫ kx dx = (k/2)(b^2 - a^2)
W_exact = (k/2) * (b**2 - a**2)

# Calcular aproximaciones y errores
results = []
for n in n_values:
    W_approx = simpson_rule(funcion, a, b, n)
    error = abs(W_exact - W_approx)
    results.append((n, W_approx, error))
    print(f"n={n}: Trabajo aproximado = {W_approx:.6f}, Error = {error:.6e}")

# Graficar errores en función de n
plt.figure(figsize=(8,5))
plt.plot([r[0] for r in results], [r[2] for r in results], marker='o', linestyle='-', color='red')
plt.yscale("log")
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error absoluto")
plt.title("Error de la regla de Simpson en función de n (Trabajo en el resorte)")
plt.grid()
plt.savefig("simpson_errores_resorte.png")
plt.show()

# Gráfica de la función y área aproximada
x_vals = np.linspace(a, b, 100)
y_vals = funcion(x_vals)

plt.plot(x_vals, y_vals, label=r"$f(x) = 200x$", color="blue")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(a, b, max(n_values)+1), funcion(np.linspace(a, b, max(n_values)+1)), 
            color="red", label="Puntos de interpolación")
plt.xlabel("x (m)")
plt.ylabel("Fuerza (N)")
plt.legend()
plt.title("Aproximación de la integral con la regla de Simpson")
plt.grid()
plt.savefig("simpson_resorte.png")
plt.show()

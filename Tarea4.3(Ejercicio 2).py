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

# Parámetros del capacitor
C = 1e-6  # Faradios
def V(t):
    return 100 * np.exp(-2*t)  # Voltaje

# Intervalo de integración
a, b = 0, 5  # Tiempo en segundos
n_values = [6, 10, 20, 30]  # Subintervalos solicitados

# Solución analítica de la integral
# ∫ 100 e^{-2t} dt = -50 e^{-2t}
# Q = C * [ -50 e^{-2t} ]_0^5
Q_exact = C * ( -50*np.exp(-2*b) + 50*np.exp(-2*a) )

# Calcular aproximaciones y errores
results = []
for n in n_values:
    Q_approx = C * simpson_rule(V, a, b, n)
    error = abs(Q_exact - Q_approx)
    results.append((n, Q_approx, error))
    print(f"n={n}: Carga aproximada = {Q_approx:.8e} C, Error = {error:.2e}")

# Graficar errores en función de n
plt.figure(figsize=(8,5))
plt.plot([r[0] for r in results], [r[2] for r in results], marker='o', linestyle='-', color='red')
plt.yscale("log")
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error absoluto")
plt.title("Error de la regla de Simpson en función de n (Carga en el capacitor)")
plt.grid()
plt.savefig("simpson_errores_capacitor.png")
plt.show()

# Graficar voltaje y área bajo la curva
t_vals = np.linspace(a, b, 200)
V_vals = V(t_vals)

plt.plot(t_vals, V_vals, label=r"$V(t) = 100 e^{-2t}$", color="blue")
plt.fill_between(t_vals, V_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(a, b, max(n_values)+1), V(np.linspace(a, b, max(n_values)+1)), 
            color="red", label="Puntos de interpolación")
plt.xlabel("t (s)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.title("Aproximación de la integral con la regla de Simpson")
plt.grid()
plt.savefig("simpson_capacitor.png")
plt.show()

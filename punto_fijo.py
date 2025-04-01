import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Método del Punto Fijo
def metodo_punto_fijo(g, x0, tol, max_iter):
    iteraciones = []
    xr_old = x0

    for i in range(1, max_iter + 1):
        xr = g(xr_old)
        ea = abs((xr - xr_old) / xr) * 100 if xr != 0 else np.nan

        iteraciones.append([i, xr_old, xr, g(xr), ea])

        if ea < tol:
            break

        xr_old = xr

    df_iteraciones = pd.DataFrame(iteraciones, columns=['Iteración', 'X anterior', 'Xr', 'g(Xr)', 'Ea(%)'])
    return xr, df_iteraciones

# Solicitar al usuario ingresar la función g(x)
g_str = input("Ingrese la función g(x) despejada (ejemplo: (1 - x**3)): ")
g = lambda x: eval(g_str)

# Parámetros de entrada
x0 = float(input("Ingrese el valor inicial (x0): "))
tolerancia = float(input("Ingrese la tolerancia (%): "))
max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))

# Ejecutar el método del punto fijo
raiz, tabla = metodo_punto_fijo(g, x0, tolerancia, max_iteraciones)

# Mostrar la tabla
print(tabla)
print(f"\nLa raíz aproximada es: {raiz}")

# Gráfica
x_vals = np.linspace(raiz - 2, raiz + 2, 400)
y_vals = [g(x) for x in x_vals]

plt.plot(x_vals, y_vals, label='g(x)')
plt.plot(x_vals, x_vals, linestyle='--', color='gray', label='y=x')
plt.scatter(raiz, g(raiz), color='red', label=f'Raíz ≈ {raiz:.5f}')
plt.title('Método del Punto Fijo')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Método de la Secante
def metodo_secante(func, x0, x1, tol, max_iter):
    iteraciones = []

    for i in range(1, max_iter + 1):
        fx0 = func(x0)
        fx1 = func(x1)

        if fx1 - fx0 == 0:
            raise ValueError("División por cero. El método no puede continuar.")

        xr = x1 - (fx1 * (x0 - x1)) / (fx0 - fx1)
        ea = abs((xr - x1) / xr) * 100 if xr != 0 else np.nan

        iteraciones.append([i, x0, x1, xr, func(xr), ea])

        if ea < tol:
            break

        x0, x1 = x1, xr

    df_iteraciones = pd.DataFrame(iteraciones, columns=['Iteración', 'X0', 'X1', 'Xr', 'f(Xr)', 'Ea(%)'])
    return xr, df_iteraciones

# Solicitar la función al usuario
func_str = input("Ingrese la función f(x) (ejemplo: x**3 + x - 1): ")
funcion = lambda x: eval(func_str)

# Parámetros de entrada
x0 = float(input("Ingrese el primer valor inicial (x0): "))
x1 = float(input("Ingrese el segundo valor inicial (x1): "))
tolerancia = float(input("Ingrese la tolerancia (%): "))
max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))

# Ejecutar el método de la Secante
raiz, tabla = metodo_secante(funcion, x0, x1, tolerancia, max_iteraciones)

# Mostrar la tabla
print(tabla)
print(f"\nLa raíz aproximada es: {raiz}")

# Gráfica
x_vals = np.linspace(raiz - 2, raiz + 2, 400)
y_vals = [funcion(x) for x in x_vals]

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.scatter(raiz, funcion(raiz), color='red', label=f'Raíz ≈ {raiz:.5f}')
plt.title('Método de la Secante')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

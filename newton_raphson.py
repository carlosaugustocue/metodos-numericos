import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Método de Newton-Raphson
def metodo_newton_raphson(func, dfunc, x0, tol, max_iter):
    iteraciones = []
    xr_old = x0

    for i in range(1, max_iter + 1):
        fx = func(xr_old)
        dfx = dfunc(xr_old)

        if dfx == 0:
            raise ValueError("La derivada es cero. El método no puede continuar.")

        xr = xr_old - fx / dfx
        ea = abs((xr - xr_old) / xr) * 100 if xr != 0 else np.nan

        iteraciones.append([i, xr_old, xr, fx, dfx, ea])

        if ea < tol:
            break

        xr_old = xr

    df_iteraciones = pd.DataFrame(iteraciones, columns=['Iteración', 'X anterior', 'Xr', 'f(Xr)', "f'(Xr)", 'Ea(%)'])
    return xr, df_iteraciones

# Solicitar funciones al usuario
func_str = input("Ingrese la función f(x) (ejemplo: x**3 + x - 1): ")
dfunc_str = input("Ingrese la derivada f'(x) (ejemplo: 3*x**2 + 1): ")

funcion = lambda x: eval(func_str)
derivada = lambda x: eval(dfunc_str)

# Parámetros de entrada
x0 = float(input("Ingrese el valor inicial (x0): "))
tolerancia = float(input("Ingrese la tolerancia (%): "))
max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))

# Ejecutar el método de Newton-Raphson
raiz, tabla = metodo_newton_raphson(funcion, derivada, x0, tolerancia, max_iteraciones)

# Mostrar la tabla
print(tabla)
print(f"\nLa raíz aproximada es: {raiz}")

# Gráfica
x_vals = np.linspace(raiz - 2, raiz + 2, 400)
y_vals = [funcion(x) for x in x_vals]

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.scatter(raiz, funcion(raiz), color='red', label=f'Raíz ≈ {raiz:.5f}')
plt.title('Método de Newton-Raphson')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
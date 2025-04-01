import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Método de la Falsa Posición
def metodo_falsa_posicion(func, a, b, tol, max_iter):
    iteraciones = []
    xr_old = None

    if func(a) * func(b) >= 0:
        raise ValueError("La función debe tener signos opuestos en los extremos [a,b]")

    for i in range(1, max_iter + 1):
        xr = b - (func(b) * (a - b)) / (func(a) - func(b))
        fxr = func(xr)

        if xr_old is None:
            ea = np.nan
        else:
            ea = abs((xr - xr_old) / xr) * 100

        iteraciones.append([i, a, b, xr, fxr, ea])

        if func(a) * fxr < 0:
            b = xr
        else:
            a = xr

        if ea is not np.nan and ea < tol:
            break

        xr_old = xr

    df_iteraciones = pd.DataFrame(iteraciones, columns=['Iteración', 'a', 'b', 'Xr', 'f(Xr)', 'Ea(%)'])
    return xr, df_iteraciones

# Solicitar al usuario ingresar la función
funcion_str = input("Ingrese la función en términos de x (ejemplo: x**3 + x - 1): ")
funcion = lambda x: eval(funcion_str)

# Parámetros de entrada
a = float(input("Ingrese el límite inferior (a): "))
b = float(input("Ingrese el límite superior (b): "))
tolerancia = float(input("Ingrese la tolerancia (%): "))
max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))

# Ejecutar el método de falsa posición
raiz, tabla = metodo_falsa_posicion(funcion, a, b, tolerancia, max_iteraciones)

# Mostrar la tabla
print(tabla)
print(f"\nLa raíz aproximada es: {raiz}")

# Gráfica
x_vals = np.linspace(a - 1, b + 1, 400)
y_vals = [funcion(x) for x in x_vals]

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.scatter(raiz, funcion(raiz), color='red', label=f'Raíz ≈ {raiz:.5f}')
plt.title('Método de la Falsa Posición')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

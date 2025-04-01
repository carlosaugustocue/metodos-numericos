# Proyecto Métodos Numéricos

Este proyecto contiene una serie de aplicaciones en Python que implementan diversos métodos numéricos utilizados para hallar raíces de ecuaciones. Cada método incluye un código claro, documentado, gráficos explicativos y tablas detalladas con resultados por iteración.

## Métodos Implementados

- **Bisección**
- **Falsa Posición**
- **Punto Fijo**
- **Newton-Raphson**
- **Secante**

## Características del Proyecto

Cada método numérico cuenta con:

- **Ingreso personalizado de funciones** desde consola.
- **Tablas de iteraciones** que muestran claramente:
  - Número de iteración
  - Valores de a, b (según aplique)
  - Valor aproximado de la raíz (Xr)
  - Valor de la función en la raíz aproximada f(Xr)
  - Error aproximado Ea (%)
- **Gráficas visuales** que indican claramente la función analizada y el punto aproximado de la raíz.

## Tecnologías Utilizadas

- **Python**
- **NumPy**
- **Matplotlib**
- **Pandas**

## Requisitos

Instalar las siguientes bibliotecas antes de ejecutar:

```bash
pip install numpy matplotlib pandas
```

## Ejecución del Proyecto

Clona este repositorio y ejecuta los scripts desde tu consola:

```bash
python biseccion.py
python falsa_posicion.py
python punto_fijo.py
python newton_raphson.py
python secante.py
```

Cada script pedirá ingresar los valores requeridos directamente desde consola.

## Ejemplo de Uso

```
Ingrese la función en términos de x (ejemplo: x**3 + x - 1): x**3 + x - 1
Ingrese el límite inferior (a): 0
Ingrese el límite superior (b): 1
Ingrese la tolerancia (%): 0.0001
Ingrese el número máximo de iteraciones: 20
```

## Autor

- **Carlos Augusto Aranzazu**

---

¡Disfruta explorando métodos numéricos con este proyecto!


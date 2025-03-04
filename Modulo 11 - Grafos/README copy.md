# Introducción

## Reglas del curso
- Estudiar individualmente.
- Las prácticas son INDIVIDUALES. Los ejercicios y/o soluciones se pueden discutir, pero cada uno debe subir su propio codigo
- Estudio constante y disciplina al desarrollar las actividades individuales.

## Requisitos
- Fundamentos de programación.
- Programación orientada a objetos.

# ¿Qué es una estructura de datos?
Una estructura de datos es una forma partucular de almacenar y manipular una serie de datos en la computadora para que estos puedan ser utilizados de manera eficiente en un determinado algoritmo.

## ¿Qué es un Dato?
- Primitivos: tipos de datos base integrados en el lenguaje de programación [!NOTE]
  - Enteros
  - Booleanos
  - Reales
- Compuestos: Tipos de datos creados por el desarrollador.
  - Clases

## Eficiencia.
Es lo que busco al desarrollar un algoritmo que me permita para poder usar la menor cantidad de memoria, y manipular la información lo más rápido posible.
La eficiencia irá enfocada al objetivo que yo quiera lograr, la solución más eficiente siempre depende del objetivo que estoy buscando.

# Eficiencia algorítmica

## ¿Cómo medir la `Eficiencia` de un algoritmo?
- Calculando la velocidad de las operacione realizadas. `f`
- Calculando la cantidad de memoria utilizada. `g`

### Ejemplo.
**Utilizaremos el siguente codigo para a prender a calcular la eficiencia de un algoritmo:**
Este ejercicio calcula la sumatoria de un número N.
```python
N = int(input())
suma = 0

num = list(range(1, N+1))
print(suma)
```
Por simplisidad toda operación tendrá un valor de: 1
Los ciclos tendrá un valor de: N

en esta solución gasté:
N + 3 operaciones
Memoria: 3 (**Estoy utilizando 3 espacios de memoria.**)

*La solución más eficiente es:*
```
N = int(input())
print(N*(N+1)/2)
```
- `f` = 2
- `g` = 1

## Notación Big O.
> [!NOTE]
> El mismo algoritmo en diferentes lenguajes puede tener una diferente eficiencia algorítmica.

Se calcula de la siguente manera:
1. Se considera el peor escenario: se calcula la mayor cantidad posible de operaciones(En caso de haber condicionales, ciclos condicionados, recursiones, etc.).
1.
  1. Se realiza un análsis asintotico: Se considera valores grandes de N(por convención N es el "Tamaño de la entrada")
  2. Se le presta atención a la forma de la función, más que a sus valores puntuales: se eliminan los términos constantes y de menor orden.

Aunque esta notación no es rigurosa, y no se debe usar como un preditor exacto del consumo de recursos de un aloritmo, si da cuenta de su comportamiento o tasa de crecimiento, considerando el peor escenario, respecto al tamaño de la entrada.

Decimos entonces que un algoritmo es mejor(más eficiente) que otro si su "O" es menor respecto a:
- Procesador
- Memoria


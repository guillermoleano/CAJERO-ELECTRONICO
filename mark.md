🧮 Calculadora Básica en Python

## 📌 Descripción del Programa

Este programa implementa una **calculadora básica en Python** que permite realizar cuatro operaciones matemáticas fundamentales:

- Suma
- Resta
- Multiplicación
- División

El usuario selecciona una opción desde la consola, ingresa dos números, y el programa ejecuta la operación correspondiente mostrando el resultado.

Es un ejemplo práctico para comprender:

- Definición de funciones
- Uso de condicionales (`if/elif/else`)
- Entrada de datos con `input()`
- Conversión de tipos con `float()`
- Manejo básico de errores
- Uso de f-strings

---

## 🏗 Estructura del Código

El código está organizado en dos partes principales:

1. **Definición de funciones matemáticas**
2. **Lógica principal del programa (interacción con el usuario)**

```python
# Funciones

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

```
BIENVENIDA
```python


print("Bienvenido a la calculadora")
print("1 → Suma")
print("2 → Resta")
print("3 → Multiplicación")
print("4 → División")


```

```python

opcion = input("Elige una opción (1/2/3/4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

```

```python

if opcion == "1":
    resultado = suma(num1, num2)
elif opcion == "2":
    resultado = resta(num1, num2)
elif opcion == "3":
    resultado = multiplicacion(num1, num2)
elif opcion == "4":
    resultado = division(num1, num2)
else:
    resultado = "Opción inválida"

print(f"El resultado es: {resultado}")

```



ESTRUCTURA
```python
    int
```
```python
    print
```
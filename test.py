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


print("Bienvenido a la calculadora")
print("1 → Suma")
print("2 → Resta")
print("3 → Multiplicación")
print("4 → División")

opcion = input("Elige una opción (1/2/3/4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

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
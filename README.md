# Explicacion paso a paso del cajero electronico.
![Cajero electrónico](https://clipart-library.com/2023/set-realistic-atm-machine-isolated-atm-bank-cash-machine-with-interface-keypad-slot-card_320857-1122.jpg)
*Este es un proyecto en el cual se puede apreciar como funciona un cajero electronico
dentro de codigos como fue echo y como funciona.*

### Donde se hizo
 
_en esta situacion trabajamos con **python** en el visual code studio_

-----------
## Explicacion paso a paso.

#### 1. Se define la funcion:

    def cajero_automatico():
        saldo = 1000
        print("bienvenido al cajero automatico")

-----------------

#### 2. Inicializacion de la variable.

    saldo = 1000 __establece el saldo inicial en 1000__
        print("bienvenido al cajero automatico")

    operaciones = int(input("cuantas operaciones deseas realizar hoy:"))

--------------

solicita al usuario el numero de operaciones que desea realizar.


#### 3. Bucle while: 

    while operaciones > 0:

* muestra las opciones disponibles


        print("1. consultar el saldo")

        print("2. retirar dinero")

        print("3. depositar dinero")

        print("4. Cambio de pin")

* Solicita al usuario que seleccione una opcion:
   ``` opcion = int(input("seleccione una opcion:"))```

-----------------

#### 4. Opciones:

###### * Consultar saldo: 
muestra el saldo inicial.

    if opcion == 1:
            print(f"su saldo actual es: {saldo}")
###### * Retirar dinero:
solicita el monton a retirar.

    elif opcion == 2:
            monto_retirar = int(input("ingrese el monto a              retirar:")).

* verifica si el saldo es suficiente:

        if monto_retirar > saldo:
                print("fondos insuficientes")

* si es suficiente, resta el monton del saldo:

        else:
                saldo -= monto_retirar
                print(f"ha retirado: {monto_retirar}. su nuevo saldo es: {saldo}")

###### * Depositar dinero:
* solicita el monto a depositar:
* y suma el monto al saldo:

        elif opcion == 3:
                monto_depositar = int(input("ingrese el monto a depositar:"))
                saldo += monto_depositar
                print(f"ha depositado: {monto_depositar}. su nuevo saldo es: {saldo}")

###### * Cambio de pin:
no implementado correctamente.

        elif opcion == 4:
            pin_actual = input("ingrese su pin actual: ")
            nuevo_pin = input("ingrese su nuevo pin: ")
            confirmar_pin = input("confirme su nuevo pin: ")
            if nuevo_pin == confirmar_pin:
                print("pin cambiado exitosamente")
            if nuevo_pin != confirmar_pin:
                print("los pines no coinciden, intente nuevamente")


5. __Fin del bucle while:__

        else:
            print("opcion no valida")
            operaciones += 1
        operaciones -= 1
        cajero_automatico()# cajero-electronico.py

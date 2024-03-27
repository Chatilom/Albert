import random
from time import *

def adivinar():
    try:
        global aleatorio , intentos
        intento = int(input("Pruebe un número: "))
        if intento < aleatorio:
            print("El número es mas alto, pruebe otra vez")
            intentos += 1
            adivinar()
        elif intento > aleatorio:
            print("El número es mas bajo, pruebe otra vez")
            intentos += 1
            adivinar()
        elif intento == aleatorio:
            print("Victoria, número de intentos:" , intentos)
            sleep(3)
            funcionador()
    except ValueError:
        print("Valor incorrecto, recuerde indicar un numero entero")
        intentos += 1
        adivinar()
def generador():
    global aleatorio , intentos
    print("1.Básico. 1-50")
    print("2.Extremo. 1-1000")
    print("3.Personalizado")
    modo = int(input("Seleccione el modo de juego: "))
    if modo == 1:
        num1 = 1
        num2 = 50
    elif modo == 2:
        num1 = 1
        num2 = 1000
    elif modo == 3:
        num1 = int(input("Selccione el primer numero: "))
        num2 = int(input("Seleccione el segundo número: "))
    else:
        print("Eleccion incorrecta")
        generador()
    intentos = 0
    aleatorio = random.randint(num1 , num2)

def funcionador():
    generador()
    adivinar()
    
funcionador()
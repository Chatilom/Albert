def celsius_kelvin():
    inicial = float(input("Seleccione la temperatura en celsius: "))
    resultado = inicial + 274.15
    print(inicial , "grados son" , resultado , "kelvin")
def celsius_fahrenheit():
    inicial = float(input("Seleccione la temperatura en celsius: "))
    resultado = (inicial * 1.8) + 32
    print(inicial , "grados celsius son" , resultado , "fahrenheit" )
def kelvin_celsius():

    inicial = float(input("Indique la temperatura en kelvin: "))
    resultado = inicial - 274.15
    print(inicial , "kelvin son" , resultado , "grados celsius")
def kelvin_fahrenheit():
    inicio = float(input("Seleccione la temperatura en kelvin: "))
    resultado = 1.8 * (inicio - 273) + 32
    print(inicio , "kelvin son" , resultado , "fahrenheit")
def fahrenheit_celsius():
    inicio = float(input("Seleccione la temperatura en fahrenheit: "))
    resultado = (inicio - 32) / 1.8
    print(inicio , "fahrenheit son" , resultado , "grados centígrados")
def fahrenheit_kelvin():
    inicio = float(input("Indique la temperatura en fahrenheit: "))
    resultado = ((inicio - 32) / 1.8) + 273.15
    print(inicio , "fahrenheit son" , resultado , "kelvin")

while True:
    print("1.Celsius")
    print("2.Kelvin")
    print("3.Fahrenheit")

    temp1 = int(input("Seleccione la temperatura que desea convertir: "))
    temp2 = int(input("Seleccione la temperatura a la que la quiera convertir: "))
    if temp1 == 1 and temp2 == 2:
        celsius_kelvin()
    elif temp1 == 1 and temp2 == 3:
        celsius_fahrenheit()
    elif temp1 == 2 and temp2 == 1:
        kelvin_celsius()
    elif temp1 == 2 and temp2 == 3:
        kelvin_fahrenheit()
    elif temp1 == 3 and temp2 == 1:
        fahrenheit_celsius()
    elif temp1 == 3 and temp2 == 2:
        fahrenheit_kelvin()
    else: 
        print("Introduzca valores correctos")

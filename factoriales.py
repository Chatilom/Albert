def factorial(entrada): 
    factorial = 1
    numero = int(entrada)
    for i in range(1 , (numero + 1)):
        factorial *= i
    return factorial

def validacion():
    global numero
    try: 
      numero = int(input("Indique un número entero: ")) 
      neg()             
    except ValueError:
       print("Valor incorrecto")
       validacion()
       return numero

def neg():
    int(numero)
    if numero < 0:
        print("Introduzca un valor postivo")
        validacion()
    else:
       print(factorial(numero))
       validacion()

validacion()
   
   



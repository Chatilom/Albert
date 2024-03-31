import string

diccionario = {}
esp = string.punctuation
num = string.digits
lista_esp = list(esp)
lista_num = list(num)

        
def crear_contraseña():
    global contraseña
    c_esp = False
    c_num = False
    contraseña = input("Indique su contraseña: ")
    for i in contraseña:
        if i in lista_esp:
            c_esp = True
    for i in contraseña:
        if i in lista_num:
            c_num = True
    if c_esp and c_num == True:
        diccionario[nombre] = contraseña
        print("usuario creado con éxito")
    else:
        print("Contraseña no segura, recuerde incluir al menos un número y un carácter especial")
        crear_contraseña()
    
def usuario():
    global nombre
    nombre = input("Nombre de usuario: ").strip()
    if nombre in diccionario:
        print("nombre de usuario no disponible")
        usuario()
    else:
        crear_contraseña()    

def iniciar():
    nombre = input("Nombre de usuario: ").strip()
    contraseña = input("indique la contraseña: ").strip()
    if nombre in diccionario and diccionario[nombre] == contraseña:
        print("Bienvenido " + nombre)
    else:
        print("usuario no encontrado, pruebe nuevo")
        iniciar()

        
while True:
    nombre = ""
    contraseña = ""
    print("1.Iniciar sesión")
    print("2.Crear usuario")
    eleccion = input("Elegir una opción: ").strip()
    if eleccion == "1":
        iniciar()
    elif eleccion == "2":
        usuario()
    else:
        print("error")
        
#ARREGLAR EL ERROR CON LOS ESPACIOS. Echo
#Verificar que el nombre de usuario esté disponible. Echo
#Validacion de contraseñas, crear contraseñas mas seguras y reescribir contraseña. echo
#Guardar usuarios en base de datos
#crear interfaz de usuario(lo mismo hace falta otro programa)



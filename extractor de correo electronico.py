try: 
    def extractor():
        correo = input("Ingrese su dirección de correo: ")
        extension = correo[correo.index("@") + 1:]
        nombre = correo[:correo.index("@")]
        print("Se está usando la extension:" , extension)
        print("Nombre de usuario:" , nombre)
        extractor()
except ValueError:
        print("Introduzca un correo válido")
extractor()
    





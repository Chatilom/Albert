from tkinter import *
import random

#colores = ["blue" , "yellow" , "green" , "oranje" , "purple" , "white" , "black"]
#-------------------------------raiz---------------------------------------------------------------------
raiz = Tk()
raiz.iconbitmap(r"C:\Users\alber\Desktop\phyton\graficos\depositphotos_23689481-stock-photo-calculator.ico")
raiz.title("Calculadora")
frame = Frame()
frame.pack()

operacion = ""
resultado = 0

numpantalla = StringVar()
#-------------------------------raiz---------------------------------------------------------------------

#-------------------------------pantalla---------------------------------------------------------------------
pantalla = Entry(frame , textvariable=numpantalla , justify="right" , bg="red" , fg="blue")
pantalla.grid(row=1 , column=1 , columnspan=4 ,  padx=10 , pady=5)

def pulsar(num):
    global operacion
    global paligual
    if operacion != "":
        numpantalla.set(num)
        paligual = "suma"
        operacion = ""
    else:
        numpantalla.set(numpantalla.get() + num)

#-------------------------------suma------------------------------------------------------
def suma(num):
    global operacion
    global resultado
    resultado += float(num)
    operacion = "suma"
    numpantalla.set(resultado)

def igual(): 
    global resultado
    global paligual
    if paligual == "suma":
        numpantalla.set(int(numpantalla.get()) + resultado)
        resultado = 0
#-------------------------------pantalla---------------------------------------------------------------------

#-------------------------------fila-1---------------------------------------------------------------------
boton_7 = Button(frame , text="7" , command=lambda:pulsar("7"))
boton_7.grid(row=2 , column=1 , sticky=NSEW)
boton_7.config(activebackground="blue" , width=5)

boton_8 = Button(frame , text="8" , command=lambda:pulsar("8"))
boton_8.grid(row=2 , column=2 , sticky=NSEW)
boton_8.config(activebackground="blue" , width=5)

boton_9 = Button(frame , text="9" , command=lambda:pulsar("9"))
boton_9.grid(row=2 , column=3 , sticky=NSEW)
boton_9.config(activebackground="blue" , width=5)

boton_div = Button(frame , text="/")
boton_div.grid(row=2 , column=4 , sticky=NSEW)
boton_div.config(width=5)


#-------------------------------fila-2---------------------------------------------------------------------
boton_4 = Button(frame , text="4" , command=lambda:pulsar("4"))
boton_4.grid(row=3 , column=1 , sticky=NSEW)
boton_4.config(activebackground="yellow" , width=5)

boton_5 = Button(frame ,text="5" , command=lambda:pulsar("5"))
boton_5.grid(row=3 , column=2 , sticky=NSEW)
boton_5.config(activebackground="yellow" , width=5)

boton_6 =Button(frame , text="6" , command=lambda:pulsar("6"))
boton_6.grid(row=3 , column=3 , sticky=NSEW)
boton_6.config(activebackground="yellow" , width=5)

boton_mult = Button(frame , text="X")
boton_mult.grid(row=3 , column=4 , sticky=NSEW)
boton_mult.config(width=5)


#-------------------------------fila-3---------------------------------------------------------------------
boton_1 = Button(frame , text="1" , command=lambda:pulsar("1"))
boton_1.grid(row=4 , column=1 , sticky=NSEW)
boton_1.config(activebackground="green" , width=5)

boton_2 = Button(frame , text="2" , command=lambda:pulsar("2"))
boton_2.grid(row=4 , column=2 , sticky=NSEW)
boton_2.config(activebackground="green" , width=5)

boton_3 = Button(frame , text="3" , command=lambda:pulsar("3"))
boton_3.grid(row=4 , column=3 , sticky=NSEW)
boton_3.config(activebackground="green" , width=5)

boton_rest = Button(frame , text="-")
boton_rest.grid(row=4 , column=4 , sticky=NSEW)
boton_rest.config(width=5)

#-------------------------------fila-4---------------------------------------------------------------------
boton_0 = Button(frame , text="0" , command=lambda:pulsar("0"))
boton_0.grid(row=5 , column=1 , sticky=NSEW)
boton_0.config(width=5)

boton_coma = Button(frame , text="," , command=lambda:pulsar("."))
boton_coma.grid(row=5 , column=2 , sticky=NSEW)
boton_coma.config(width=5)

boton_ig = Button(frame , text="=" , command=igual)
boton_ig.grid(row=5 , column=3 , sticky=NSEW)
boton_ig.config(width=5)

boton_sum = Button(frame , text="+" , command=lambda:suma(numpantalla.get()))
boton_sum.grid(row=5 , column=4 , sticky=NSEW)
boton_sum.config(width=5)

raiz.mainloop()
from tkinter import *
raiz = Tk()
raiz.geometry("400x400")
raiz.config(bg="blue")
raiz.title("Odio latam")

def ventana(color1 , color2):
    ventana = Tk()
    ventana.geometry("300x200")
    ventana.config(bg=color1)
    textote = Label(ventana , text=entrada.get())
    textote.place(x=50 , y="100")
    textote.config(fg=color2 , bg=color1 , font=30)

frame1 = Frame(raiz , width=200 , height=200)
frame1.place(x=0 , y=0)
frame1.config(bg="yellow" , cursor="heart")

frame2 = Frame(raiz , width=200 , height=200)
frame2.place(x=200 , y=0)
frame2.config(bg="red" , cursor="pirate")

botonsete = Button(raiz , width=4 , height=1 , text="pulsa" , command=lambda:ventana("yellow" , "blue"))
botonsete.config(bg="yellow" , activebackground="black")
botonsete.place(x=100 , y=250)

botonsete2 = Button(raiz , width=4 , height=1 , text="pulsa" , command=lambda:ventana("purple" , "orange"))
botonsete2.config(bg="purple" , fg="white")
botonsete2.place(x=100 , y=300)

entrada = Entry(raiz)
entrada.place(x=250 , y=300)

raiz.mainloop()
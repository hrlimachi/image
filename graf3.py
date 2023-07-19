from tkinter import *

raiz = Tk()
raiz.title("ventana de pruebas")
# raiz.resizable(1, 1)
raiz.iconbitmap("Scott.ico")
# raiz.geometry("650x350")
raiz.config(bg="olivedrab1")

miFrame = Frame(raiz, width=500, height=400)
miFrame.pack()
miFrame.config(bg="lightgreen")
miImagen = PhotoImage(file="image_01.png")
# Label(miFrame, text="Hola mundo", fg="orange", font=("Comic Sans MS", 18)).place(x=100, y=200)
Label(miFrame, image=miImagen).place(x=100, y=200)
raiz.mainloop()

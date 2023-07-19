from tkinter import *

raiz = Tk()
raiz.title("ventana de pruebas")
# raiz.resizable(1, 1)
raiz.iconbitmap("Scott.ico")
# raiz.geometry("650x350")
raiz.config(bg="olivedrab1")

miFrame = Frame()
miFrame.pack()
miFrame.config(bg="lightgreen")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="ridge")
miFrame.config(cursor="pirate")
raiz.mainloop()

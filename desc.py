from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox


def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()


def popup():
    MessageBox.showinfo("sobre mi", "enlace a mi perfil:\nhttps://youtube.com")


root = Tk()
root.config(bd=15)
root.title("Script descargar videos")

imagen = PhotoImage(file="youtube.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para mas info", menu=helpmenu)
helpmenu.add_command(label="infor del autor", command=popup)

menubar.add_command(label="salir", command=root.destroy)

instrucciones = Label(
    root, text="programa creado en Python para descargar videos de YouTube\n"
)
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=2, column=1)

boton = Button(root, text="Descargar :)", command=accion)
boton.grid(row=3, column=1)

root.mainloop()

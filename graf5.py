from tkinter import *
from PIL import Image, ImageTk
import cv2
import imutils
import numpy as np

# ventana principal
# Pantalla
pantalla = Tk()
pantalla.title("GUI | Tkinter")
pantalla.geometry("1280x720")

# fondo
imagenF = PhotoImage(file="image_01.png")
background = Label(image=imagenF, text="Fondo")
background.place(x=0, y=0, relwidth=1, relheight=1)

# interfaz

texto1 = Label(pantalla, text="Video en tiempo real")

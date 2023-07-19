import cv2
import numpy as np

# Crea una imagen en blanco con dimensiones 500x500 y 3 canales (BGR)
width, height = 500, 500
blank_image = np.zeros((height, width, 3), np.uint8)

# Muestra la imagen en una ventana
cv2.circle(blank_image, (100, 200), 6, (128, 0, 255), -1)
cv2.imshow("Ventana en blanco", blank_image)

# Espera hasta que se presione una tecla

cv2.waitKey(0)

# Cierra todas las ventanas
cv2.destroyAllWindows()

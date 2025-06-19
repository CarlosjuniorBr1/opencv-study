import numpy as np
from matplotlib import pyplot as plt
import cv2 


obj_img = cv2.imread("img/im2.jpg")

plt.imshow(obj_img)  # constroi a janela com a imagem
plt.show() # exibe a janela


#invertendo as cores de bgr -> rgb
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
plt.imshow(obj_img)
plt.show()

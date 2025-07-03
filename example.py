import numpy as np
from matplotlib import pyplot as plt
import cv2 

def showImage(img):
    #invertendo as cores de bgr -> rgb
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()
    
def main():
    # obj_img = cv2.imread("img/im2.jpg")
    obj_img = cv2.imread("img/im2.jpg") #passando o segundo parametro com 0 a imagem é carregada como preto e branco
    
    #print(obj_img.shape) # mostra infos da imagem: altura, largura, quantos canais de cores
    
    altura, largura, canais_de_cor = obj_img.shape
    print("Dimensoes da Imagem: " + str(altura) + "x" + str(largura))
    print("Canais de cor: ", canais_de_cor)
    # showImage(obj_img)
    
    
    #percorrendo uma imagem, vai primeiro nas colunas dps nas linhas
    
    for y in range(0, altura):
        for x in range(0, largura):
            # print("[" + str(x) + ","+ str(y) +"] = " + str(obj_img[x][y]))
            azul = obj_img.item(y,x, 0)
            verde = obj_img.item(y,x,1)
            vermelho = obj_img.item(y,x,2)
            
            obj_img.itemset((y,x, 1), 0) 

main()
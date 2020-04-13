import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d


def HSV_control(im_rgb):
    
    #Função que controla a HUE
    def H_layer(x):
        H = cv2.getTrackbarPos('H','image')

        im_HSV_copy[:,:,0] = im_HSV[:,:,0] + H
        #Converte im_r de HSV para RGB.

        im_rf = cv2.cvtColor(im_HSV_copy, cv2.COLOR_HSV2BGR)

        #Printa na tela a imagen.
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 1000,600)
        cv2.imshow('image',im_rf)
        return

    #Função que controla a SATURATION
    def S_layer(x):
        S = cv2.getTrackbarPos('S','image')
        im_HSV_copy[:,:,1] = im_HSV[:,:,1] + S

        #Converte im_r de HSV para RGB.
        im_rf = cv2.cvtColor(im_HSV_copy, cv2.COLOR_HSV2BGR)

        #Printa na tela a imagen.
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 1000,600)
        cv2.imshow('image',im_rf)
        return

    #Função que controla O VALUE
    def V_layer(x):
        V = cv2.getTrackbarPos('V','image')
        im_HSV_copy[:,:,2] = im_HSV[:,:,2] + V
        #Converte im_r de HSV para RGB.

        im_rf = cv2.cvtColor(im_HSV_copy, cv2.COLOR_HSV2BGR)

        #Printa na tela a imagen.
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 1000,600)
        cv2.imshow('image',im_rf)
        return

    def callback_func(x):
        return

    #Convertendo de RGB para HSV.
    im_HSV = cv2.cvtColor(im_rgb, cv2.COLOR_RGB2HSV)
    im_HSV_copy = im_HSV.copy()

    #Cria uma janela com a tag 'image'.
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)


    #Criando as track bars para H,S e V.
    cv2.createTrackbar('H','image',0,180,H_layer)
    cv2.createTrackbar('S','image',0,255,S_layer)
    cv2.createTrackbar('V','image',0,255,V_layer)
    
    
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 1000,600)
    cv2.imshow('image',cv2.cvtColor(im_rgb,cv2.COLOR_RGB2BGR))


    while(1):

        #Espera que seja pressionado o botão 'ESC' para fecha a tela da imagen.
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    
    w = cv2.cvtColor(im_HSV_copy,cv2.COLOR_HSV2BGR)

    return w
    
    

#Leio a imagem
im = cv2.imread('Flag_of_Brazil.png')

#Converto a imagem de BGR para RGB.
im_rgb = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
saida = HSV_control(im_rgb)
plt.imshow(saida,'gray')
plt.show()
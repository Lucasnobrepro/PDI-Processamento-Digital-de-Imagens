import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
  pass


def thresHold(img):

    def confWindon(w,h):
        cv2.namedWindow('red',cv2.WINDOW_NORMAL)
        cv2.namedWindow('green',cv2.WINDOW_NORMAL)
        cv2.namedWindow('blue',cv2.WINDOW_NORMAL)
        
        cv2.resizeWindow('red',w,h)
        cv2.resizeWindow('green',w,h)
        cv2.resizeWindow('blue',w,h)

    def minValue(x):
        # Pego a posição na BARRA
        minVar_B = cv2.getTrackbarPos('Value B',wnd)
        minVar_G = cv2.getTrackbarPos('Value G',wnd)
        minVar_R = cv2.getTrackbarPos('Value R',wnd)
        op = cv2.getTrackbarPos('Opcao salvar',wnd)

        # Aplico o ThrashHold
        ret,im_thresh_B = cv2.threshold(B, minVar_B,255,cv2.THRESH_BINARY_INV)
        ret,im_thresh_G = cv2.threshold(G, minVar_G,255,cv2.THRESH_BINARY_INV)
        ret,im_thresh_R = cv2.threshold(R, minVar_R,255,cv2.THRESH_BINARY_INV)

        # Configuro a tela
        confWindon(200,200)

        cv2.imshow('red',im_thresh_R)
        cv2.imshow('green',im_thresh_G)
        cv2.imshow('blue',im_thresh_B)
        
        if op == 1:
            im_thresh = im_thresh_B
            cv2.imshow(wnd,im_thresh)
            
        elif op == 2:
            im_thresh = im_thresh_G
            cv2.imshow(wnd,im_thresh)
            
        elif op == 3:
            im_thresh = im_thresh_R
            cv2.imshow(wnd,im_thresh)
            
        else:
            im_thresh = im
            cv2.imshow(wnd,im_thresh)
        
        cp[:,:] = im_thresh[:,:]
        print(op)
        return

    im = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    im_thresh = im.copy()
    cp = im.copy()

    B, G, R = cv2.split(img)

    cv2.namedWindow('Colorbars')

    wnd = 'Colorbars'
    cv2.createTrackbar("Value B", "Colorbars",0,255,minValue)
    cv2.createTrackbar("Value G", "Colorbars",0,255,minValue)
    cv2.createTrackbar("Value R", "Colorbars",0,255,minValue)
    cv2.createTrackbar("Opcao salvar", "Colorbars",0,3,minValue)
    cv2.imshow(wnd,img)


    while(1):
        k = cv2.waitKey(0) & 0xFF
        
        if k == 27:
            break

    return cp

'''# Teste
img = cv2.imread('cuphead.jpg')

fim = thresHold(img=img)

cv2.imshow('fim',fim)

while(1):
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()'''




# Fim

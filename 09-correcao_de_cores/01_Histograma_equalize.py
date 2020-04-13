import numpy as np
import cv2
from matplotlib import pyplot as plt

def equalise_hist(img):
    
    img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
    img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
    hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2RGB)
    
    return hist_equalization_result

#TESTE
'''
img = cv2.imread('cuphead.jpg')
plt.imshow(equalise_hist(img))
plt.show()
plt.close()
'''

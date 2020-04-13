import cv2

def selection(img):
    r = cv2.selectROI("Image", img, False, False)
    # Crop image
    imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    #fecha a tela com ESC
    while(1):
        k = cv2.waitKey(0) & 0xff
        if k == 27:
            break

    cv2.destroyAllWindows()

    return imCrop


'''# Teste

img = cv2.imread("cuphead.jpg")
c = selection(img)

cv2.imshow('recorte',c)

while(1):
    k = cv2.waitKey(0) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()'''
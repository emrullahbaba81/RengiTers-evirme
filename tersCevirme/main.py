import cv2
resim = cv2.imread('manzara.jpg')
cv2.imshow("ilk resim",resim)
def renk_degistirme(resim):
    h = resim.shape[0]
    w = resim.shape[1]
    for y in range(0, h):
        for x in range(0, w):
            b = resim[y, x, 0]
            g = resim[y, x, 1]
            r = resim[y, x, 2]

            b = 255 - b
            g = 255 - g
            r = 255 - r
            resim[y, x, 0] = b
            resim[y, x, 1] = g
            resim[y, x, 2] = r
    return resim

resim = cv2.imread('manzara.jpg')
renk_degistirme(resim)
cv2.imwrite('output.jpg', resim)
cv2.imshow('test',resim)
cv2.waitKey(0)
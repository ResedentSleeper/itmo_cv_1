import cv2
import numpy as np

# Set primitive 3x3
primitive = np.array([[255, 255, 255],
                     [255, 255, 255],
                     [255, 255, 255]],  np.uint8)
m0 = np.zeros((3, 3))
isErosion = 0

# Camera Capture 
cap = cv2.VideoCapture(0)
cap.set(3, 600)

while True:
# Converting an image to a gray background and binarizing it
    succes, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  

    if  isErosion==True:
           img = cv2.erode(img, primitive,iterations = 1)

    cv2.imshow("res", img)
    cv2.imwrite('res/1_result.jpg', img)
    k = cv2.waitKey(10)

# Switch erosion filter
    if k == ord('1'):
        isErosion = not isErosion



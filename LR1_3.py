import time
import cv2
import numba
import numpy as np

# Function to compare two arrays with optimization by Numba’s JIT compiler
@numba.jit()
def func_equal(a, b):
    y1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    y2 = np.zeros((3, 3))
    k=0
    for i in range(0,3):
        for j in range(3):
            if a[i][j] == b[i][j]:
                  k += 1
    if k == 9:
        y=255
    else:
        y=0
    return y

# Set primitive 3x3
primitiv = np.array([[255, 255, 255],
                     [255, 255, 255],
                     [255, 255, 255]])
m0 = np.zeros((3, 3))
isErosion = 0

# Camera Capture 
cap = cv2.VideoCapture(0)
cap.set(3, 600)


while True:
# Converting an image to a gray background and binarizing it
    img = cv2.imread('photo_2.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # cv2.THRESH_BINARY=0?

    i = 0
    j = 0

    if isErosion:
        start_time = time.time()
        n0 = np.zeros(img.shape)

        # Passing through horizontally and vertically
        while i < img.shape[0] -1:
            while j < img.shape[1] - 1:

                n0[i+1][j+1]=func_equal(img[i:i + 3, j:j + 3],primitiv[0:3, 0:3])
                j=j+1
            i = i + 1
            j = 0
        img = n0
        print("Execution time: ", time.time()-start_time)
        
    cv2.imshow("res", img)
    cv2.imwrite('res/3_result.jpg',img)
    k = cv2.waitKey(10)

    if k == ord('1'):
        isErosion = not isErosion
        print(isErosion)



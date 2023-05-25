import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgL = cv.imread('img/tsukuba_l.png',0)
imgR = cv.imread('img/tsukuba_r.png',0)

cv.imshow("Original L", imgL)
cv.imshow("Original R", imgR)

stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)

plt.imshow(disparity,'gray')
plt.show()
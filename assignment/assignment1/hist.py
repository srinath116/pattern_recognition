import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('input.jpeg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist(img,[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
#print(img)
plt.show()

while True:
    k = cv2.waitKey(0) & 0xFF     
    if k == 27: break             # ESC key to exit 
cv2.destroyAllWindows()

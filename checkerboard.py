
import numpy as np
import cv2
b=np.zeros([240,240],dtype='uint8')
for i in range(30,400,60):
 for j in range(30,400,60):
  b[j-30:j,i-30:i]=255
  b[j:j+30,i:i+30]=255
cv2.imshow('checker board 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()

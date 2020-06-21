
import numpy as np
import cv2
n=int(50)
b=np.zeros([400,400],dtype='uint8')
for i in range(n,400,n*2):
 for j in range(n,400,n*2):
  b[j-n:j,i-n:i]=255
  b[j:j+n,i:i+n]=255
cv2.imshow('checker board 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt
import numpy as np


image=cv2.imread("images.jpeg")
rows,cols=image.shape[:2]
(h,w)=image.shape[:2]


flipped=cv2.flip(image,1)
cropped=image[50:100,100:300]
resize=cv2.resize(image,(200,400))

M=np.float32([[1,0,-10],[0,1,0]])
translate=cv2.warpAffine(image,M,(cols,rows))

RM=cv2.getRotationMatrix2D((w//2,h//2),45,1.0)
rotated=cv2.warpAffine(image,RM,(w,h))

scaled=cv2.resize(image,None,fx=2,fy=2)
line=cv2.line(image,(500,500),(200,500),(0,255,0),2)
rectangle=cv2.rectangle(image,(200,200),(500,70),(255,0,0),2)
circle=cv2.circle(image,(700,700),100,(0,0,255),2)
cv2.putText(image,"OpenCV",(500,1000),cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2)

plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
cv2.imwrite("output.jpeg",image)
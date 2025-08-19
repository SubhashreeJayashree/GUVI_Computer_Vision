import cv2
import matplotlib.pyplot as plt
img=cv2.imread("images.jpeg")
print(img.shape)
line=cv2.line(img,(500,500),(100,100),(0,0,255),2)
circle=cv2.circle(img,(500,500),100,(0,0,255),2)
plt.axis("off")
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
resize=cv2.resize(img,(200,200))
plt.show()

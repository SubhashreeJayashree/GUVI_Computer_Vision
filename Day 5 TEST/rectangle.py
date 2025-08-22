import cv2
import matplotlib.pyplot as plt
img=cv2.imread("robot.jpg")
print(img.shape)
rectangle=cv2.rectangle(img,(50,50),(100,100),(0,0,255),1)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
resize=cv2.resize(img,(200,200))
plt.axis("off")
plt.show()
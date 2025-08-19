import cv2
import matplotlib.pyplot as plt
img=cv2.imread("image.jpeg")
print(img.shape)
rectangle=cv2.rectangle(img,(500,500),(100,100),(255,0,0),2)
plt.axis("off")
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
resize=cv2.resize(img,(200,200))
plt.show()
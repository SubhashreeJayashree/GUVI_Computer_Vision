import cv2
import matplotlib.pyplot as plt
img1=cv2.imread("building1.jpeg")
img2=cv2.imread("building2.jpeg")


#ORB Keypoint Extractor
orb=cv2.ORB_create()
kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)

Brute_force=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches=Brute_force.match(des1,des2)
matches=sorted(matches,key=lambda x:x.distance)
result=cv2.drawMatches(img1,kp1,img2,kp2,matches[:30],None,flags=2) #flags is 0 or 2 only 0 means it will have connect all the points but 2 will not connect like that 
plt.imshow(cv2.cvtColor(result,cv2.COLOR_BGR2RGB))
plt.show()
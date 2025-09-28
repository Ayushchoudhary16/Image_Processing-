import cv2
image=cv2.imread("./project-5.jpeg")

w,h,ch=image.shape
w=round(w*0.7)
h=round(w*0.7)

small_image=cv2.resize(image,(w,h))
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
jadu=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

cv2.imshow("small Image",small_image)
cv2.imshow("gray image",gray_image)
cv2.imshow("jadu image",jadu)

x1, y1 = 120, 150  # Top-left corner of the box
x2, y2 = 220, 270  # Bottom-right corner of the box

cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)
cv2.putText(image, "Ayush Choudhary",(x1, y1 - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0),2)

cv2.imshow("My Image",image)
cv2.waitKey(0)















# task1-original image par ractangle banana hai or rancatngle ke just  upper ik text homa chaiye
# 
#  
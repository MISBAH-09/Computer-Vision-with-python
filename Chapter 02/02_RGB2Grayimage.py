import cv2

image = cv2.imread('Chapter 02/images/dark1.PNG',cv2.IMREAD_GRAYSCALE) 
cv2.imwrite('Chapter 02/images/dark1_gray.jpg', image)
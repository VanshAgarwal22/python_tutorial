#image-resizer

import cv2
src =cv2.imread("(29).jpg")

# cv2.imshow("tittle" ,src)

#percent by which the image is resized
scale_percent = 50

#calculate the 50 percent of original dimensions

new_width = int(src.shape[1] * scale_percent / 100)   # shape is a numpy array function which gives you height by width
new_height = int(src.shape[0] * scale_percent / 100)

# dsize

dsize = (new_width, new_height)

# resize image

output = cv2.resize(src, dsize)

cv2.imwrite('new_image.jpg',output) 
cv2.waitKey(0)


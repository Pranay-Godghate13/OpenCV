import cv2
import os

#read image
img_path=os.path.join('.','myvenv/Include/data','bird.jpg')
img=cv2.imread(img_path)

#write image
cv2.imwrite(os.path.join('.','myvenv/Include/data','bird_out.jpg'),img)

#vizualizing image
cv2.imshow('image',img)
cv2.waitKey(5000)

import cv2 as cv
import numpy as np


img = cv.imread('image.jpg')

cv.imshow('BGR',img)
key = cv.waitKey(0)

print("input key here is ",key)

#what is the size of the image
print(img.shape)

# change image from BGR to gray

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray',img)
key = cv.waitKey(0)
print(img.shape)


# reshape

img = cv.resize(img,(500,500))
cv.imshow('Resized image',img)
key = cv.waitKey(0)
print(img.shape)


for i in range(10):
    print("value of the  pixel ",img[i][0])

# thresholding

cv.threshold(img,127,255,cv.THRESH_BINARY,img)

cv.imshow('after threshold',img)
key = cv.waitKey(0)
print(img.shape)


for i in range(10):
    print("value of the  pixel ",img[i][0])


    # adding pepper noise in image

for i in range(500):
    for j in range(500):
        if i%10 == 0 and j%10==0:
            img[i][j]= 0;

cv.imshow('pepper noise',img)
key = cv.waitKey(0)

# now fixing pepper noise with dilate

kernel = np.ones((3,3),np.uint8)
cv.dilate(img,kernel,img)
cv.erode(img,kernel,img)
cv.imshow('after fixing pepper noise',img)
key = cv.waitKey(0)


# TODo introduce salt noise  and try to correct

# trying to improve the image

img2 = cv.imread("faces.jpg")

cv.imshow("faces",img2)
cv.waitKey(0)

blur = cv.GaussianBlur(img2,(5,5),0)
cv.imshow("blured image",img2)
cv.waitKey(0)
cv.addWeighted(img2, 1.2, blur, 2, 0, img2)

cv.imshow("sharped image",img2)
cv.waitKey(0)
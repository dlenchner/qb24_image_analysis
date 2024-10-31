#!/usr/bin/env python3

# import required packages
import cv2
import sys
import numpy

image1 = sys.argv[1]
image1_name = str(sys.argv[1])
image1_data = open("image1_data.txt", mode = 'w')
image1_data.write("File: " + image1_name + '\n')


# read in the same image file and use it to generate a numpy array
# the default for cv2.imread is to read the file in BGR format (blue, green, red)
image_bgr = cv2.imread(image1)

# quality control to ensure that the image was read in properly
if image_bgr is not None:
    cv2.imshow("Color", image_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading image")


image1_data.write("Size: {} x {} pixels".format(image_bgr.shape[0], image_bgr.shape[1]) + '\n' + '\n')

image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

image1_data.close()

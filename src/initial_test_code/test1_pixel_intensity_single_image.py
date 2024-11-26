#!/usr/bin/env python3

# import required packages
import cv2
import sys
import PIL
import numpy
from PIL import Image

# for any arrays that are printed, print the full array (don't truncate the array)
numpy.set_printoptions(threshold=sys.maxsize)


# read in a test image file from the command line to get metadata information
image = Image.open(sys.argv[1])

# generate a report file
report = open("image_report.txt", mode = 'w')
report.write("Image Report" + '\n')

# add features of the test image file to the report file
report.write("Format:" + image.format + '\n')
report.write("Image size:" + str(image.size) + '\n')
report.write("Image mode:" + image.mode + '\n' + '\n')


### 

# the following code is not necessary, but is an alternative way to generate an array from the image file

# # convert the test image file into a numpy array
# img_array = numpy.array(image)

# # add features of the image array and the array itself to the report file
# report.write("Array shape:" + str(img_array.shape) + '\n')
# report.write(str(img_array) + '\n' + '\n')

###


report.write("Pixel Intensities" + '\n')


# read in the image file a second time, this time getting it into a format that can be converted to grayscale
image_rgb = cv2.imread(sys.argv[1])

# convert the image to grayscale
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)


# display the color and grayscale images sequentially
cv2.imshow("Color", image_rgb)
cv2.waitKey(0)
cv2.imshow("Grayscale", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# convert the grayscale image to a numpy array
img_gray_array = numpy.array(image_gray)

# add each row of pixels to the report file
for row in img_gray_array:
    report.write(str(row) + '\n')



###

# the following code is one potential way to generate a threshold... needs to be improved upon

# result = numpy.where(img_gray_array > 20)
# print(result)
# print(img_array[result])

# report.write(str(result) + '\n')
# report.write(str(img_array[result]) + '\n')

###


# close the test image file and the report file
image.close()
report.close()



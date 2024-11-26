#!/usr/bin/env python3

# import required packages
import cv2
import sys
import numpy

# create a report file
image_data = open("image_data.tsv", mode = 'w')

# create a descriptive header row for the report file
image_data.write("image\tsize\ttotal_pixels\tpixels_above_threshold\tpat_sum\tavg_int\n")

# take image file from command line and save as image1
image1 = sys.argv[1]


# read the image file into OpenCV to generate a numpy array from the image
image_bgr = cv2.imread(image1) # NOTE: cv2.imread defaults to reading the file in BGR format (blue, green, red)

# perform quality control to ensure that the image was read in properly
# display the color image (if loaded properly), press any key to continue
if image_bgr is not None:
    cv2.imshow("Color", image_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading image")

# extract metadata from the image and write it to the report file
# the following code presents the size as image height x image width
image_data.write("image1\t")
image_data.write("{}x{}\t".format(image_bgr.shape[0], image_bgr.shape[1]))


# convert the image to grayscale and generate a new numpy array
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

# display the grayscale image, press any key to continue
cv2.imshow("Grayscale", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# establish a threshold
# this can be any number, but here the threshold is just the average intensity from the entire image
threshold = numpy.mean(image_gray)

# identify the indices in the image_gray array where the intensity values are greater than the threshold
# the following code returns two arrays - the first describes y-coordinates, the second describes x-coordinates
pixel_indices = numpy.where(image_gray > threshold) 

# generate a new array that only includes the pixels whose intensity values are above the threshold
pixels = image_gray[pixel_indices]

# perform statistics on the pixels array to determine the total intensity, the number of pixels, and the average intensity
pixel_sum = numpy.sum(pixels)
pixel_count = numpy.size(pixels)
avg_int = pixel_sum / pixel_count

# print(pixels_sum)
# print(pixel_count)
# print(avg_int)

# write the statistics to the report file
image_data.write(str(pixel_count) + '\t')
image_data.write(str(pixel_sum) + '\t')
image_data.write(str(avg_int) + '\n')


# close the report file
image_data.close()

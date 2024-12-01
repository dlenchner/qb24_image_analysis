#!/usr/bin/env python

import numpy
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import skimage as ski
from skimage.measure import regionprops, label

# Establish the filepath and the filename
filepath = "~/qb24_image_analysis/data/"
# filename = "962_F1_1_blue.png"
# filename = "FluorescentCells.jpg"
filename = "Week10_200907_G11_s4_w1C97E64C3-00B1-4693-AE49-A8708F25B55F.tif"

# Read in the image file
img = imageio.imread(uri = filepath + filename)
# img = imageio.imread(uri = "~/qb24_image_analysis/data/962_F1_1_blue.png")
# img = imageio.imread(uri = "~/qb24_image_analysis/data/FluorescentCells.jpg", )

# create a metadata file
image_metadata = open("image_metadata.tsv", mode = 'w')

# create a descriptive header row for the metadata file
image_metadata.write("image\tfilename\tsize\tdimensions\tconvert?\n")


# Convert to grayscale if necessary
# If there are 3 dimensions (RGB, instead of grayscale), proceed with the following
if img.ndim == 3:
    # Show the image
    plt.imshow(img)
    plt.title("Color Image")
    plt.show()
    # Report the image shape and features and write to the metadata file (mark "y" for converted)
    image_metadata.write(f"001\t{filename}\t{img.shape[0]} x {img.shape[1]}\t{img.ndim}\ty\n")
    # Convert to grayscale
    img_gray = ski.color.rgb2gray(img)
    # Show the grayscale image
    plt.imshow(img_gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.show()
# If there are 2 dimensions (grayscale, instead of RGB), proceed with the following
else:
    # Report the image shape and features and write to the metadata file (mark "n" for converted)
    image_metadata.write(f"001\t{filename}\t{img.shape[0]} x {img.shape[1]}\t{img.ndim}\tn\n")
    # Rename img to img_gray
    img_gray = img
    # Show the image
    plt.imshow(img_gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.show()

# Apply a Gaussian blur to the image
img_blur = ski.filters.gaussian(img_gray, sigma = 1.0)
plt.imshow(img_blur, cmap='gray')
plt.title("Smoothed Image")
plt.show()


# Automatically determine a threshold, t
t = ski.filters.threshold_otsu(img_blur)

# Using the threshold, t, establish a binary mask
mask = img_blur > t

# Show the mask
fig, ax = plt.subplots()
ax.imshow(mask, cmap="gray")
plt.title("Binary Mask")
plt.show()


# Identify separate objects based on the mask and label them
labels = label(mask)

# Show the identified objects
plt.imshow(labels)
plt.title("Labeled Objects")
plt.show()

# Establish a protocol to filter the objects based on size
def filter_by_size(labels, minsize, maxsize):
    # Find label sizes
    sizes = numpy.bincount(labels.ravel())
    # Iterate through labels, skipping background
    for i in range(1, sizes.shape[0]):
        # If the number of pixels falls outsize the cutoff range, relabel as background
        if sizes[i] < minsize or sizes[i] > maxsize:
            # Find all pixels for label
            where = numpy.where(labels == i)
            labels[where] = 0
    # Get set of unique labels
    ulabels = numpy.unique(labels)
    for i, j in enumerate(ulabels):
        # Relabel so labels span 1 to # of labels
        labels[numpy.where(labels == j)] = i
    return labels

# Filter out any objects smaller than 500 pixels
labels = filter_by_size(labels, 500, 10000000)


# Show the filtered objects
plt.imshow(labels)
plt.title("Filtered Objects")
plt.show()

# Save each of the objects identified above as a region 
regions = regionprops(labels, intensity_image = img_gray)

# create a report file
image_data = open("image_data.tsv", mode = 'w')

# create a descriptive header row for the report file
image_data.write("region\tpixels\ttotal_intensity\taverage_intensity\n")


# For each of the identified objects/regions, calculate the total intensity, the size in pixels, and the averaged intensity
# Write the data for each region to the report file
i = 1
for region in regions:
    intensity = region.intensity_image.sum()
    size = region.area
    average = intensity / size
    image_data.write(f"{i}\t{size}\t{intensity}\t{average}\n")
    i += 1


# Close the report file
image_data.close()
image_metadata.close()















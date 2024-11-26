#!/usr/bin/env python

# import sys
import numpy
import matplotlib.pyplot as plt
import imageio.v2 as imageio
# import cv2
import skimage as ski
from skimage.measure import regionprops, label

# Establish the filepath and the filename
filepath = "~/qb24_image_analysis/data/"
# filename = "962_F1_1_blue.png"
filename = "FluorescentCells.jpg"

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

# # Display a histogram of intensity values, so a threshold can be set
# plt.hist(img_blur, bins = 10)
# plt.show()

# Automatically determine a threshold, t
t = ski.filters.threshold_otsu(img_blur)

# Using the threshold, t, establish a binary mask
mask = img_blur > t

# Show the mask
fig, ax = plt.subplots()
ax.imshow(mask, cmap="gray")
plt.title("Binary Mask")
plt.show()


# def find_labels(mask):
#     # Set initial label
#     l = 0
#     # Create array to hold labels
#     labels = numpy.zeros(mask.shape, numpy.int32)
#     # Create list to keep track of label associations
#     equivalence = [0]
#     # Check upper-left corner
#     if mask[0, 0]:
#         l += 1
#         equivalence.append(l)
#         labels[0, 0] = l
#     # For each non-zero column in row 0, check back pixel label
#     for y in range(1, mask.shape[1]):
#         if mask[0, y]:
#             if mask[0, y - 1]:
#                 # If back pixel has a label, use same label
#                 labels[0, y] = equivalence[labels[0, y - 1]]
#             else:
#                 # Add new label
#                 l += 1
#                 equivalence.append(l)
#                 labels[0, y] = l
#     # For each non-zero row
#     for x in range(1, mask.shape[0]):
#         # Check left-most column, up  and up-right pixels
#         if mask[x, 0]:
#             if mask[x - 1, 0]:
#                 # If up pixel has label, use that label
#                 labels[x, 0] = equivalence[labels[x - 1, 0]]
#             elif mask[x - 1, 1]:
#                 # If up-right pixel has label, use that label
#                 labels[x, 0] = equivalence[labels[x - 1, 1]]
#             else:
#                 # Add new label
#                 l += 1
#                 equivalence.append(l)
#                 labels[x, 0] = l
#         # For each non-zero column except last in nonzero rows, check up, up-right, up-right, up-left, left pixels
#         for y in range(1, mask.shape[1] - 1):
#             if mask[x, y]:
#                 if mask[x - 1, y]:
#                     # If up pixel has label, use that label
#                     labels[x, y] = equivalence[labels[x - 1, y]]
#                 elif mask[x - 1, y + 1]:
#                     # If not up but up-right pixel has label, need to update equivalence table
#                     if mask[x - 1, y - 1]:
#                         # If up-left pixel has label, relabel up-right equivalence, up-left equivalence, and self with smallest label
#                         labels[x, y] = min(equivalence[labels[x - 1, y - 1]], equivalence[labels[x - 1, y + 1]])
#                         equivalence[labels[x - 1, y - 1]] = labels[x, y]
#                         equivalence[labels[x - 1, y + 1]] = labels[x, y]
#                     elif mask[x, y - 1]:
#                         # If left pixel has label, relabel up-right equivalence, left equivalence, and self with smallest label
#                         labels[x, y] = min(equivalence[labels[x, y - 1]], equivalence[labels[x - 1, y + 1]])
#                         equivalence[labels[x, y - 1]] = labels[x, y]
#                         equivalence[labels[x - 1, y + 1]] = labels[x, y]
#                     else:
#                         # If neither up-left or left pixels are labeled, use up-right equivalence label
#                         labels[x, y] = equivalence[labels[x - 1, y + 1]]
#                 elif mask[x - 1, y - 1]:
#                     # If not up, or up-right pixels have labels but up-left does, use that equivalence label
#                     labels[x, y] = equivalence[labels[x - 1, y - 1]]
#                 elif mask[x, y - 1]:
#                     # If not up, up-right, or up-left pixels have labels but left does, use that equivalence label
#                     labels[x, y] = equivalence[labels[x, y - 1]]
#                 else:
#                     # Otherwise, add new label
#                     l += 1
#                     equivalence.append(l)
#                     labels[x, y] = l
#         # Check last pixel in row
#         if mask[x, -1]:
#             if mask[x - 1, -1]:
#                 # if up pixel is labeled use that equivalence label 
#                 labels[x, -1] = equivalence[labels[x - 1, -1]]
#             elif mask[x - 1, -2]:
#                 # if not up but up-left pixel is labeled use that equivalence label 
#                 labels[x, -1] = equivalence[labels[x - 1, -2]]
#             elif mask[x, -2]:
#                 # if not up or up-left but left pixel is labeled use that equivalence label 
#                 labels[x, -1] = equivalence[labels[x, -2]]
#             else:
#                 # Otherwise, add new label
#                 l += 1
#                 equivalence.append(l)
#                 labels[x, -1] = l
#     equivalence = numpy.array(equivalence)
#     # Go backwards through all labels
#     for i in range(1, len(equivalence))[::-1]:
#         # Convert labels to the lowest value in the set associated with a single object
#         labels[numpy.where(labels == i)] = equivalence[i]
#     # Get set of unique labels
#     ulabels = numpy.unique(labels)
#     for i, j in enumerate(ulabels):
#         # Relabel so labels span 1 to # of labels
#         labels[numpy.where(labels == j)] = i
#     return labels

# labels = find_labels(mask)
# # Since the first label is 1 and the background is 0, let's adjust the background for more contrast
# label_copy = numpy.copy(labels)
# label_copy[numpy.where(label_copy == 0)] -= 50
# plt.imshow(label_copy)
# plt.show()

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

# region_intensities = {region.label: region.intensity_image.sum() for region in regions}
# region_sizes = {region.label: region.area for region in regions}
# region_average = {region.label: region.intensity_image.mean() for region in regions}


# create a report file
image_data = open("image_data.tsv", mode = 'w')

# create a descriptive header row for the report file
image_data.write("region\tpixels\ttotal_intensity\taverage_intensity\n")


# for label, total_intensity in region_intensities.items():
#     print(f"Nucleus {label}: Total Intensity = {total_intensity}")
# for label, size in region_sizes.items():
#     print(f"Region {label}: Size = {size} pixels")
# for label, average in region_average.items():
#     print(f"Region {label}: Average Intensity = {average:.2f}")

# total_intensity = sum(region.intensity_image.sum() for region in regions)
# print(f"{total_intensity}")

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















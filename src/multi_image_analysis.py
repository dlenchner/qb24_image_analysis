#!/usr/bin/env python

# import the necessary packages
import numpy
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import skimage as ski
from skimage.measure import regionprops, label
import glob
import os

# establish a working directory to draw images from and a results directory to save files to
data_directory = '../data/'
results_directory = '../results/'

# generate a sorted list of file names frmo the working directory
filenames = glob.glob(f'{data_directory}*.tif')
filenames = sorted([os.path.basename(file) for file in filenames])


# create a metadata file and generate a descriptive header row
image_metadata = open(f"{results_directory}image_metadata.tsv", mode = 'w')
image_metadata.write("image\tfilename\tsize\tdimensions\tconvert?\n")

# create a report file and generate a descriptive header row
image_data = open(f"{results_directory}image_data.tsv", mode = 'w')
image_data.write("image\tregion\tpixels\ttotal_intensity\taverage_intensity\n")

# close the metadata and report files
image_metadata.close()
image_data.close()

# define an image analysis function that acts on a given input "img"
def image_analysis(img):
    # read in the image file
    img = imageio.imread(uri = data_directory + filename)
    
    # open the metadata and report files
    image_metadata = open(f"{results_directory}image_metadata.tsv", mode = 'a')
    image_data = open(f"{results_directory}image_data.tsv", mode = 'a')

    # convert to grayscale if necessary
    # if there are 3 dimensions (RGB, instead of grayscale), proceed with the following
    if img.ndim == 3:
        # show the image
        plt.imshow(img)
        plt.title("Color Image")
        plt.show()
        # report the image shape and features and write to the metadata file (mark "y" for converted)
        image_metadata.write(f"{i+1}\t{filename}\t{img.shape[0]} x {img.shape[1]}\t{img.ndim}\ty\n")
        # convert to grayscale
        img_gray = ski.color.rgb2gray(img)
        # show the grayscale image
        plt.imshow(img_gray, cmap='gray')
        plt.title("Grayscale Image")
        plt.show()
    # if there are 2 dimensions (grayscale, instead of RGB), proceed with the following
    else:
        # report the image shape and features and write to the metadata file (mark "n" for converted)
        image_metadata.write(f"{i+1}\t{filename}\t{img.shape[0]} x {img.shape[1]}\t{img.ndim}\tn\n")
        # rename img to img_gray
        img_gray = img
        # show the image
        plt.imshow(img_gray, cmap='gray')
        plt.title("Grayscale Image")
        plt.show()

    # apply a Gaussian blur to the image
    img_blur = ski.filters.gaussian(img_gray, sigma = 1.0)
    plt.imshow(img_blur, cmap='gray')
    plt.title("Smoothed Image")
    plt.show()

    # automatically determine a threshold, t
    t = ski.filters.threshold_otsu(img_blur)

    # using the threshold, t, establish a binary mask
    mask = img_blur > t

    # show the mask
    fig, ax = plt.subplots()
    ax.imshow(mask, cmap="gray")
    plt.title("Binary Mask")
    plt.show()


    # identify separate objects based on the mask and label them
    labels = label(mask)

    # show the identified objects
    plt.imshow(labels)
    plt.title("Labeled Objects")
    plt.show()


    # establish a protocol to filter the objects based on size
    def filter_by_size(labels, minsize, maxsize):
        # find label sizes
        sizes = numpy.bincount(labels.ravel())
        # iterate through labels, skipping background
        for i in range(1, sizes.shape[0]):
            # if the number of pixels falls outsize the cutoff range, relabel as background
            if sizes[i] < minsize or sizes[i] > maxsize:
                # find all pixels for label
                where = numpy.where(labels == i)
                labels[where] = 0
        # get set of unique labels
        ulabels = numpy.unique(labels)
        for i, j in enumerate(ulabels):
            # relabel so labels span 1 to # of labels
            labels[numpy.where(labels == j)] = i
        return labels

    # filter out any objects smaller than 500 pixels
    labels = filter_by_size(labels, 500, 10000000)

    # show the filtered objects
    plt.imshow(labels)
    plt.title("Filtered Objects")
    plt.show()

    # save each of the objects identified above as a region 
    regions = regionprops(labels, intensity_image = img_gray)

    # generate a plot to display the labeled regions
    fig, ax = plt.subplots()
    ax.imshow(labels)

    # for each of the identified objects/regions, label the region
    # calculate the total intensity, the size in pixels, and the averaged intensity of the region and write the data to the report file
    j = 1
    for region in regions:
        centroid = region.centroid
        ax.text(centroid[1], centroid[0], str(j), backgroundcolor = 'black', color = 'white', fontsize = 5, ha = 'center', va = 'center')
        intensity = region.intensity_image.sum()
        size = region.area
        average = intensity / size
        image_data.write(f"{i+1}\t{j}\t{size}\t{intensity}\t{average}\n")
        j += 1

    # remove the axes from the plot of labeled regions
    ax.axis('off')

    # save the plot as a tif image file
    plt.savefig(f"{results_directory}image_{i+1}_{filename}_annotated.png", dpi = 300, bbox_inches = 'tight')
    plt.close(fig)

    # close the metadata and report files
    image_metadata.close()
    image_data.close()


# for each of the images in the working directory, run the function "image_analysis" defined above
for i, filename in enumerate(filenames):
    image_analysis(filename)












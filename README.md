# qb24_image_analysis


# Title #

Developing code that can quantify, report, and compare fluorescence intensity across samples



# Description #

In an effort to better understand how image analysis software functions under the hood, we plan to work from the ground up to develop code that can automate quantification of fluorescent images and report the average fluorescent intensity in a given region of interest. The ultimate goal is to apply the code to multiple images and compare average fluorescence intensity across samples or across time points. 


# Published figure examples #

The following figures demonstrate analyses that involve quantifying fluorescence intensity in an image. Our plan is to write a Python script that can extract fluorescence intensity data from an image file. From there, we can hopefully recapitulate any of these figure types depending on how we structure the R script for plotting.

FRAP
![alt text](https://link.springer.com/article/10.1007/s11095-013-1146-9/figures/4)





# Datasets #

For most of our process, we plan to use local fluorescent images that we already have from our personal research experiences. Once we develop our code and are able to show that it works, we hope to apply our code to a larger set of publicly available images that can be used to compare fluorescence intensity over time (such as in a FRAP analysis) or compare fluorescence intensity between treatment groups (such as a gene expression experiment using a fluorescent reporter on the protein product).

Some possible research areas/topics/systems to keep in mind when looking for image sets:

    FRAP analysis
    Live cell imaging of fluorescent gene expression reporters
    Analysis of PacBIO or Illumina sequencing reads that generate fluorescent signals during nucleotide incorporation



# Software and versions #

[Python](https://www.python.org) v3.12.3 - Quantify and report fluorescence intensity

[R](https://www.r-project.org) v4.4.1 - Plot the fluorescence data generated in Python



[ImageJ](https://imagej.net/ij/index.html) v1.54k - Run analyses to serve as comparisons for the results generated from our code


# Proposed steps #

Step 1.     Read an individual image file into Python, quantify fluorescent intensity at each pixel, and report that fluorescent intensity.

Step 2.     Build on the work in step 1 by developing code that can isolate a region of interest, subtract background intensity, and report the average fluorescent intensity just in that region.

Step 3.     Modify the code to analyze two or more images at a time.

Step 4.     Read the fluorescence intensity data from each image into R.

Step 5.     Generate a plot in R that displays the fluorescence intensity data from each of the images.
    
    
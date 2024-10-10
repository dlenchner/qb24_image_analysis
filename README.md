# qb24_image_analysis


# Title #

Developing code that can quantify, report, and compare fluorescence intensity across samples



# Description #

In an effort to better understand how image analysis software functions under the hood, we plan to work from the ground up to develop code that can automate quantification of fluorescent images and report the average fluorescent intensity in a given region of interest. The ultimate goal is to apply the code to multiple images and compare average fluorescence intensity across samples or across time points. 


# Example published figure #





# Datasets #

For most of our process, we plan to use local fluorescent images that we already have from our personal research experiences. Once we develop our code and are able to show that it works, we hope to apply our code to larger set of publicly available images that can be used to compare fluorescence intensity over time (such as in a FRAP analysis) or compare fluorescence intensity between treatment groups (such as a gene expression experiment using a fluorescent reporter on the protein product).

Some possible research areas/topics/systems to keep in mind when looking for image sets:

    FRAP analysis
    Live cell imaging of fluorescent gene expression reporters
    Analysis of PacBIO or Illumina sequencing reads that generate fluorescent signals during nucleotide incorporation



# Software and versions #

For quantification of fluorescence intensity, we plan to write a Python script that can be run in terminal

    [Python](https://www.python.org) v3.12.3 

For plotting of the fluorescence data, we plan to write an R script

    [R](https://www.r-project.org) v4.4.1



As we work through the project, we plan to compare results from our Python script with results generated from external software, such as Fiji ImageJ

    [ImageJ](https://imagej.net/ij/index.html) v1.54k


# Proposed steps #

Step 1. Read an individual image file into Python, quantify fluorescent intensity at each pixel, and report that fluorescent intensity. \n
Step 2. Build on the work in step 1 by developing code that can isolate a region of interest, subtract background intensity, and report the average fluorescent intensity in that region.\n
Step 3. Modify the code to analyze two or more images at a time.\n
Step 4. Read the fluorescence intensity data from each image into R.\n
Step 5. Generate a plot in R that displays the fluorescence intensity data from each of the images.\n
    
    
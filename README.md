# qb24_image_analysis


# Title #

Developing code that can quantify, report, and compare fluorescence intensity across samples



# Description #

In an effort to better understand how image analysis software functions under the hood, we plan to work from the ground up to develop code that can automate quantification of fluorescent images and report the average fluorescent intensity in a given region of interest. The ultimate goal is to apply the code to multiple images and compare average fluorescence intensity across samples or across time points. 


# Published figure example #

The following figure demonstrates a FRAP analysis, which is one of many techniques that involve quantifying fluorescence intensity in an image. Depending on the images we are able to obtain, recapitulating a FRAP analysis like the one pictured below is one potential avenue that our project can take.


![alt text](https://ars.els-cdn.com/content/image/1-s2.0-S1046202302002888-gr2.jpg)

Paper: [Using FRAP and mathematical modeling to determine the in vivo kinetics of nuclear proteins](https://www.sciencedirect.com/science/article/pii/S1046202302002888?via%3Dihub#FIG1)

Reference: Carrero G, McDonald D, Crawford E, de Vries G, Hendzel MJ. Using FRAP and mathematical modeling to determine the in vivo kinetics of nuclear proteins. Methods. 2003 Jan;29(1):14-28. doi: 10.1016/s1046-2023(02)00288-8. PMID: 12543068.


# Datasets #

For most of our process, we plan to use local fluorescent images that we already have from our personal research experiences. Once we develop our code and are able to show that it works, we hope to apply our code to a larger set of publicly available images that can be used to compare fluorescence intensity over time (such as in a FRAP analysis) or compare fluorescence intensity between treatment groups.

Some possible research areas/topics/systems to keep in mind when looking for image sets:
    FRAP analysis
    Live cell imaging of fluorescent gene expression reporters
    Analysis of PacBIO or Illumina sequencing reads that generate fluorescent signals during nucleotide incorporation

One potential source we can use to find publicly available image sets is the [Image Data Resource](http://idr.openmicroscopy.org) 



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
    
    
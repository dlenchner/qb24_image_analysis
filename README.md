

# Comparative Analysis of Fluorescence Intensity - An Exploration into Quantitative Microscopy #



## Description ##

In an effort to better understand how image analysis software functions under the hood, we plan to work from the ground up to develop code that can automate quantification of fluorescent images and report the average fluorescence intensity in a given region of interest. The ultimate goal is to apply the code to multiple images and compare average fluorescence intensity across samples or across time points. 


## Example of a published figure ##

The following figure demonstrates a FRAP analysis, where a region of interest in a cell is photobleached and monitored over time to track the recovery of the fluorescent signal in that region. This is just one of many experiment types that involve quantifying fluorescence intensity in a given area. Depending on the images we are able to obtain from public repositories, recapitulating a FRAP analysis (like the one pictured below) is one trajectory our project could take.



![Sample FRAP analysis](https://ars.els-cdn.com/content/image/1-s2.0-S1046202302002888-gr2.jpg)
Fig. 2. Example of a FRAP recovery curve. The cell from Fig. 1 is again illustrated. Images collected at different points in the recovery time course are shown. The right-hand panel shows the normalized plot of intensity-versus-time for the cell shown.

Paper: Carrero G, McDonald D, Crawford E, de Vries G, Hendzel MJ. [Using FRAP and mathematical modeling to determine the in vivo kinetics of nuclear proteins](https://www.sciencedirect.com/science/article/pii/S1046202302002888?via%3Dihub#FIG1) Methods. 2003 Jan;29(1):14-28. doi: 10.1016/s1046-2023(02)00288-8. PMID: 12543068.



## Datasets ##

The bulk of our project will be done on local fluorescent image files that we already have access to from our personal research experience. Once we develop our code and can demonstrate its function, we hope to apply it to a larger set of publicly available image files that can be used to compare fluorescence intensity over time (such as in a FRAP analysis) or compare fluorescence intensity between different treatment groups.

Some possible research areas/topics/systems to keep in mind when looking for image sets:
- FRAP analysis
- Live cell imaging of fluorescent gene expression reporters
- Analysis of PacBIO or Illumina sequencing reads that generate fluorescent signals during nucleotide incorporation

One potential source we can use to find publicly available image sets is the [Image Data Resource](http://idr.openmicroscopy.org) 



## Software ##

[Python](https://www.python.org) v3.12.3 - Quantify and report fluorescence intensity

[R](https://www.r-project.org) v4.4.1 - Plot the fluorescence data generated in Python



[ImageJ](https://imagej.net/ij/index.html) v1.54k - Run analyses to serve as comparisons for the results generated from our code


## Proposed steps ##

1. Read an individual image file into Python, quantify fluorescence intensity at each pixel, and report that fluorescence intensity.
2. Build on the work in step 1 by developing code that can isolate a region of interest, subtract background intensity, and report the average fluorescence intensity just in that region.
3. Modify the code to analyze two or more images at a time.
4. Read the fluorescence intensity data from each image into R.
5. Generate a plot in R that displays the fluorescence intensity data from each of the images.
    
    
## Project Organization ##

    ├── README.md
    ├── data
    │   ├── 962_F1_1_blue.png
    │   ├── A1_c2.jpg
    │   ├── FluorescentCells.jpg
    │   └── GMC101_miR71KO-40x_DAPI.jpg
    ├── doc
    │   ├── checkin-2024_11_01.md
    │   └── checkin-2024_11_22.md
    ├── requirements.txt
    ├── results
    │   ├── image_1_962_F1_1_blue.png_annotated.png
    │   ├── image_2_A1_c2.jpg_annotated.png
    │   ├── image_3_FluorescentCells.jpg_annotated.png
    │   ├── image_4_GMC101_miR71KO-40x_DAPI.jpg_annotated.png
    │   ├── image_data.tsv
    │   └── image_metadata.tsv
    └── src
        ├── initial_test_code
        │   ├── test1_pixel_intensity_single_image.py
        │   ├── test2_alt_avg_intensity_single_image.py
        │   ├── test2_avg_intensity_single_image.py
        │   └── test3_thresholding_masking_single_image.ipynb
        ├── multi_image_analysis.py
        └── single_image_analysis.py


# How to use this image analysis program #

## Setting up the repository ##

### Create a repository with the following layout ###

    ├── data
    │   ├── image_of_interest_001
    │   ├── image_of_interest_002
    │   └── image_of_interest_etc.....
    ├── results
    └── src
        └── multi_image_analysis.py

## Running multi image analysis ##

1. Within the /src/ directory in Terminal, ensure the program is executable by running the following command:
  - chmod +x multi_image_analysis.py
2. Once the program is executable, run the program by providing the following command:
  - ./multi_image_analysis.py

## Expected results ##

- The program will enter the /data/ directory to run the analysis on each of the dowloaded image files
- Report files (tsv format) and labeled images (png format) will be output to the /results/ directory with the following naming convention:
  - image_data.tsv
  - image_metadata.tsv
  - image_{#}_{filename}_annotated.png


### The final repository should look something like this ###

    ├── data
    │   ├── image_of_interest_001
    │   ├── image_of_interest_002
    │   └── image_of_interest_003
    ├── results
    │   ├── image_1_image_of_interest_001_annotated.png
    │   ├── image_2_image_of_interest_002_annotated.png
    │   ├── image_3_image_of_interest_003_annotated.png
    │   ├── image_data.tsv
    │   └── image_metadata.tsv
    └── src
        └── multi_image_analysis.py

 
## Next steps ##

- The output files (image_data.tsv and image_metadata.tsv) can be read into a graphing software, such as ggplot in R and plotted. As it stands, the output data file will report the total fluorescent intensity, the total size (in pixels), and the average fluorescent intensity (total intensity / total size) for each region of interest in each image of interest.




#### NOTE: This code should be adaptable to any study involving comparative fluorescence between samples. The report files may have to be altered to best fit the study. ####
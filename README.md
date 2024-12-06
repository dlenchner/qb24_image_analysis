

# Comparative Analysis of Fluorescence Intensity - An Exploration into Quantitative Microscopy #


The final presentation for this project can be viewed [here](https://docs.google.com/presentation/d/1TWOr0OYpdGLmi3ymKDzFBMR0HWqh9NBstzVpAkOugoM/edit?usp=sharing)


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


### Note: ###
- See the USAGE.md file for details about the image set used for our proof of concept
- See the image_retrieval.md file for information on how to acquire the image set we used for our proof of concept





## Software ##

[Python](https://www.python.org) v3.12.3 - Quantify and report fluorescence intensity

- See the requirements.txt file for specific packages needed in python.

[R](https://www.r-project.org) v4.4.1 - Plot the fluorescence data generated in Python

- The R script used is adaptable based on the particular study of interest. For our proof of concept, we utilized Tidyverse.



## Proposed steps ##

- [x] Read an individual image file into Python, quantify fluorescence intensity at each pixel, and report that fluorescence intensity.
- [x] Build on the work in step 1 by developing code that can isolate a region of interest, subtract background intensity, and report the average fluorescence intensity just in that region.
- [x] Modify the code to analyze two or more images at a time.
- [x] Read the fluorescence intensity data from each image into R.
- [x] Generate a plot in R that displays the fluorescence intensity data from each of the images.
    
    
## Project Organization ##

    ├── README.md
    ├── USAGE.md
    ├── data
    │   ├── Week10_200907_B02_s4_w1BBC355D6-EAC9-4C4B-894B-6289981539D6.tif
    │   ├── Week10_200907_B03_s4_w1E1B49716-E2C2-48FF-91E5-71E844AF38BD.tif
    │   ├── Week10_200907_B04_s4_w1B632CB5F-4D31-42CC-A5D2-0BC6A4D33C28.tif
    │   ├── Week10_200907_B05_s4_w168154335-E870-426E-8C07-AE6243C511B8.tif
    │   ├── Week10_200907_B06_s4_w176CA3679-C863-40B8-98A8-8248552A3D16.tif
    │   ├── Week10_200907_B07_s4_w1B39B1CBB-9449-4757-84C8-6F2D156925C7.tif
    │   ├── Week10_200907_B08_s4_w173DC9509-E539-4402-8C60-5A4BFCF963BA.tif
    │   ├── Week10_200907_B09_s4_w17414221F-2154-4685-AB36-D6270E11832B.tif
    │   ├── Week10_200907_B10_s4_w1DABEE4FC-FF53-48AF-B6A7-B19EB9EBABDE.tif
    │   ├── Week10_200907_B11_s4_w14222240C-811F-436D-B8A5-22A1C4749191.tif
    │   ├── Week10_200907_C02_s4_w13F830D82-B5CE-4F35-8104-40D5773B2772.tif
    │   ├── Week10_200907_C03_s4_w1EFE40D10-5278-4F09-8E89-CCDBFCB8D25E.tif
    │   ├── Week10_200907_C04_s4_w18EBFCB24-900A-4C6A-858A-7EEE30BC7572.tif
    │   ├── Week10_200907_C05_s4_w11DFD4B37-6709-4109-9057-D3D6827E4E22.tif
    │   ├── Week10_200907_C06_s4_w1512105A2-3028-4E6D-9DCC-2F5CB796FBD0.tif
    │   ├── Week10_200907_C07_s4_w1879F9F61-C5FC-4D93-BD67-6C3F318C6606.tif
    │   ├── Week10_200907_C08_s4_w19DF61E7F-2F93-4123-AC49-AA0817662E29.tif
    │   ├── Week10_200907_C09_s4_w1AB53C280-34E3-4D14-813B-C8A9D12F6E56.tif
    │   ├── Week10_200907_C10_s4_w11D1A4526-36AD-47A1-9054-C5E853C92094.tif
    │   ├── Week10_200907_C11_s4_w1032A8276-94FD-4D49-A1BF-12F511CF4E35.tif
    │   ├── Week10_200907_D02_s4_w1367FF4E3-4C42-4441-9066-CEEEBAC48951.tif
    │   ├── Week10_200907_D03_s4_w166C4B8C2-5D5D-4AAA-AD7F-E2DC438DFCB0.tif
    │   ├── Week10_200907_D04_s4_w106E4067E-9F89-4545-BAD6-9910F8D60EBB.tif
    │   ├── Week10_200907_D05_s4_w15FD3A56E-CCE8-4F9E-976D-0E5A0E1CF66B.tif
    │   ├── Week10_200907_D06_s4_w1E2BD8DD5-E55A-4CDE-B6EE-A6DC8C49AD42.tif
    │   ├── Week10_200907_D07_s4_w1E2486CB3-E73D-4AEB-9BEC-6E5C38045566.tif
    │   ├── Week10_200907_D08_s4_w1514C0575-DDB1-4110-B14E-95119FA85FF9.tif
    │   ├── Week10_200907_D09_s4_w107709937-B04C-41CC-A1BB-255F8C499B24.tif
    │   ├── Week10_200907_D10_s4_w1A8487670-2075-4134-836C-CAB208F98678.tif
    │   ├── Week10_200907_D11_s4_w1E5582706-5F25-4366-B477-69F94CE5113D.tif
    │   ├── Week10_200907_E02_s4_w15BF47DA6-3F2F-48C7-A4DB-B766F4572841.tif
    │   ├── Week10_200907_E03_s4_w1C44D3649-70F9-4919-8A28-A8C1C14D7AD1.tif
    │   ├── Week10_200907_E04_s4_w1C94B58DF-67F9-473A-A73C-CD47A4E55109.tif
    │   ├── Week10_200907_E05_s4_w1CDAB22AF-67E1-44D6-8D32-174309FD0602.tif
    │   ├── Week10_200907_E06_s4_w1B05EB867-9336-4263-A35D-EE6F61E1E478.tif
    │   ├── Week10_200907_E07_s4_w1C87609AD-CBAD-4006-9274-2A5E98E45317.tif
    │   ├── Week10_200907_E08_s4_w1EFFF45BE-EB40-474E-91F5-B19CAB785BDA.tif
    │   ├── Week10_200907_E09_s4_w1C2C45DDA-7155-489E-92C2-FFA7E26B1086.tif
    │   ├── Week10_200907_E10_s4_w13739F8EF-7EEA-4A81-AC7A-5C7B557E65A1.tif
    │   ├── Week10_200907_E11_s4_w12ACA1887-96F1-4BD1-9D55-B6D39D2CCFC2.tif
    │   ├── Week10_200907_F02_s4_w1C6AA18DD-F80A-4995-839C-CD5D61AF5F76.tif
    │   ├── Week10_200907_F03_s4_w1A5EB8746-0AD7-458C-A694-43BC16DCAC2A.tif
    │   ├── Week10_200907_F04_s4_w1437A63CC-8026-44F2-A30F-3291261E93F5.tif
    │   ├── Week10_200907_F05_s4_w1E3F4786B-3689-4771-85E2-F6B9E1EB95D7.tif
    │   ├── Week10_200907_F06_s4_w19F37C07C-5035-45A3-B2BE-38588B882EE0.tif
    │   ├── Week10_200907_F07_s4_w19B407A74-C12F-4476-9355-C1BFB843CE98.tif
    │   ├── Week10_200907_F08_s4_w166B7955B-5702-44FB-A811-989057A9E57E.tif
    │   ├── Week10_200907_F09_s4_w15A971D48-10C5-45FC-A442-8F37ADF0074B.tif
    │   ├── Week10_200907_F10_s4_w1E2A67B77-86E8-4D82-9AE6-C1891804BB53.tif
    │   ├── Week10_200907_F11_s4_w15770CA2F-AA0B-4FFB-A13F-0FE2DC7A3AA3.tif
    │   ├── Week10_200907_G02_s4_w142FA2990-EC8F-43E9-91BE-70ED0846A69E.tif
    │   ├── Week10_200907_G03_s4_w158CD874C-D02F-4C08-A15C-3C4E512A0378.tif
    │   ├── Week10_200907_G04_s4_w1CEAC513E-335D-4C62-A2EF-27E4143AAD6C.tif
    │   ├── Week10_200907_G05_s4_w103572952-DB06-46B8-974D-97BBA6A864BE.tif
    │   ├── Week10_200907_G06_s4_w14CB58CDA-63E3-470E-9F9B-52EEA6449A7A.tif
    │   ├── Week10_200907_G07_s4_w16F5FF8C8-4737-4E4C-B24A-206E981AD982.tif
    │   ├── Week10_200907_G08_s4_w1FDE931CD-9F92-4FD1-8D2E-F4441777EC98.tif
    │   ├── Week10_200907_G09_s4_w14DF3FB85-B19D-4B4F-8769-A0F9C89C6F22.tif
    │   ├── Week10_200907_G10_s4_w16787DC48-B706-4182-BA69-02E42913A12A.tif
    │   ├── Week10_200907_G11_s4_w1C97E64C3-00B1-4693-AE49-A8708F25B55F.tif
    │   ├── image_retrieval.md
    │   └── initial_test_data
    │       ├── 962_F1_1_blue.png
    │       ├── A1_c2.jpg
    │       ├── APEX1_field0_DAPI.tif
    │       ├── APEX1_field1_DAPI.tif
    │       ├── FluorescentCells.jpg
    │       ├── GMC101_miR71KO-40x_DAPI.jpg
    │       ├── PIM2_field0_DAPI.tif
    │       ├── PIM2_field1_DAPI.tif
    │       ├── POLR2B_field0_DAPI.tif
    │       ├── POLR2B_field1_DAPI.tif
    │       ├── SRSF1_field0_DAPI.tif
    │       └── SRSF1_field1_DAPI.tif
    ├── doc
    │   ├── checkin-2024_11_01.md
    │   └── checkin-2024_11_22.md
    ├── requirements.txt
    ├── results
    │   ├── MCF7_AZ138_plot.png
    │   ├── MCF7_AZU_plot.png
    │   ├── MCF7_CDKinhib_plot.png
    │   ├── MCF7_Monastrol_plot.png
    │   ├── MCF7_TKK_plot.png
    │   ├── MCF7_Temozolomide_plot.png
    │   ├── annotated_image_retrieval.md
    │   ├── image_10_Week10_200907_B11_s4_w14222240C-811F-436D-B8A5-22A1C4749191.tif_annotated.png
    │   ├── image_11_Week10_200907_C02_s4_w13F830D82-B5CE-4F35-8104-40D5773B2772.tif_annotated.png
    │   ├── image_12_Week10_200907_C03_s4_w1EFE40D10-5278-4F09-8E89-CCDBFCB8D25E.tif_annotated.png
    │   ├── image_13_Week10_200907_C04_s4_w18EBFCB24-900A-4C6A-858A-7EEE30BC7572.tif_annotated.png
    │   ├── image_14_Week10_200907_C05_s4_w11DFD4B37-6709-4109-9057-D3D6827E4E22.tif_annotated.png
    │   ├── image_15_Week10_200907_C06_s4_w1512105A2-3028-4E6D-9DCC-2F5CB796FBD0.tif_annotated.png
    │   ├── image_16_Week10_200907_C07_s4_w1879F9F61-C5FC-4D93-BD67-6C3F318C6606.tif_annotated.png
    │   ├── image_17_Week10_200907_C08_s4_w19DF61E7F-2F93-4123-AC49-AA0817662E29.tif_annotated.png
    │   ├── image_18_Week10_200907_C09_s4_w1AB53C280-34E3-4D14-813B-C8A9D12F6E56.tif_annotated.png
    │   ├── image_19_Week10_200907_C10_s4_w11D1A4526-36AD-47A1-9054-C5E853C92094.tif_annotated.png
    │   ├── image_1_Week10_200907_B02_s4_w1BBC355D6-EAC9-4C4B-894B-6289981539D6.tif_annotated.png
    │   ├── image_20_Week10_200907_C11_s4_w1032A8276-94FD-4D49-A1BF-12F511CF4E35.tif_annotated.png
    │   ├── image_21_Week10_200907_D02_s4_w1367FF4E3-4C42-4441-9066-CEEEBAC48951.tif_annotated.png
    │   ├── image_22_Week10_200907_D03_s4_w166C4B8C2-5D5D-4AAA-AD7F-E2DC438DFCB0.tif_annotated.png
    │   ├── image_23_Week10_200907_D04_s4_w106E4067E-9F89-4545-BAD6-9910F8D60EBB.tif_annotated.png
    │   ├── image_24_Week10_200907_D05_s4_w15FD3A56E-CCE8-4F9E-976D-0E5A0E1CF66B.tif_annotated.png
    │   ├── image_25_Week10_200907_D06_s4_w1E2BD8DD5-E55A-4CDE-B6EE-A6DC8C49AD42.tif_annotated.png
    │   ├── image_26_Week10_200907_D07_s4_w1E2486CB3-E73D-4AEB-9BEC-6E5C38045566.tif_annotated.png
    │   ├── image_27_Week10_200907_D08_s4_w1514C0575-DDB1-4110-B14E-95119FA85FF9.tif_annotated.png
    │   ├── image_28_Week10_200907_D09_s4_w107709937-B04C-41CC-A1BB-255F8C499B24.tif_annotated.png
    │   ├── image_29_Week10_200907_D10_s4_w1A8487670-2075-4134-836C-CAB208F98678.tif_annotated.png
    │   ├── image_2_Week10_200907_B03_s4_w1E1B49716-E2C2-48FF-91E5-71E844AF38BD.tif_annotated.png
    │   ├── image_30_Week10_200907_D11_s4_w1E5582706-5F25-4366-B477-69F94CE5113D.tif_annotated.png
    │   ├── image_31_Week10_200907_E02_s4_w15BF47DA6-3F2F-48C7-A4DB-B766F4572841.tif_annotated.png
    │   ├── image_32_Week10_200907_E03_s4_w1C44D3649-70F9-4919-8A28-A8C1C14D7AD1.tif_annotated.png
    │   ├── image_33_Week10_200907_E04_s4_w1C94B58DF-67F9-473A-A73C-CD47A4E55109.tif_annotated.png
    │   ├── image_34_Week10_200907_E05_s4_w1CDAB22AF-67E1-44D6-8D32-174309FD0602.tif_annotated.png
    │   ├── image_35_Week10_200907_E06_s4_w1B05EB867-9336-4263-A35D-EE6F61E1E478.tif_annotated.png
    │   ├── image_36_Week10_200907_E07_s4_w1C87609AD-CBAD-4006-9274-2A5E98E45317.tif_annotated.png
    │   ├── image_37_Week10_200907_E08_s4_w1EFFF45BE-EB40-474E-91F5-B19CAB785BDA.tif_annotated.png
    │   ├── image_38_Week10_200907_E09_s4_w1C2C45DDA-7155-489E-92C2-FFA7E26B1086.tif_annotated.png
    │   ├── image_39_Week10_200907_E10_s4_w13739F8EF-7EEA-4A81-AC7A-5C7B557E65A1.tif_annotated.png
    │   ├── image_3_Week10_200907_B04_s4_w1B632CB5F-4D31-42CC-A5D2-0BC6A4D33C28.tif_annotated.png
    │   ├── image_40_Week10_200907_E11_s4_w12ACA1887-96F1-4BD1-9D55-B6D39D2CCFC2.tif_annotated.png
    │   ├── image_41_Week10_200907_F02_s4_w1C6AA18DD-F80A-4995-839C-CD5D61AF5F76.tif_annotated.png
    │   ├── image_42_Week10_200907_F03_s4_w1A5EB8746-0AD7-458C-A694-43BC16DCAC2A.tif_annotated.png
    │   ├── image_43_Week10_200907_F04_s4_w1437A63CC-8026-44F2-A30F-3291261E93F5.tif_annotated.png
    │   ├── image_44_Week10_200907_F05_s4_w1E3F4786B-3689-4771-85E2-F6B9E1EB95D7.tif_annotated.png
    │   ├── image_45_Week10_200907_F06_s4_w19F37C07C-5035-45A3-B2BE-38588B882EE0.tif_annotated.png
    │   ├── image_46_Week10_200907_F07_s4_w19B407A74-C12F-4476-9355-C1BFB843CE98.tif_annotated.png
    │   ├── image_47_Week10_200907_F08_s4_w166B7955B-5702-44FB-A811-989057A9E57E.tif_annotated.png
    │   ├── image_48_Week10_200907_F09_s4_w15A971D48-10C5-45FC-A442-8F37ADF0074B.tif_annotated.png
    │   ├── image_49_Week10_200907_F10_s4_w1E2A67B77-86E8-4D82-9AE6-C1891804BB53.tif_annotated.png
    │   ├── image_4_Week10_200907_B05_s4_w168154335-E870-426E-8C07-AE6243C511B8.tif_annotated.png
    │   ├── image_50_Week10_200907_F11_s4_w15770CA2F-AA0B-4FFB-A13F-0FE2DC7A3AA3.tif_annotated.png
    │   ├── image_51_Week10_200907_G02_s4_w142FA2990-EC8F-43E9-91BE-70ED0846A69E.tif_annotated.png
    │   ├── image_52_Week10_200907_G03_s4_w158CD874C-D02F-4C08-A15C-3C4E512A0378.tif_annotated.png
    │   ├── image_53_Week10_200907_G04_s4_w1CEAC513E-335D-4C62-A2EF-27E4143AAD6C.tif_annotated.png
    │   ├── image_54_Week10_200907_G05_s4_w103572952-DB06-46B8-974D-97BBA6A864BE.tif_annotated.png
    │   ├── image_55_Week10_200907_G06_s4_w14CB58CDA-63E3-470E-9F9B-52EEA6449A7A.tif_annotated.png
    │   ├── image_56_Week10_200907_G07_s4_w16F5FF8C8-4737-4E4C-B24A-206E981AD982.tif_annotated.png
    │   ├── image_57_Week10_200907_G08_s4_w1FDE931CD-9F92-4FD1-8D2E-F4441777EC98.tif_annotated.png
    │   ├── image_58_Week10_200907_G09_s4_w14DF3FB85-B19D-4B4F-8769-A0F9C89C6F22.tif_annotated.png
    │   ├── image_59_Week10_200907_G10_s4_w16787DC48-B706-4182-BA69-02E42913A12A.tif_annotated.png
    │   ├── image_5_Week10_200907_B06_s4_w176CA3679-C863-40B8-98A8-8248552A3D16.tif_annotated.png
    │   ├── image_60_Week10_200907_G11_s4_w1C97E64C3-00B1-4693-AE49-A8708F25B55F.tif_annotated.png
    │   ├── image_6_Week10_200907_B07_s4_w1B39B1CBB-9449-4757-84C8-6F2D156925C7.tif_annotated.png
    │   ├── image_7_Week10_200907_B08_s4_w173DC9509-E539-4402-8C60-5A4BFCF963BA.tif_annotated.png
    │   ├── image_8_Week10_200907_B09_s4_w17414221F-2154-4685-AB36-D6270E11832B.tif_annotated.png
    │   ├── image_9_Week10_200907_B10_s4_w1DABEE4FC-FF53-48AF-B6A7-B19EB9EBABDE.tif_annotated.png
    │   ├── image_data.tsv
    │   ├── image_metadata.tsv
    │   └── initial_test_results
    │       ├── image_1_APEX1_field0_DAPI.tif_annotated.png
    │       ├── image_2_APEX1_field1_DAPI.tif_annotated.png
    │       ├── image_3_PIM2_field0_DAPI.tif_annotated.png
    │       ├── image_4_PIM2_field1_DAPI.tif_annotated.png
    │       ├── image_5_POLR2B_field0_DAPI.tif_annotated.png
    │       ├── image_6_POLR2B_field1_DAPI.tif_annotated.png
    │       ├── image_7_SRSF1_field0_DAPI.tif_annotated.png
    │       ├── image_8_SRSF1_field1_DAPI.tif_annotated.png
    │       ├── image_data_test.tsv
    │       └── image_metadata_test.tsv
    └── src
        ├── initial_test_code
        │   ├── test1_pixel_intensity_single_image.py
        │   ├── test2_alt_avg_intensity_single_image.py
        │   ├── test2_avg_intensity_single_image.py
        │   └── test3_thresholding_masking_single_image.ipynb
        ├── multi_image_analysis.py
        ├── multi_image_analysis_plotting.R
        └── single_image_analysis.py


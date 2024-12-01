# load in the tidyverse library
library(tidyverse)

# read in the data and metadata files
image_data <- read_tsv("~/qb24_image_analysis/results/image_data.tsv")
image_metadata <- read_tsv("~/qb24_image_analysis/results/image_metadata.tsv")

# ensure that the image ID number is recognized as a factor
image_data$image <- factor(image_data$image)

# provide the drug treatment given for each row of the 96-well plate in this particular experiment
B <- "Cdk1/2 inhibitor (NU6102)"
C <- "AZ138"
D <- "AZ-U"
E <- "Temozolomide"
F <- "TKK"
G <- "Monastrol"


# add a column to the metadata file that describes the row on the 96-well plate that each image was taken from (corresponds to the well value in the image name)
image_metadata$treatment <- c(B, B, B, B, B, B, B, B, B, B, 
                                   C, C, C, C, C, C, C, C, C, C, 
                                   D, D, D, D, D, D, D, D, D, D, 
                                   E, E, E, E, E, E, E, E, E, E, 
                                   F, F, F, F, F, F, F, F, F, F, 
                                   G, G, G, G, G, G, G, G, G, G)

# add a column to the metadata file that describes the dosages for each of the treatments 
image_metadata$dosage <- c("DMSO", 10, 3, 1, 0.3, 0.1, 0.03, 0.01, 0.003, "Taxol",
                           "DMSO", 30, 10, 3, 1, 0.3, 0.1, 0.03, 0.01, "Taxol",
                           "DMSO", 30, 10, 3, 1, 0.3, 0.1, 0.03, 0.01, "Taxol",
                           "Taxol", 20, 6, 2, 0.6, 0.2, 0.06, 0.02, 0.006, "DMSO",
                           "Taxol", 10, 3, 1, 0.3, 0.1, 0.03, 0.01, 0.003, "DMSO",
                           "Taxol", 100, 30, 10, 3, 1, 0.3, 0.1, 0.03, "DMSO")

# combine the image data and metadata to label each image with it's appropriate treatment and dosage 
combined_data <- merge(image_data, image_metadata, by = "image", all.x = TRUE)

# split the data in the combined dataframe based on treatment to allow for plotting of treatments separately
split_data <- split(combined_data, combined_data$treatment)


# generate a box plot of average fluorescence intensity per nucleus in each treatment group across each dosage
# also include the a label showing the count (number of nuclei observed) across each dosage
# save each plot as a variable

# CDK1/2 Inhibitor (NU6102) treatment
plot1 <- ggplot(split_data$`Cdk1/2 inhibitor (NU6102)`, 
                mapping = aes(x = dosage, y = average_intensity)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 0, vjust = 0, hjust=0.5),
        plot.title = element_text(hjust = 0.5)) +
  scale_x_discrete(limits = c("DMSO", 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, "Taxol")) +
  ylim(0, 10500) +
  labs(
    title = "Average intensity of MCF-7\n nuclei after CDK1/2 inhibitor treatment",
    x = "Dose (micromolar)",
    y = "Average fluorecsent intensity\n per nucleus") +
  stat_summary(fun = length, aes(label = ..y..), geom = "text", vjust = -0.5, size = 4)


# AZ138 treatment
plot2 <- ggplot(split_data$`AZ138`, 
                mapping = aes(x = dosage, y = average_intensity)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 0, vjust = 0, hjust=0.5), 
        plot.title = element_text(hjust = 0.5)) +
  scale_x_discrete(limits = c("DMSO", 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, "Taxol")) +
  ylim(0, 10500) +
  labs(
    title = "Average intensity of MCF-7\n nuclei after AZ138 treatment",
    x = "Dose (micromolar)",
    y = "Average fluorecsent intensity\n per nucleus") +
  stat_summary(fun = length, aes(label = ..y..), geom = "text", vjust = -0.5, size = 4)


# AZ-U treatment
plot3 <- ggplot(split_data$`AZ-U`, 
                mapping = aes(x = dosage, y = average_intensity)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 0, vjust = 0, hjust=0.5),
        plot.title = element_text(hjust = 0.5)) +
  scale_x_discrete(limits = c("DMSO", 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, "Taxol")) +
  ylim(0, 10500) +
  labs(
    title = "Average intensity of MCF-7\n nuclei after AZ-U treatment",
    x = "Dose (micromolar)",
    y = "Average fluorecsent intensity\n per nucleus") +
  stat_summary(fun = length, aes(label = ..y..), geom = "text", vjust = -0.5, size = 4)


# Temozolomide treatment
plot4 <- ggplot(split_data$`Temozolomide`, 
                mapping = aes(x = dosage, y = average_intensity)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 0, vjust = 0, hjust=0.5),
        plot.title = element_text(hjust = 0.5)) +
  scale_x_discrete(limits = c("DMSO", 0.006, 0.02, 0.06, 0.2, 0.6, 2, 6, 20, "Taxol")) +
  ylim(0, 10500) +
  labs(
    title = "Average intensity of MCF-7\n nuclei after Temozolomide treatment",
    x = "Dose (micromolar)",
    y = "Average fluorecsent intensity\n per nucleus") +
  stat_summary(fun = length, aes(label = ..y..), geom = "text", vjust = -0.5, size = 4)


# TKK treatment
plot5 <- ggplot(split_data$`TKK`, 
                mapping = aes(x = dosage, y = average_intensity)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 0, vjust = 0, hjust=0.5),
        plot.title = element_text(hjust = 0.5)) +
  scale_x_discrete(limits = c("DMSO", 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, "Taxol")) +
  ylim(0, 10500) +
  labs(
    title = "Average intensity of MCF-7\n nuclei after TKK treatment",
    x = "Dose (micromolar)",
    y = "Average fluorecsent intensity\n per nucleus") +
  stat_summary(fun = length, aes(label = ..y..), geom = "text", vjust = -0.5, size = 4)


# Monastrol treatment
plot6 <- ggplot(split_data$`Monastrol`, 
                mapping = aes(x = dosage, y = average_intensity)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 0, vjust = 0, hjust=0.5),
        plot.title = element_text(hjust = 0.5)) +
  scale_x_discrete(limits = c("DMSO", 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, "Taxol")) +
  ylim(0, 10500) +
  labs(
    title = "Average intensity of MCF-7\n nuclei after Monastrol treatment",
    x = "Dose (micromolar)",
    y = "Average fluorecsent intensity\n per nucleus") +
  stat_summary(fun = length, aes(label = ..y..), geom = "text", vjust = -0.5, size = 4)


# save each of the plots above as a separate png file
ggsave(filename = "~/qb24_image_analysis/results/MCF7_CDKinhib_plot.png", plot = plot1)
ggsave(filename = "~/qb24_image_analysis/results/MCF7_AZ138_plot.png", plot = plot2)
ggsave(filename = "~/qb24_image_analysis/results/MCF7_AZU_plot.png", plot = plot3)
ggsave(filename = "~/qb24_image_analysis/results/MCF7_Temozolomide_plot.png", plot = plot4)
ggsave(filename = "~/qb24_image_analysis/results/MCF7_TKK_plot.png", plot = plot5)
ggsave(filename = "~/qb24_image_analysis/results/MCF7_Monastrol_plot.png", plot = plot6)

from PIL import Image
import numpy as np

# Open an image file
img = Image.open('test.png')

# Convert the image to grayscale (optional)
img = img.convert('L')  # 'L' mode means grayscale

# Convert the image to a numpy array
img_array = np.array(img)

# Get the dimensions
print(img_array.shape)  # (height, width, channels) 
# If the image is grayscale, it will not have a channel dimension, so the output would be (height, width).

print(img_array)

np.savetxt('image_array.txt', img_array, fmt='%d')

#### 1. USING FOR loop method To screen through all the numbers in the array to add up all the postive readings (Not setting up threshold yet)

# sum_positive_pixels = 0 # Set the initial counting to be 0. # Assuming 'image_array' is your 2D array of pixel intensity values

# Loop through each element in the array
#for row in img_array:
    # if value > 0:
            #sum_positive_pixels += value
#print(sum_positive_pixels)

### 2. Use NUMPY directly to be more efficient. 
# Calculate the sum and count of positive pixels
positive_pixels = img_array[img_array > 0] # In this step, we can set the threshold for adding up the pixels readings above certain readings
sum_positive_pixels = np.sum(positive_pixels) # Sum up all the readings that are above the certain threshold.
positive_pixel_count = positive_pixels.size # Sum up the number of readings we extract out from the array.
average_positive_pixel = sum_positive_pixels / positive_pixel_count # Do the average calculation for the pixel readings.

print(sum_positive_pixels)
print(positive_pixel_count)
print(average_positive_pixel)




### IF YOU KNOW OR WANT TO SUM UP CERTAIN AREA OF THE ARRAY OR IMAGE, use these. Need to redefine the area range
#row_start, row_end = 10, 20   # Define row range
#col_start, col_end = 15, 25   # Define column range
#sum_of_area = np.sum(image_array[row_start:row_end, col_start:col_end])

#positive_reading = img_array > 0
#labeld_array, num_features = label(positive_reading)
#regions = [np.where(labeled_array == 1, img_array, o)] for i in range(1, num_features + 1)

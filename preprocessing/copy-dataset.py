#import numpy as np
#from PIL import Image
import os
from shutil import copyfile



# You should use this script AFTER using the cropping script.
# Or simply clone "https://github.com/ghjardim/dbt-denoising-dataset/" to some-
#   where in your computer and use the cloned repo as the input of this code.



### DEFINING VARIABLES ###
# Input directory. CHANGE THIS FOR YOUR USE.
const_in_noisy = '/home/guilherme/coding/git/dbt-denoising-dataset/slices_with_noise_aspng'
const_in_clean = '/home/guilherme/coding/git/dbt-denoising-dataset/slices_without_noise_aspng'
# The directories follow the structure: const_in_noisy/ -> 0/, 1/, 2/, ..., 99/ -> files.png
# Example: ...slices_without_noise/0/0.png
#          ...slices_without_noise/0/1.png
# Where the folder 0, ..., 99 is one DBT sample, and the .png files inside are the breast slices.
# The same logic is valid for const_in_clean

# output directory: place to save cropped images.
const_dir_out_base = '/home/guilherme/coding/git/_IC/mydncnn/dncnn/data'
# Inside of it, you'll find: /train/original/, /train/noisy/,
#                            /test/original/, /test/noisy/,
# And /denoised/, a directory which this code will not be interested in.

ratio = 0.7
# Percentile of the dataset designed to training the DnCNN.
# 0.7 => 70% of the data will be used for training, and 30% for testing.



### ALGORITHM ###
# Calculates the number of training and testing images
total_num_of_samples = 0
for _, dirnames, _ in os.walk(const_in_noisy) :
   total_num_of_samples += len(dirnames)

training_num_samples = int(ratio*total_num_of_samples)
testing_num_samples = int((1-ratio)*total_num_of_samples)

# Copying images
for breast in range(total_num_of_samples):
    input_clean = const_in_clean + "/" + str(breast) + "/31.png" 
    input_noisy = const_in_noisy + "/" + str(breast) + "/31.png" 
    # Copying the training samples
    if(breast <= training_num_samples):
        output_clean = const_dir_out_base + "/train/original/" + str(breast) + ".png"
        output_noisy = const_dir_out_base + "/train/noisy/" + str(breast) + ".png"
    else:   # Copying the testing samples
        output_clean = const_dir_out_base + "/test/original/" + str(breast) + ".png"
        output_noisy = const_dir_out_base + "/test/noisy/" + str(breast) + ".png"
    copyfile(input_clean, output_clean)
    print("Copying: " + input_clean + " -> " + output_clean)
    copyfile(input_noisy, output_noisy)
    print("Copying: " + input_noisy + " -> " + output_noisy)

"""
for breast in range(num_of_samples):
  selected_input_directory = const_dir_in + "/" + str(breast) + "/" # It will run through each DBT sample.
  selected_output_directory = const_dir_out + "/" + str(breast) + "/"
  
  if os.path.exists(selected_output_directory) == False:  # If the output folder does not exist, then we'll create it.
    os.mkdir(selected_output_directory)

  for filename in os.listdir(selected_input_directory):
    if filename.endswith(".png"):
      if os.path.exists(selected_output_directory + str(filename)) == True: # Then the file is already cropped. We'll not crop it again.
        print("[SKIPPED] " + selected_output_directory + str(filename) + " already exists.")
      else:                                                                 # The file is not cropped. We'll crop it and save it.
        file = os.path.join(selected_input_directory, filename)
        save_file = os.path.join(selected_output_directory, filename)
        im = Image.open(file)
        region = im.crop((934, 0, 1114, 180 ))                              # Cropping region
        region.save(save_file)
        print("[SAVED] " + str(file))
    else:
      continue
"""

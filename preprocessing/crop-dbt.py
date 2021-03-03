import numpy as np
import os
from PIL import Image



#input directory: images to be cropped. CHANGE THIS FOR YOUR USE.
const_dir_in = '/gdrive/My Drive/Iniciação Científica/C - Base de dados/reconstruida/sem cortes/slices_sem_ruido_aspng'

#output directory: place to save cropped images. CHANGE THIS FOR YOUR USE.
const_dir_out = '/gdrive/My Drive/Iniciação Científica/C - Base de dados/reconstruida/cortada/slices_sem_ruido_aspng'

# The directories follow the structure: const_dir_in/ -> 0/, 1/, 2/, ..., 99/ -> files.png
# Example: ...slices_without_noise/0/0.png
#          ...slices_without_noise/0/1.png
# Where the folder 0, ..., 99 is one DBT sample, and the .png files inside are the breast slices.



num_of_samples = 100

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

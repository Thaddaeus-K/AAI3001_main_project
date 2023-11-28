import os
import random
import shutil

# Set the seed value for reproducibility
random.seed(3001)

# Define the dataset folders
train_data_folder = "MoNuSed 2018 Training Data"
test_data_folder = "MoNuSegTestData"

# Create train, val, and test folders
train_folder = "train"
val_folder = "val"
test_folder = "test"

# Create the train, val, and test folders if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Get the list of tissue types in the test set
test_tissue_types = ["tissue_type_1", "tissue_type_2", "tissue_type_3"]

# Move files to train and val folders from the train_data_folder
for root, dirs, files in os.walk(train_data_folder):
    for file in files:
        # Randomly assign files to train or val folders
        if random.random() < 0.8:
            destination_folder = train_folder
        else:
            destination_folder = val_folder

        # Get the source and destination paths
        source_path = os.path.join(root, file)
        destination_path = os.path.join(destination_folder, file)

        # Copy the file from the source to the destination
        shutil.copy(source_path, destination_path)

# Move files to val and test folders from the test_data_folder
for root, dirs, files in os.walk(test_data_folder):
    for file in files:
        # Check if the tissue type is in the test set
        if any(tissue_type in file for tissue_type in test_tissue_types):
            destination_folder = test_folder
        else:
            destination_folder = val_folder

        # Get the source and destination paths
        source_path = os.path.join(root, file)
        destination_path = os.path.join(destination_folder, file)

        # Copy the file from the source to the destination
        shutil.copy(source_path, destination_path)
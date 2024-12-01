import os
import shutil

# Paths to the dataset
input_dataset = "D:\BANGKIT Bootcamp and Program\container"

output_dataset = "D:\BANGKIT Bootcamp and Program\containersmall"

# List of 18 basic aksara to retain
basic_aksara = [
    "a", "na", "ca", "ra", "ka", "da", "ta", "sa", "wa",
    "la", "ma", "ga", "ba", "nga", "pa", "ja", "ya", "nya"
]

# Ensure output dataset folder exists
os.makedirs(output_dataset, exist_ok=True)

# Iterate through folders in the input dataset
for folder_name in os.listdir(input_dataset):
    folder_path = os.path.join(input_dataset, folder_name)

    # Check if the folder corresponds to a basic aksara
    if folder_name in basic_aksara:
        # Copy the folder to the output dataset
        shutil.copytree(folder_path, os.path.join(output_dataset, folder_name))
        print(f"Copied: {folder_name}")
    else:
        print(f"Skipped: {folder_name}")

print("Reduction to basic 18 aksara completed!")

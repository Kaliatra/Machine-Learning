import os
import shutil
from sklearn.model_selection import train_test_split
from PIL import Image

# Paths
source_folder = "containersmall"  # Folder containing the reduced aksara dataset
final_dataset = "final_dataset"
images_train_folder = os.path.join(final_dataset, "images/train")
images_val_folder = os.path.join(final_dataset, "images/val")
labels_train_folder = os.path.join(final_dataset, "labels/train")
labels_val_folder = os.path.join(final_dataset, "labels/val")

# Dynamically determine the basic aksara list based on folder names (alphabetical order)
basic_aksara = sorted([folder for folder in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, folder))])
aksara_to_label = {aksara: idx for idx, aksara in enumerate(basic_aksara)}

# Print the dynamically generated mapping for verification
print("Dynamically generated aksara-to-label mapping:")
for aksara, label in aksara_to_label.items():
    print(f"{aksara}: {label}")

# Ensure output folders exist
for folder in [images_train_folder, images_val_folder, labels_train_folder, labels_val_folder]:
    os.makedirs(folder, exist_ok=True)

# Iterate over each aksara folder
for aksara in basic_aksara:  # Use dynamically sorted aksara list
    aksara_folder = os.path.join(source_folder, aksara)

    # Create subfolders for the aksara in train and val
    train_aksara_images_folder = os.path.join(images_train_folder, aksara)
    val_aksara_images_folder = os.path.join(images_val_folder, aksara)
    train_aksara_labels_folder = os.path.join(labels_train_folder, aksara)
    val_aksara_labels_folder = os.path.join(labels_val_folder, aksara)

    os.makedirs(train_aksara_images_folder, exist_ok=True)
    os.makedirs(val_aksara_images_folder, exist_ok=True)
    os.makedirs(train_aksara_labels_folder, exist_ok=True)
    os.makedirs(val_aksara_labels_folder, exist_ok=True)

    # Get all image files in the folder
    image_files = sorted(os.listdir(aksara_folder))
    image_paths = [os.path.join(aksara_folder, img) for img in image_files if img.endswith(".jpg")]

    # Split into train and validation
    train_images, val_images = train_test_split(image_paths, test_size=0.2, random_state=42)

    # Process train images
    for img_path in train_images:
        # Copy the image
        img_name = os.path.basename(img_path)
        shutil.copy(img_path, os.path.join(train_aksara_images_folder, img_name))

        # Generate the annotation
        class_label = aksara_to_label[aksara]  # Get the dynamically assigned label
        annotation = f"{class_label} 0.5 0.5 1.0 1.0\n"
        label_path = os.path.join(train_aksara_labels_folder, img_name.replace(".jpg", ".txt"))
        with open(label_path, "w") as label_file:
            label_file.write(annotation)

    # Process validation images
    for img_path in val_images:
        # Copy the image
        img_name = os.path.basename(img_path)
        shutil.copy(img_path, os.path.join(val_aksara_images_folder, img_name))

        # Generate the annotation
        class_label = aksara_to_label[aksara]  # Get the dynamically assigned label
        annotation = f"{class_label} 0.5 0.5 1.0 1.0\n"
        label_path = os.path.join(val_aksara_labels_folder, img_name.replace(".jpg", ".txt"))
        with open(label_path, "w") as label_file:
            label_file.write(annotation)

print("Dataset annotation and split completed!")

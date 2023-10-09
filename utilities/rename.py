import os

# Define the path to the rename.txt file and the image folder
rename_file_path = 'utilities/rename.txt'
image_folder_path = 'imgs/'

# List of valid image file extensions
valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']

# Function to rename images based on instructions in the rename.txt file
def rename_images(rename_file_path, image_folder_path):
    # Check if the rename.txt file exists
    if not os.path.exists(rename_file_path):
        print(f"The file '{rename_file_path}' does not exist.")
        return
    
    # Read instructions from rename.txt and rename images accordingly
    with open(rename_file_path, 'r') as rename_file:
        lines = rename_file.readlines()
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines and comments (lines starting with #)
            if not line or line.startswith('#'):
                continue
            
            # Split the line into old_name and new_name
            old_name, new_name = line.split('=', 1)
            old_name = old_name.strip()
            new_name = new_name.strip()
            
            # Find the old image file by its old name
            old_path = os.path.join(image_folder_path, old_name)
            
            if any(old_path.endswith(ext) for ext in valid_extensions):
                if os.path.exists(old_path):
                    # Construct the new path based on the new name
                    new_path = os.path.join(image_folder_path, new_name)
                    
                    # Rename the image file
                    os.rename(old_path, new_path)
                    print(f"Renamed '{old_name}' to '{new_name}'")
                else:
                    print(f"Image file '{old_name}' not found. Skipping.")
            else:
                print(f"Invalid image format for '{old_name}'. Skipping.")

# Call the function to rename images
rename_images(rename_file_path, image_folder_path)

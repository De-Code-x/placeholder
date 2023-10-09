import os
import json
import re

# Define the path to the description.txt file and the image folder
description_file_path = 'utilities/desc.txt'
image_folder_path = 'imgs/'

# Function to find a matching image file for a given name
def find_matching_image(name):
    for file_name in os.listdir(image_folder_path):
        if re.search(f'{name}', file_name, re.IGNORECASE):
            return file_name
    return None

# Read the description.txt file
with open(description_file_path, 'r') as description_file:
    description_text = description_file.read()

# Split the description into paragraphs
paragraphs = description_text.split('\n')

# Create a list to store name-description pairs
data = []

# Parse the name and description from each paragraph
for paragraph in paragraphs:
    if paragraph.strip():
        # Split each paragraph into name and description
        name, description = paragraph.split(':', 1)
        name = name.strip()
        description = description.strip()
        
        # Find a matching image for the name
        image_name = find_matching_image(name)
        
        # Create a dictionary for each entry
        entry = {
            'Name': name,
            'Description': description,
            'Image': image_name if image_name else 'Image not found'
        }
        data.append(entry)

# Define the path for the output JSON file
output_json_file_path = 'allowedUsers.json'

# Check if the JSON file already exists
if os.path.exists(output_json_file_path):
    overwrite = input(f"The JSON file '{output_json_file_path}' already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
    if overwrite != 'yes':
        print("JSON file not overwritten.")
        exit()

# Write the data to the JSON file
with open(output_json_file_path, 'w') as output_json_file:
    json.dump(data, output_json_file, indent=4)

print(f"JSON file '{output_json_file_path}' has been created successfully.")

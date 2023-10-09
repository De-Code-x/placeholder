# Define the file paths
possible_file = 'possible.txt'
desc_file = 'desc.txt'

# Read the list of names from possible.txt
with open(possible_file, 'r') as file:
    possible_names = [line.strip() for line in file]

# Read and filter the descriptions
filtered_descriptions = []
with open(desc_file, 'r') as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        name = lines[i].split(':')[0].strip()
        if name in possible_names:
            filtered_descriptions.append(lines[i])
            if i + 1 < len(lines):
                filtered_descriptions.append(lines[i+1])
            else:
                print(f"No description found for '{name}' in desc.txt. Skipping.")
        else:
            print(f"Name '{name}' not found in possible.txt. Skipping.")
        i += 2

# Write the filtered descriptions back to desc.txt
with open(desc_file, 'w') as file:
    file.writelines(filtered_descriptions)

print("Filtered descriptions have been saved to desc.txt.")

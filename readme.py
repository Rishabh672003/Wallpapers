import os

# Specify the directory containing the images
image_dir = "/home/rishabh/Pictures/Wallpapers/wallpapers/"

# Get a list of all files in the directory
files = os.listdir(image_dir)

# Filter the list to only include JPG, JPEG, and PNG files
image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
image_files.sort()

# Open the README file in read mode
with open('README.md', 'r') as f:
    # Read the file content
    content = f.read()

# Split the content at the line '# Showcase'
parts = content.split('# Showcase', 1)

# Open the README file in write mode
with open('README.md', 'w') as f:
    # Write the first part (everything before '# Showcase') back to the README file
    f.write(parts[0])

    f.write(f"# Showcase\n\n")
    # Generate the Markdown syntax for each image and write it to the README file
    for image in image_files:
        f.write(f"![](./wallpapers/{image})\n---\n")

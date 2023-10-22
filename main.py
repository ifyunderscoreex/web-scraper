# File name
file_name = "name123.txt"

# Link to add at the beginning of each line
link = '\'https://api.mojang.com/users/profiles/minecraft/'

try:
    # Open the file for reading
    with open(file_name, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Remove leading and trailing whitespace from each line and add the link
    lines_with_link = [link + line.strip() for line in lines]

    # Print the modified lines
    for line in lines_with_link:
        print(line,"',")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

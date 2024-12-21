def modify_file_content(input_filename, output_filename):
    try:
        # Attempt to open and read the file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Content successfully modified and saved to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Insufficient permissions to read '{input_filename}' or write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for filenames
input_file = input("Enter the name of the file to read: ")
output_file = input("Enter the name of the file to save the modified content: ")

# Execute the file modification function
modify_file_content(input_file, output_file)

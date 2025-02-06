# Function to read from a file and write to a new file with modifications
def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            # Read the content from the input file
            content = infile.read()
        
        # Modify the content (e.g., converting it to uppercase)
        modified_content = content.upper()

        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            # Write the modified content to the output file
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"Error: Unable to read/write the file. {e}")

# Example usage:
input_filename = 'input.txt'   # Replace with your input file name
output_filename = 'output.txt'  # Replace with your desired output file name
read_and_write_file(input_filename, output_filename)

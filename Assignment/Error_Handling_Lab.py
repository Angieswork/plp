# Function to handle file reading with error handling
def safe_file_read():
    filename = input("Enter the filename: ")
    
    try:
        # Try opening the file for reading
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except IOError as e:
        print(f"Error: Unable to read the file. {e}")

# Example usage:
safe_file_read()

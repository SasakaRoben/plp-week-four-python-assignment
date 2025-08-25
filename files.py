def modify_content(content):
    
    return content.upper()


def main():
    # Ask user for the input filename
    input_filename = input("Enter the filename to read: ")

    try:
        # Try reading the file
        with open(input_filename, "r") as infile:
            content = infile.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except IOError:
        print("Error: Could not read the file.")
        return

    # Modify the content
    modified_content = modify_content(content)

    # Create a new output filename
    output_filename = "modified_" + input_filename

    try:
        # Write to a new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{output_filename}'")
    except IOError:
        print("Error: Could not write to the new file.")


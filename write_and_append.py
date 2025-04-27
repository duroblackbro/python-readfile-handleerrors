# Task 2: Write and Append Data to a File

def write_and_append(filename):
    # Take user input
    data = input("Enter some text to write to the file: ")

    # Write data to the file
    with open(filename, 'w') as file:
        file.write(data + "\n")

    # Append additional data
    additional_data = input("Enter additional text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(additional_data + "\n")

    # Read and display final content
    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Call the function
write_and_append("output.txt")

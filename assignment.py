# file_handling_assignment.py

def create_file():
    try:
        # Create a new file and write lines to it
        with open("my_file.txt", 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is line 2 with a number: 42\n")
            file.write("Third line: Python file handling is fun!\n")
        print("File created and data written successfully.")
    except (PermissionError, Exception) as e:
        print(f"Error while creating file: {e}")

def read_file():
    try:
        # Read the contents of the file
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("Contents of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied while reading the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        # Append additional lines to the file
        with open("my_file.txt", 'a') as file:
            file.write("Appending a new line 1!\n")
            file.write("Appending a new line 2: 100\n")
            file.write("Final append: Enjoy coding!\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied while appending to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to show the appended content

if __name__ == "__main__":
    main()

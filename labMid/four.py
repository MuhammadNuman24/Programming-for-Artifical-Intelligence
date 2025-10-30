def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")

def write_file(filename):
    text = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(text)

filename = input("Enter the filename: ")
operation = input("Enter the operation (read/write): ")

match operation:
    case 'read':
        read_file('{filename}.txt')
    case 'write':
        write_file('{filename}.txt')
    case _:
        print("Invalid operation. Please specify 'read' or 'write'.")
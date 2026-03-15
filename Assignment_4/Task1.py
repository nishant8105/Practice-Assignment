file_path = 'sample.txt'

try:
    with open(file_path, 'r') as fh:
        for i in range(1, 7):
            content = fh.readline()
            print(f"Line {i}: {content.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
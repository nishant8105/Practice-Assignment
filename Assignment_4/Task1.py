import os 

file_path = 'sample.txt'
if os.path.exists(file_path):
    with open(file_path, 'rt') as fh :
        for i in range(1, 7):
            content = fh.readline()
            # print adds a newline by default, and content already has one, so avoid double newline
            print(f"Line {i} : {content.strip()}")
else :
    print(f"Error : The file '{file_path}' was not found")
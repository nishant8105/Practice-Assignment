# Assignment 4 Report

This report documents the Python scripts created for Assignment 4, focusing on file handling operations.

## Task 1: File Read & Traversal (`Task1.py`)

### Description
This script demonstrates how to check for a file's existence and read its content line by line.

### Explanation
1.  **File Existence Check**: uses `os.path.exists('sample.txt')` to verify if the file exists before attempting to open it.
2.  **Reading File**: Opens `sample.txt` in read text mode (`'rt'`).
3.  **Traversal**: Iterates through the first 6 lines of the file using a loop and `readline()`.
4.  **Output**: Prints each line with its corresponding line number.
5.  **Error Handling**: If the file does not exist, it prints an error message.

## Task 2: File Write & Append Operations (`Task2.py`)

### Description
This script demonstrates how to write data to a file, append data to it, and read the entire content back.

### Explanation
1.  **Writing to File**: Opens `output.txt` in write mode (`'w'`), which creates the file or overwrites it if it exists. Taking user input and writing it to the file.
2.  **Appending to File**: Opens `output.txt` in append mode (`'at'`) to add new content without erasing existing data. Taking user input and appending it.
3.  **Reading File**: Opens `output.txt` in read mode (`'r'`) and prints the entire content to verify the operations.

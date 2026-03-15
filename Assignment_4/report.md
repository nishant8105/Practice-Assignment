# Assignment 4 Journey

Hey there! This is my report for Assignment 4, where I learned a ton about handling files in Python. It was a really good experience figuring out how to read and write text files from scratch.

## What I Learned in Task 1

For the first file, I needed to read some text from `sample.txt`. Originally, I tried to check if the file existed using the `os` module before opening it - but I learned that the proper, Pythonic way to do this is by trying to open the file and handling the exception if it fails.

I set up a `try-except` block to catch a `FileNotFoundError`. This way, if the file isn't there, the program gracefully prints an error message instead of crashing. I also used the simple `'r'` mode and read the file line-by-line using a loop and `readline()`. This is great because it means I don't have to load a massive file all into memory at once.

## What I Learned in Task 2

In the second task, I learned how to create and modify files. First, I opened `output.txt` using `'w'` mode to take text from the user and write it out. Doing this creates the file if it doesn't exist, and completely overwrites it if it does!

Then, to add more without deleting everything I just wrote, I used the append mode (`'a'`). I took some more input and tacked it onto the end. Afterwards, I just opened the file again in read mode (`'r'`) to print everything out and make sure my additions worked correctly.

Overall, learning how to properly use try-except blocks instead of just making `os.path.exists()` checks was the most valuable part. It makes the code feel much more natural and solid.

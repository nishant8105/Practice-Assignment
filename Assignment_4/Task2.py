with open('output.txt', 'w') as fh:
    write = input("Enter text to write to the file : ")
    message = f"{write} \n"
    fh.write(message)
    print(f"Data successfully written to 'output.txt'")
    print()

with open('output.txt', 'at') as fh:
    append = input("Enter additional text to append :")
    message = f"{append} \n"
    fh.write(message)
    print("Data successfully appended.")
    print()

with open('output.txt', 'r') as fh:
    content = fh.read()
    print(content)
    print()
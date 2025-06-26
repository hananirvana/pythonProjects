"""
Text Editor - Notepad style application that can open, edit, and save text documents.
Optional: Add syntax highlighting and other features.
"""
# CLI style
import os

menu = int(input("Notepad Editor 1.0: Welcome! Choose an option by typing its number: \n (1) Create a new File \n (2) Open a file \n (3) Delete a file \n-> "))

if menu == 1:
    lines = []
    print("Enter text: x and hit enter to exit.")
    while True:
        line = input("-> ")
        if line.lower() == 'x':
            break
        lines.append(line)

    ask = str(input("What would you like to name the file? (without .txt suffix): "))
    with open(ask+".txt", "w+") as file:
        file.write(' '.join(lines))
elif menu == 2:
    prompt = str(input("Name of File to read? (without .txt suffix): "))
    with open(prompt+".txt", "r+") as file:
        contents = file.read()
        print(contents)
elif menu == 3:
    question = str(input("Name of File to delete? (without .txt suffix): "))
    try:
        os.remove(question+".txt")
        print("File Deleted.")
    except FileNotFoundError:
        print("Error when trying to find File. Try and type the name again.")

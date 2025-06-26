"""
Count Words in a String - Counts the number of individual words in a string. For added
complexity read these strings in from a text file and generate a summary.
"""

text = str(input("Text to count # of words? "))
lis = text.split()
print(len(lis))

with open("TextsFile1.txt", "r") as file:
    text = file.read()
    print(len(text.split()))

print("File Closed.")

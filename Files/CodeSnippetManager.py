"""
Code Snippet Manager - Another utility program that allows coders to put in
functions, classes or other tidbits to save for use later. Organized by the type
of snippet or language the coder can quickly look up code. Optional: For extra
practice try adding syntax highlighting based on the language.
"""

code = """"""

keyword = ""

def findSnip(keyword, file_path='codes.txt'):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return None

    snippet = ""
    keyword_found = False
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if keyword_found:
            if line == '*' * 78:  # Separator line
                break
            snippet += line + "\n"
        if line == keyword:
            keyword_found = True

    if not snippet:
        print("Keyword not found.")
        return None

    return snippet.strip()  # Remove trailing newline


def saveSnip(keyword, code):
    with open("codes.txt", mode='a') as f:
        f.write(keyword)
        f.write(code)
        f.write("****************************************************************************** \n")

    print("Done saving code!")


saveSnip(keyword,code)
code_snippet = findSnip(keyword)
if code_snippet:
    print(f"Code snippet for keyword '{keyword}':\n{code_snippet}")


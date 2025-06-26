"""
Check if Palindrome - Checks if the string entered by the user is a palindrome. That
is that it reads the same forwards as backwards, like “racecar”
"""

to_check = str(input("What word should be checked if it is a palindrome? ")).lower()

if to_check[::-1] == to_check:
    print(to_check, "is a palindrome!")
else:
    print(to_check, "is not a palindrome!")

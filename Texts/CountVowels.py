"""
Count Vowels - Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""
import re

text = str(input("Text to find the number of vowels in: "))
n_text = re.sub(r'\d+', '', text).lower()
n_vowels = 0
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for i in n_text:
    if i == 'a':
        n_vowels += 1
        vowel_count['a'] += 1
    elif i == 'e':
        n_vowels += 1
        vowel_count['e'] += 1
    elif i == 'i':
        n_vowels += 1
        vowel_count['i'] += 1
    elif i == 'o':
        n_vowels += 1
        vowel_count['o'] += 1
    elif i == 'u':
        n_vowels += 1
        vowel_count['u'] += 1


print("Number of vowels found: ", n_vowels)
print(vowel_count)

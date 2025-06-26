"""
Pig Latin - Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is transposed
to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read
Wikipedia for more information on rules.
"""

word = str(input("What word needs to be translated to pig latin? "))
letter = word[0]
word = word.removeprefix(word[0])
joined = word + letter + "ay"
print(joined)

# Trying a whole text implementing the same idea
sentence = str(input("What sentence needs to be translated to pig latin? "))
words = sentence.split()
lis = []

for i in words:
    letter = i[0]
    i = i.removeprefix(i[0])
    lis.append(i + letter + "ay")

print(' '.join(lis))

"""
Quiz Maker - Make an application which takes various questions from a
file, picked randomly, and puts together a quiz for students. Each quiz
can be different and then reads a key to grade the quizzes.

topics:
artliterature
language
sciencenature
general
fooddrink
peopleplaces
geography
historyholidays
entertainment
toysgames
music
mathematics
religionmythology
sportsleisure
"""

import requests
import json
import getpass

f = open("quiz.txt", "w")
my_secret = getpass.getpass("API_KEY: ")
category = input("What category would you like to choose? (refer to code files for topics)")
questions = int(input("How many questions would you like?"))
ans = []
api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
for i in range(1,questions):
    response = requests.get(api_url, headers={'X-Api-Key': my_secret})
    if response.status_code == requests.codes.ok:
        que = json.loads(response.text)
        f.write(f'{i}. '+que[0]['question']+"\n")
        ans.append(que[0]['answer'])
    else:
        print("Error:", response.status_code, response.text)

print("Done! Check quiz.txt")
f.close()

with open("answers.txt", "w") as file:
    count = 1
    for i in ans:
        file.write(f"{count}. {i}\n")
        count += 1

print("Done writing answers!")

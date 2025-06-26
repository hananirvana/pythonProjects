"""
Coin Flip Simulation - Write some code that simulates flipping a single coin however
many times the user decides. The code should record the outcomes and count the number
of tails and heads.
"""

import random

track = {'Heads': 0, 'Tails': 0}
count = 0

while True:
    ch = input("Flip or not? Y or N: ")
    if ch == 'Y':
        cho = random.randint(0, 1)
        count += 1
        if cho == 0:
            track['Heads'] = track['Heads'] + 1
            print('Heads')
        else:
            track['Tails'] = track['Tails'] + 1
            print('Tails')
    elif ch == 'N':
        break
    else:
        print("Invalid Input, try again! ")

print(f'After {count} outcomes, we got {track["Heads"]} Heads and {track["Tails"]} Tails.')

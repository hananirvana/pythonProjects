"""
Credit Card Validator - Takes in a credit card number from a common credit card vendor
(Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it
is a valid number (look into how credit cards use a checksum).

The algorithm that will be used to verify card numbers is called the Luhn algorithm.

1. The Luhn algorithm starts from the last digit which is called the check digit.
Then moving left from this check digit (←), double the value of every digit at even indices.
2. If the result of this doubling operation is greater than 9 (e.g., 6 × 2 = 12), then subtract 9
from the result (e.g., 12: 12 − 9 = 3) or, equivalently, add the digits of the result (e.g., 12: 1 + 2 =3).
3. Now sum all the digits (including the check digit).
4. If the total is divisible by 10 then the number is valid; otherwise, it is not valid.
"""
import re

def valid_card(card):
    """This function validates a credit card number."""
    card_number = [int(num) for num in card]
    checkDigit = card_number.pop(-1)
    card_number.reverse()

    # Double digits at even indices
    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]

    # Subtract 9 at even indices if digit is over 9
    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]

    card_number.append(checkDigit)
    checkSum = sum(card_number)

    return checkSum % 10 == 0


if __name__ == '__main__':
    card = input("Card Number of which you would like to validate? ")
    print(valid_card(card))

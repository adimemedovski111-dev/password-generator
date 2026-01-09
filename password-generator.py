## Questions: Number of letters; number of symbols; number of numbers

import random

# Our Characters
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "="]

letters1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = []

for char in letters1:
    letters.append(char)


# Randomising our Characters
random.shuffle(numbers)
random.shuffle(symbols)
random.shuffle(letters)


# Receiving our input
n_number = int(input("How many numbers would you like in your password? "))
if n_number > len(numbers):
    raise ValueError(f"Limit of numbers is {len(numbers)}")

n_letter = int(input("How many letters would you like in your password? "))
if n_letter > len(letters):
    raise ValueError(f"Limit of Letters is {len(letters)}")

n_symbols = int(input("How many symbols would you like in your password? "))
if n_symbols > len(symbols):
    raise ValueError(f"Limit of Symbols is {len(symbols)}")

# Gathering our Characters
password = []

testing testing testing

for n in range(n_number):
    password.append(numbers[n])

for l in range(n_letter):
    password.append(letters[l])

for s in range(n_symbols):
    password.append(symbols[s])


# Final Shuffle of our password
random.shuffle(password)


# Joining the characters in our list 
result = "".join(password)

# Printing our result 
print(f"Your password is {result}")

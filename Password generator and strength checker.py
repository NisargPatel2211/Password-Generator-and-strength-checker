#Password Generator and strength checker

import random

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\'' , '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~' ]

password_list=[]

print("Welcome to password generator")

n_uppercase=int(input('Enter how much Uppercase letters you want for your password:'))

n_lowercase=int(input('Enter how much lowercase letters you want for your password:'))

n_digit=int(input('Enter how much digit you want for your password:'))

n_symbols=int(input('Enter how much symbols you want for your password:'))

for i in range(1,n_uppercase+1):

    char = random.choice(uppercase)
           
    password_list += char

for i in range(1,n_lowercase+1):

    char = random.choice(lowercase)
           
    password_list += char

for i in range(1,n_digit+1):

    char = random.choice(digit)
           
    password_list += char

for i in range(1,n_symbols+1):

    char = random.choice(symbols)
           
    password_list += char

random.shuffle(password_list)

password = ''

for char in password_list:

    password += char

print(password)

#Password Generator and strength checker

import random
import re

#Menu

def menu():

    while True:

        print('---------------MENU--------------')
        print("Welcome to password generator\n\n")
        print('1.User input password')
        print('2.System created password')
        print('3.Exit\n')


        ch=int(input('Enter you choice:'))

        if ch==1:

            user_input_password()

        elif ch==2:
            
            password_generator_system()

        elif ch==3:

            print('\nThank you for using this tool!')
            break

        else:

            print('Invalid choice')
            
#Password Generator by system

def password_generator_system():
    
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\'' , '|', ';', ':', '"', ',', '<', '.', '>', '/', '?', '`', '~' ]

    password_list=[]

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

    result = check_password(password)
    
    print(result)


#User input password

def user_input_password():

    while True:

        password = input('Enter password (or write [exit] to end ):')

        if password.lower() == 'exit':

            print('Thank you for using this tool')
            break
            
        result = check_password(password)
        print(result)

#Password Srength Checker

def check_password(password):

    if len(password) <8:
        return '\nPassword length should be minimum of 8 characters'

    if not any(char.isupper() for char in password):
        return '\nPassword should contain minimum of 1 Uppercase'

    if not any(char.islower() for char in password):
        return '\nPassword should contain minimum of 1 Lowercase'

    if not any(char.isdigit() for char in password):
        return '\nPassword should contain minimum of 1 Digit'

    if not re.search(r'[!@#$%^&*()\-_=+\[\]{}|;:",<.>/?`~]', password):
        return '\nPassword should contain minimum of 1 special symbol'

    return f"{password} is strong password"
    

#Run program from here

if __name__ == "__main__":
    menu()

#Password Generator and strength checker

import secrets
import string
import re

#Helper - safely get an integer from the user

def get_int(prompt):

    while True:

        try:
            value = int(input(prompt))

            if value < 0:
                print('Please enter a non-negative number.')
                continue

            return value

        except ValueError:
            print('Please enter a valid number.')


#Menu

def menu():

    while True:

        print('---------------MENU--------------')
        print("Welcome to password generator\n\n")
        print('1.User input password')
        print('2.System created password')
        print('3.Exit\n')

        ch = get_int('Enter you choice:')

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
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digit = string.digits
    symbols = '!@#$%^&*()-_=+[]{}\'|;:",<.>/?`~'

    password_list=[]

    n_uppercase = get_int('Enter how much Uppercase letters you want for your password:')
    n_lowercase = get_int('Enter how much lowercase letters you want for your password:')
    n_digit = get_int('Enter how much digit you want for your password:')
    n_symbols = get_int('Enter how much symbols you want for your password:')

    if n_uppercase + n_lowercase + n_digit + n_symbols == 0:
        print('\nYou must request at least one character.')
        return

    for i in range(n_uppercase):
        password_list.append(secrets.choice(uppercase))

    for i in range(n_lowercase):
        password_list.append(secrets.choice(lowercase))

    for i in range(n_digit):
        password_list.append(secrets.choice(digit))

    for i in range(n_symbols):
        password_list.append(secrets.choice(symbols))

    secrets.SystemRandom().shuffle(password_list)

    password = ''.join(password_list)

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

    issues = []

    if len(password) < 8:
        issues.append('minimum 8 characters')

    if not any(char.isupper() for char in password):
        issues.append('at least 1 uppercase letter')

    if not any(char.islower() for char in password):
        issues.append('at least 1 lowercase letter')

    if not any(char.isdigit() for char in password):
        issues.append('at least 1 digit')

    if not re.search(r'[!@#$%^&*()\-_=+\[\]{}|;:",<.>/?`~]', password):
        issues.append('at least 1 special symbol')

    if issues:
        return '\nPassword needs: ' + ', '.join(issues)

    return f"{password} is a strong password"
    

#Run program from here

if __name__ == "__main__":
    menu()

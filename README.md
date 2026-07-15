# Password Generator & Strength Checker

A simple Python command-line tool that generates strong, customizable passwords and checks the strength of any password you provide.

## Features

- **System-generated passwords** — choose exactly how many uppercase letters, lowercase letters, digits, and symbols you want, and the tool builds a randomly shuffled password to match.
- **User password checker** — enter your own password and get instant feedback on whether it meets strength requirements.
- **Strength validation** based on:
  - Minimum length of 8 characters
  - At least 1 uppercase letter
  - At least 1 lowercase letter
  - At least 1 digit
  - At least 1 special symbol
- Simple, interactive menu-driven interface.

## Requirements

- Python 3.x
- No external dependencies (uses only the built-in `random` and `re` modules)

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/password-generator-and-strength-checker.git
cd password-generator-and-strength-checker
```

## Usage

Run the script:

```bash
python "Password_generator_and_strength_checker.py"
```

You'll see a menu with three options:

```
---------------MENU--------------
Welcome to password generator

1.User input password
2.System created password
3.Exit
```

### Option 1: Check your own password
Enter any password you'd like, and the tool will tell you whether it's strong or which requirement it's missing. Type `exit` to return to the menu.

### Option 2: Generate a password
Specify how many uppercase letters, lowercase letters, digits, and symbols you want included. The tool randomly generates and shuffles a password matching your criteria, then runs it through the strength checker.

### Option 3: Exit
Closes the program.

## Example

```
Enter you choice:2
Enter how much Uppercase letters you want for your password:2
Enter how much lowercase letters you want for your password:4
Enter how much digit you want for your password:2
Enter how much symbols you want for your password:2

aB3!k9pQ@r is strong password
```

## Possible Improvements

- Use Python's `secrets` module instead of `random` for cryptographically secure password generation.
- Add password length as a direct input option.
- Provide a strength score (weak/medium/strong) instead of pass/fail messages.
- Add a GUI or web interface.

## License

This project is open source and available under the [MIT License](LICENSE).

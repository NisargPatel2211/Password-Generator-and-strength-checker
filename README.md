# Password Generator & Strength Checker

A Python command-line tool that generates strong, customizable passwords and checks the strength of any password you provide. Built with security best practices in mind, using Python's `secrets` module for cryptographically secure randomness.

## Features

- **System-generated passwords** — choose exactly how many uppercase letters, lowercase letters, digits, and symbols you want, and the tool builds a securely randomized, shuffled password to match.
- **User password checker** — enter your own password and get instant feedback on every requirement it's missing (not just the first one it finds).
- **Cryptographically secure** — uses the `secrets` module instead of `random`, making generated passwords suitable for real-world use.
- **Robust input handling** — invalid input (non-numbers, negative numbers) is caught and re-prompted instead of crashing the program.
- **Strength validation** based on:
  - Minimum length of 8 characters
  - At least 1 uppercase letter
  - At least 1 lowercase letter
  - At least 1 digit
  - At least 1 special symbol
- Simple, interactive menu-driven interface.

## Requirements

- Python 3.x
- No external dependencies (uses only the built-in `secrets`, `string`, and `re` modules)

## Installation

Clone the repository:

```bash
git clone https://github.com/NisargPatel2211/Password-Generator-and-strength-checker.git
cd Password-Generator-and-strength-checker
```

## Usage

Run the script:

```bash
python "Password generator and strength checker.py"
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
Enter any password you'd like, and the tool will list every strength requirement it fails to meet. Type `exit` to return to the menu.

### Option 2: Generate a password
Specify how many uppercase letters, lowercase letters, digits, and symbols you want included. The tool securely generates and shuffles a password matching your criteria, then runs it through the strength checker. You must request at least one character total.

### Option 3: Exit
Closes the program.

## Example

```
Enter you choice:2
Enter how much Uppercase letters you want for your password:2
Enter how much lowercase letters you want for your password:4
Enter how much digit you want for your password:2
Enter how much symbols you want for your password:2

aB3!k9pQ@r is a strong password
```

```
Enter you choice:1
Enter password (or write [exit] to end ):abc

Password needs: minimum 8 characters, at least 1 uppercase letter, at least 1 digit, at least 1 special symbol
```

## Possible Improvements

- Add a weighted strength *score* (weak/medium/strong/very strong) instead of pass/fail messages.
- Check generated/entered passwords against a common or breached password list.
- Add a maximum length limit and reject whitespace-only passwords.
- Add docstrings to functions for better maintainability.
- Add unit tests (`pytest`) for `check_password`.
- Add a GUI or web interface.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Nisarg Patel**
GitHub: [@NisargPatel2211](https://github.com/NisargPatel2211)

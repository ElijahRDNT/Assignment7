# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

def get_input():
    password_input = input("\nEnter password: ")
    return password_input


def count_letters(letter_numbers):
    number_count = 0
    for n in letter_numbers:
        if n.isalpha():
            number_count = number_count + 1

    if number_count >= 16:
        return True 


def case_letter_validator(letter_check):
    for l in letter_check:
        if l.isupper():
            return True


def number_validator(number_check):
    for n in number_check:
        if n.isdigit():
            return True


def special_char_validation(char_check):
    for n in char_check:
        if not n.isdigit() and not n.isalpha() and n != " ":
            return True

password = get_input()
valid_letter_number = count_letters(password)
valid_case = case_letter_validator(password)
pass_with_number = number_validator(password)
pass_with_special_char = special_char_validation(password)
print(valid_letter_number)
print(valid_case)
print(pass_with_number)
print(pass_with_special_char)
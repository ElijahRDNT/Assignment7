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

def get_input():    # function to get user sentence input
    # no need to convert because inputs have automatically string datatypes
    password_input = input("\nEnter password: ")
    return password_input


def count_letters(letter_numbers):  # function to count number of letters
    number_count = 0
    for n in letter_numbers:    # the program will go through every character one by one to see if they belong to the alphabet letters
        if n.isalpha():         # .isalpha() is a function to check is a character is an alphabet letter
            # if a character belongs to the alphabet letters, number_count will be added by 1 until all the characters are checked
            number_count = number_count + 1

    if number_count >= 16:  # if the number of letters is greater than 15, it will return True value
        return True


# function to check if there is an uppercase letter
def case_letter_validator(letter_check):
    for l in letter_check:  # the program will go through every character one by one to see if there is an uppercase letter
        if l.isupper():     # .isupper is a function to check if a character is an uppercase letter
            return True     # if the program encounters an uppercase letter, it will return True Value


# function to check if there is a number character
def number_validator(number_check):
    for n in number_check:      # the program will go through every character one by one to see if there is a number character
        if n.isdigit():         # .isdigit() is a function to check if a character is a number digit
            return True         # if the program encounters a number character, it will return True Value


# function to check is there is a special character
def special_char_validation(char_check):
    for n in char_check:    # the program will go through every character one by one to see if there is a special character
        # if it is not a number, an alphabet letter, or a "space", then it is a special character
        if not n.isdigit() and not n.isalpha() and n != " ":
            return True     # if the program encounters a special character, it will return True Value


password = get_input()
valid_letter_number = count_letters(password)
valid_case = case_letter_validator(password)
pass_with_number = number_validator(password)
pass_with_special_char = special_char_validation(password)
if valid_letter_number == valid_case == pass_with_number == pass_with_special_char == True:
    print("\nPassword is valid.")
else:
    print("\nERROR: Password is invalid.")
    if valid_letter_number == None:
        print("Note: Password must have atleast 16 letters.")
    if valid_case == None:
        print("Note: Password must have atleast one uppercase/capital letter.")
    if pass_with_number == None:
        print("Note: Password must have atleast one number.")
    if pass_with_special_char == None:
        print("Note: Password must have atleast one special character. (Ex.: !@#$%^&*()_+`~-=)")

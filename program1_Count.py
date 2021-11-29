# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

def get_input():    # function to get user sentence input
    # no need to convert because inputs have automatically string datatypes
    sentence_input = input("\nEnter your sentence input:  ")
    return sentence_input


def count_words(sentence_word_count):   # function to count number of words
    word_count = 1  # word count should be set to 1 to count the first word because we used "spaces" to count words

    for w in sentence_word_count:
        if w == " ":    # if the user inputs a proper syntax of a sentence, the program will add 1 to the number of words if it encounters a "space"
            word_count = word_count + 1

    return word_count


def count_vowels(sentence_vowel_count):  # function to count number of vowels
    vowels = 'aeiou'    # this is the reference for the vowel characters
    vowel_number = 0    # we need to declare a variable before adding a value to it later on

    for v in sentence_vowel_count.lower():  # the program will convert all the letters to lowercase letters to easily check if they are vowels
        if v in vowels:     # the program will go through every letter one by one to see if they belong to the vowel reference above
            # if a character belongs to the vowel reference above, the vowel_number will be added by 1 until all the characters are checked
            vowel_number = vowel_number + 1

    return vowel_number


# function to count number of consonants
def count_consonants(sentence_consonant_count):
    # this is the reference for the consonant characters
    consonants = 'bcdfghjklmnñpqrstvwxyz'
    # we need to declare a variable before adding a value to it later on
    consonant_number = 0

    # the program will convert all the letters to lowercase letters to easily check if they are consonants
    for c in sentence_consonant_count.lower():
        if c in consonants:                     # the program will go through every letter one by one to see if they belong to the consonant reference above
            # if a character belongs to the consonant reference above, the consonant_number will be added by 1 until all the characters are checked
            consonant_number = consonant_number + 1

    return consonant_number


sentence = get_input()
number_of_words = count_words(sentence)
number_of_vowels = count_vowels(sentence)
number_of_consonants = count_consonants(sentence)

print("\n\nWords: " + str(number_of_words) + "\nVowels: " +
      str(number_of_vowels) + "\nConsonants: " + str(number_of_consonants) + "\n")

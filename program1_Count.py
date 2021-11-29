# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

def get_input():
    sentence_input = input("\nEnter your sentence input:  ")
    return sentence_input


def count_words(sentence_word_count):
    word_count = 1

    for w in sentence_word_count:
        if w == " ":
            word_count = word_count + 1

    return word_count


def count_vowels(sentence_vowel_count):
    vowels = 'aeiou'
    vowel_number = 0

    for v in sentence_vowel_count.lower():
        if v in vowels:
            vowel_number = vowel_number + 1

    return vowel_number


def count_consonants(sentence_consonant_count):
    consonants = 'bcdfghjklmnñpqrstvwxyz'
    consonant_number = 0

    for c in sentence_consonant_count.lower():
        if c in consonants:
            consonant_number = consonant_number + 1

    return consonant_number

sentence = get_input()
number_of_words = count_words(sentence)
number_of_vowels = count_vowels(sentence)
number_of_consonants = count_consonants(sentence)

print("\n\nWords: " + str(number_of_words) + "\nVowels: " + str(number_of_vowels) + "\nConsonants: " + str(number_of_consonants) + "\n")
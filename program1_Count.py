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


sentence = get_input()
number_of_words = count_words(sentence)
print("\n\nWords: " + str(number_of_words))
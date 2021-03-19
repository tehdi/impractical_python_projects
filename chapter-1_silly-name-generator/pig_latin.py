#!/usr/local/bin/python3

"""Translate a word to Pig Latin.

To form Pig Latin, you take an English word that begins with a consonant,
move that consonant to the end, and then add “ay” to the end of the word.
If the word begins with a vowel, you simply add “way” to the end of the
word. One of the most famous Pig Latin phrases of all time is “ixnay on the
ottenray,” uttered by Marty Feldman in Mel Brooks’s comedic masterpiece
Young Frankenstein.

Write a program that takes a word as input and uses indexing and
slicing to return its Pig Latin equivalent. Run Pylint and pydocstyle on
your code and correct any style mistakes. You can find a solution in the
appendix or download pig_latin_practice.py from https://www.nostarch.com/
impracticalpython/.
"""

VOWELS = 'aeiou'

def main():
    """Translate a word to Pig Latin.

    Accept a word as input from stdin, then print the Pig Latin translation.
    Only handles basic cases. Does not do thorough input validation. Does
    not look for multiple consonants at the start of the word. Does not
    handle multi-word input.

    Look dude, it's a tiny throwaway function for a practice problem from
    a book called Impractical Python Projects. This is what you get.
    """
    english = input('Word to translate: ')
    if english == '':
        print('No input detected')
    elif english[0] in VOWELS:
        print(english + 'way')
    else:
        print(english[1:] + english[0] + 'ay')

if __name__ == "__main__":
    main()

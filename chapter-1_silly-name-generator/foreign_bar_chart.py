#!/usr/local/bin/python3

"""Create a Poor Foreign Man’s Bar Chart of letter frequency.

Use an online translator to change your text into another Latin-based writ-
ing system (such as Spanish or French), rerun your code from the Poor
Man’s Bar Chart, and compare the results. For example, a Spanish version
of the text in Figure 1-2 yields the results in Figure 1-3

Twice as many Ls and three times as many Us appear in the Spanish
sentence. To make the bar charts for different inputs directly comparable,
change the code so every letter of the alphabet has a key and is displayed
even if there are no values.
"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def main():
    """Create a bar chart of letter frequency for the given input.

    Take input on stdin and print the chart to stdout.
    Output all letters regardless of whether they appear in the input.
    """
    letter_frequency = {letter:0 for letter in ALPHABET}

    # for each letter in input.lower(), increment dict value
    sentence = input('Input to count: ')
    letters = (letter.lower() for letter in sentence if letter.isalpha())
    for letter in letters:
        letter_frequency[letter] += 1

    # for each key in dict.keys.sorted, print '{dict.key}' * dict[key]
    # (sorted so they're printed in alphabetical order)
    for letter,count in sorted(letter_frequency.items()):
        print("{}: {}".format(letter, letter * count))

if __name__ == "__main__":
    main()

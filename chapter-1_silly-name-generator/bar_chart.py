#!/usr/local/bin/python3

"""Create a Poor Man’s Bar Chart of letter frequency.

The six most commonly used letters in the English language can be remembered
with the mnemonic “etaoin” (pronounced eh-tay-oh-in). Write a Python
script that takes a sentence (string) as input and returns a simple
bar-chart–type display.
"""

# https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict

def main():
    """Create a bar chart of letter frequency for the given input.

    Take input on stdin and print the chart to stdout.
    """
    letter_frequency = defaultdict(int)

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

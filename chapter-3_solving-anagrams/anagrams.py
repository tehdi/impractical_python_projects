"""Find anagrams from a dictionary file."""

# https://docs.python.org/3/library/argparse.html
import argparse
from impractical_modules import load_dictionary

DEFAULT_DICTIONARY = "/home/pythondev/resources/words"

parser = argparse.ArgumentParser(description='Find some anagrams.')
parser.add_argument('base_word', help='Word to find anagrams of')
parser.add_argument('-d', '--dictionary', default=DEFAULT_DICTIONARY,
                    help='Path to the file to use as the word dictionary'
                    ' (default: %(default)s)')


def find_anagrams(base_word, filename):
    """Print anagrams from a dictionary file."""
    lower_base_word = base_word.lower()
    sorted_base_word = sorted(lower_base_word)
    anagrams = (word for word in load_dictionary.load(filename)
                if _is_valid(word)
                # a word doesn't count as an anagram of itself
                and word.lower() != lower_base_word
                and _are_anagrams(sorted_base_word, word.lower()))

    print("Anagrams of {} found in {}:".format(base_word, filename))
    # * unpacks args
    # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    print(*anagrams, sep='\n')


def _is_valid(word):
    return (
        "'" not in word
    )


def _are_anagrams(sorted_base_word, word):
    return sorted_base_word == sorted(word)


if __name__ == "__main__":
    args = parser.parse_args()
    find_anagrams(args.base_word, args.dictionary)

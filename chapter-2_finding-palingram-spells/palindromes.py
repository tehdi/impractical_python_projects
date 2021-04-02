"""Find palindromes from a dictionary file."""

# https://docs.python.org/3/library/argparse.html
import argparse
# no path needed to import a module from the same directory
import load_dictionary

RESOURCE_DIR = "/home/pythondev/resources"
DEFAULT_DICTIONARY = RESOURCE_DIR + "/chapter-2_finding-palingram-spells/words"

parser = argparse.ArgumentParser(description='Find some palindromes.')
parser.add_argument('-d', '--dictionary', default=DEFAULT_DICTIONARY,
                    help='Path to the file to use as the word dictionary'
                    ' (default: %(default)s)')
parser.add_argument('-l', '--min_word_length', type=int, default=1,
                    help='Minimum length for a word to be included in results'
                    ' (default: %(default)s)')


def find_palindromes(filename, min_word_length):
    """Print palindromes from a dictionary file."""
    words = load_dictionary.load(filename)
    palindromes = (word for word in words
                   if _is_valid(word, min_word_length)
                   and _is_palindrome(word))

    print("Palindromes found in {}:".format(filename))
    # * unpacks args
    # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    print(*palindromes, sep='\n')


def _is_valid(word, min_word_length):
    return (
        len(word) >= min_word_length
        and len(set(word)) > 1
        and "'" not in word
    )


def _is_palindrome(word):
    return word == word[::-1]


if __name__ == "__main__":
    args = parser.parse_args()
    find_palindromes(args.dictionary, args.min_word_length)

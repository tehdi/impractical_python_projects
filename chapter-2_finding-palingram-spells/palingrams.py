"""Find palingrams from a dictionary file."""

# https://docs.python.org/3/library/argparse.html
import argparse
# no path needed to import a module from the same directory
import load_dictionary

RESOURCE_DIR = "/home/pythondev/resources"
DEFAULT_DICTIONARY = RESOURCE_DIR + "/chapter-2_finding-palingram-spells/words"

parser = argparse.ArgumentParser(description='Find some palingrams.')
parser.add_argument('-d', '--dictionary', default=DEFAULT_DICTIONARY,
                    help='Path to the file to use as the word dictionary'
                    ' (default: %(default)s)')


def find_palingrams(filename):
    """Print palingrams from a dictionary file."""
    valid_words = [word for word in load_dictionary.load(filename)
                   if _is_valid(word)]

    palingrams = []
    for word in valid_words:
        palingramic_pair = _find_palingram(word, valid_words)
        if palingramic_pair:
            palingrams.append((palingramic_pair))
    palingrams.sort()

    print("Palingrams found in {}:".format(filename))
    # * unpacks args
    # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    print(*palingrams, sep='\n')


def _is_valid(word):
    return (
        len(word) > 1
        and len(set(word)) > 1
        and "'" not in word
    )


def _find_palingram(word, words):
    for i in range(len(word)):
        start = word[:i]
        end = word[i:]
        if _is_palindrome(start) and _is_reversed_word(end, words):
            return (end[::-1], word)
        if _is_palindrome(end) and _is_reversed_word(start, words):
            return (word, start[::-1])
    return False


def _is_reversed_word(word, words):
    return word[::-1] in words


def _is_palindrome(word):
    return word == word[::-1]


if __name__ == "__main__":
    args = parser.parse_args()
    find_palingrams(args.dictionary)

"""Find palingrams from a dictionary file."""

# https://docs.python.org/3/library/argparse.html
import argparse
from impractical_modules import load_dictionary

DEFAULT_DICTIONARY = "/home/pythondev/resources/words"

parser = argparse.ArgumentParser(description='Find some palingrams.')
parser.add_argument('-d', '--dictionary', default=DEFAULT_DICTIONARY,
                    help='Path to the file to use as the word dictionary'
                    ' (default: %(default)s)')
parser.add_argument('-l', '--min_word_length', type=int, default=1,
                    help='Minimum length of each word in a palingramic pair'
                    ' for the pair to be included in results'
                    ' (default: %(default)s)')


def find_palingrams(filename, min_word_length):
    """Print palingrams from a dictionary file."""
    valid_words = set(
        word
        for word in load_dictionary.load_lowercase(filename, min_word_length)
        if _is_valid(word))

    palingrams = []
    for word in valid_words:
        palingramic_pair = _find_palingram(word, valid_words, min_word_length)
        if palingramic_pair:
            palingrams.append(palingramic_pair)
    palingrams.sort()

    print("{} palingrams found in {}:".format(len(palingrams), filename))
    # * unpacks args
    # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    print(*palingrams, sep='\n')


def _is_valid(word):
    return (
        len(set(word)) > 1
        and "'" not in word
    )


def _find_palingram(word, words, min_word_length):
    for i in range(len(word)):
        start = word[:i]
        end = word[i:]
        if len(start) < min_word_length or len(end) < min_word_length:
            continue
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
    find_palingrams(args.dictionary, args.min_word_length)

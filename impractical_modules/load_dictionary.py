"""Load a text file into a list.

Arguments:
- Text file name (and directory path if not current directory).
- Minimum length of a word for it to be included in the response.

Exceptions:
- IOError for any problem loading or reading the given file.

Returns:
- A list of all of the words in the text file matching the request.
"""


def load(filename, min_word_length=1):
    """Return the contents of the given file as a list of words."""
    return _load(filename, lambda word: word, min_word_length)


def load_lowercase(filename, min_word_length=1):
    """Return the contents of the given file as a list of lowercase words."""
    return _load(filename, lambda word: word.lower(), min_word_length)


def _load(filename, manipulate_function, min_word_length):
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            return (manipulate_function(word) for word in loaded_txt
                    if len(word) >= min_word_length)
    except IOError as ex:
        # log and reraise to let the caller handle it more appropriately
        print("Error opening [{}]: {}".format(filename, ex))
        raise

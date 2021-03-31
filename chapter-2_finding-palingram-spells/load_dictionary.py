"""Load a text file into a list.

Arguments:
- Text file name (and directory path if not current directory).

Exceptions:
- IOError for any problem loading or reading the given file.

Returns:
- A list of all of the words in the text file, in lower case.
"""

def load(filename):
    """Return the contents of the given file as a list of lowercase words."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            return (word.lower() for word in loaded_txt)
    except IOError as ex:
        # log and reraise to let the caller handle it more appropriately
        print("Error opening [{}]: {}".format(filename, ex))
        raise

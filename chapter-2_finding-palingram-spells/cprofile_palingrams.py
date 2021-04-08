import cProfile
import palingrams

# I'm not committing all the test dictionaries
# but I generated them like this:
# $ head -30000 /usr/share/dict/words >> thirty_thousand_words

# list: 201 function calls in 0.000 seconds
# set: 211 function calls in 0.000 seconds
very_small_dictionary = 'palingram_test_dictionary.txt'

# list: 14996 function calls in 0.038 seconds
# set: 15515 function calls in 0.007 seconds
thousand_word_dictionary = 'thousand_words'

# list: 146608 function calls in 1.705 seconds
# set: 151742 function calls in 0.072 seconds
ten_thousand_word_dictionary = 'ten_thousand_words'

# list: 300063 function calls in 6.422 seconds
# set: 310568 function calls in 0.137 seconds
twenty_thousand_word_dictionary = 'twenty_thousand_words'

# list: 509132 function calls in 19.680 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  55802   19.436    0.000   19.436    0.000 palingrams.py:54(_is_reversed_word)
# set: 524721 function calls in 0.229 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  55355    0.015    0.000    0.015    0.000 palingrams.py:54(_is_reversed_word)
thirty_thousand_word_dictionary = 'thirty_thousand_words'

# list: not completed
# set: 975042 function calls in 0.553 seconds
fifty_thousand_word_dictionary = 'fifty_thousand_words'

# list: not completed
# set: 2073483 function calls in 1.032 seconds
hundred_thousand_word_dictionary = 'hundred_thousand_words'

# list: not completed
# set: 2109226 function calls in 1.047 seconds
# the hottest spots:
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   71863    0.425    0.000    0.780    0.000 palingrams.py:43(_find_palingram)
# 1160113    0.268    0.000    0.268    0.000 palingrams.py:58(_is_palindrome)
whole_dictionary = '/home/pythondev/resources/words'


cProfile.run("palingrams.find_palingrams('{}')".format(whole_dictionary))

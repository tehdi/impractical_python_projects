import cProfile
import palingrams

# I'm not committing all the test dictionaries
# but I generated them like this:
# $ head -30000 /usr/share/dict/words >> thirty_thousand_words

# 201 function calls in 0.000 seconds
very_small_dictionary = 'palingram_test_dictionary.txt'

# 14996 function calls in 0.038 seconds
thousand_word_dictionary = 'thousand_words'

# 146608 function calls in 1.705 seconds
ten_thousand_word_dictionary = 'ten_thousand_words'

# 300063 function calls in 6.422 seconds
twenty_thousand_word_dictionary = 'twenty_thousand_words'

# 509132 function calls in 19.680 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  55802   19.436    0.000   19.436    0.000 palingrams.py:54(_is_reversed_word)
thirty_thousand_word_dictionary = 'thirty_thousand_words'

# not completed
fifty_thousand_word_dictionary = 'fifty_thousand_words'
# not completed
hundred_thousand_word_dictionary = 'hundred_thousand_words'
# not completed
whole_dictionary = '/home/pythondev/resources/chapter-2_finding-palingram-spells/words'


cProfile.run("palingrams.find_palingrams('{}')".format(thirty_thousand_word_dictionary))

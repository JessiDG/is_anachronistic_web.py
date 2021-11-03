#This id the code defining a word object

# from output_obj import output_obj
# from input_obj import input_obj

class word_obj:

    def __init__(self, word):
        self._word = word

    # getter method
    def get_word(self):
        return self._word

    # setter method
    def set_word(self, x):
        self._word = x
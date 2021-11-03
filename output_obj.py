#This is the code defining an output object

# from word_obj import word_obj
# from input_obj import input_obj

class output_obj:

    def __init__(self, words):
        self._words = list(words)

    def serialize(self):
        return {"words": self._words}

    # getter method
    def get_words(self):
        return self._words

    # setter method
    def set_words(self, x):
        self._words = x
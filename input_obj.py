#This is the code defining an input object

# from word_obj import word_obj
# from output_obj import output_obj

class input_obj:

    def __init__(self, text, date):
        self._text = text
        self._date = date

    # getter method
    def get_text(self):
        return self._text

    # setter method
    def set_text(self, x):
        self._text = x

    # getter method
    def get_date(self):
        return self._date

    # setter method
    def set_date(self, x):
        self._date = x
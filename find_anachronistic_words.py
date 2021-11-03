#This is the file where manuscripts are compared to the unique sets by year.

import string

#The class object includes a manuscript and a dictionary, both of which are turned into sets of unique words
class Is_Anachronistic:

    def __init__(self, manuscript, dictionary):
        self.manuscript = self.to_unique_set(manuscript)
        self.dictionary = self.to_unique_set(dictionary)
        # self.unique_set = open("unique_set.txt", "w")
        # self.unique_set.write(str(self.dictionary))
        self.total_word_count = len(dictionary.split())
        self.unique_word_count = len(self.dictionary)

#This is where any text can become the set of its unique words
    def to_unique_set(self, text):
        if type(text) is not str:
            raise TypeError("Please input a string")

        to_remove = string.punctuation + '-' + "\”" + "\"" + "\'" + "“" + "‘" + "’" + string.digits
        stripped_string = ""
        for char in str(text):
            if char in to_remove:
                stripped_string += ' '
            else:
                stripped_string += char.lower()

        list_stripped_string = stripped_string.split()

        unique_words_set = set(list_stripped_string)
        return unique_words_set

#This uses Python's powerful set() function's subtraction ability to determine the overlap between the sets
    def find_difference(self):
        return self.manuscript - self.dictionary

#This is no longer in production use, but it helpful for testing
    def __str__(self):
        i = 0
        difference = self.find_difference()
        return_str = "Analyzing " + str(self.unique_word_count) + " unique words of public domain texts out of " + str(self.total_word_count) + " total words. \n"
        for word in difference:
            if word is not None:
                return_str += str(i) + ": " + str(word) + "\n"
            i += 1
        return return_str

#This is the old main, no longer in production use but useful for testing
# if __name__ == "__main__":
#     ms = open('manuscript.txt', 'r', encoding='utf8')
#     ms_read = ms.read()
#     comparison_text = open('unique_set_1966.txt', 'r', encoding='utf8')
#     comparison_text_read = comparison_text.read()
#     ms_compare = Is_Anachronistic(ms_read, comparison_text_read)
#     print(ms_compare)

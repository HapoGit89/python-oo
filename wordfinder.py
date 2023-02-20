"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """ Machine to read in text file and give out random words  """

    def __init__(self, location):
        """ reads in file and prints number of words in file """
        self.location = location
        self.text = open(location, "r")
        self.words_list = self.lines_to_list(self.text)

    def lines_to_list(self, textfile):
        """ makes wordfile into list and prints num of words"""
        text_list = [line.replace("\n","") for line in textfile]
        print (f"{len(text_list)} words read")
        return text_list

    def random(self):
        """ returns random word out of self.words_list"""
        return self.words_list[random.randint(0, len(self.words_list)-1)]








class SpecialWordFinder(WordFinder):
    """ Subclass of WordFinder which enables to read more complex files
    >>> t = SpecialWordFinder("test.txt")
    3 words read
    >>> t.random() in ['Orange','Apple', 'Car']
    True
    >>> t.words_list == ['Apple', 'Car', 'Orange']
    True

    """
    def __init__(self, location):
        super().__init__(location)
        self.words_list = [x for x in self.words_list if x != "" and x.count("#")==0]
        print (f"{len(self.words_list)} words read")


    def lines_to_list(self, textfile):
        """ makes wordfile into list and prints num of words"""
        text_list = [line.replace("\n","") for line in textfile]
        return text_list
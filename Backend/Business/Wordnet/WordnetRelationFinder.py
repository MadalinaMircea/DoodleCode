from nltk.corpus import wordnet as wn
import re

class WordnetRelationFinder:
    def __init__(self):
        pass

    def get_synsets(self, word):
        return wn.synsets(word)

    def get_main_synset(self, word):
        return wn.synsets(word)[0]

    def get_hypernyms(self, word):
        return self.get_main_synset(word).hypernyms()

    def get_hyponyms(self, word):
        hyponym_synsets = self.get_main_synset(word).hyponyms()
        result = []
        for hyponym in hyponym_synsets:
            name = hyponym.name()
            name = name[:name.index(".")]
            result.append(name)
        return result

    def get_definition(self, word):
        print(word)
        main = self.get_main_synset(word)
        print(main)
        return main.definition()

from Business.Wikipedia.WikipediaInformationExtractor import WikipediaInformationExtractor
from Business.Wordnet.WordnetRelationFinder import WordnetRelationFinder

wiki = WikipediaInformationExtractor()
wn = WordnetRelationFinder()
# import nltk
# nltk.download('wordnet')


print(wn.get_hyponyms("person"))
# print(wn.get_definition("corgi"))
# print(wiki.get_page_summary("corgi"))

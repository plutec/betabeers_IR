import os
import sys
import nltk
from nltk.stem.snowball import EnglishStemmer
from nltk.corpus import stopwords
import pprint

#Based on: http://tech.swamps.io/simple-inverted-index-using-nltk/
 
class Index:
    """ Inverted index datastructure """
 
    def __init__(self, tokenizer, stemmer=None, stopwords=None):
        """
        tokenizer   -- NLTK compatible tokenizer function
        stemmer     -- NLTK compatible stemmer 
        stopwords   -- list of ignored words
        """
        self.tokenizer = tokenizer
        self.stemmer = stemmer
        self.index = dict()
        self.documents = {}
        if not stopwords:
            self.stopwords = set()
        else:
            self.stopwords = set(stopwords)
 
    def lookup(self, text):
        """
        Lookup a text in the index
        """
        to_ret = dict()
        for word in self.tokenizer(text):
            word = word.lower()
            if self.stemmer:
                word = self.stemmer.stem(word)
            if word in self.stopwords:
                print "- Ignore word: %s" % word
                continue

            print "+ Search word: %s" % word

            to_ret.update({id:self.documents.get(id, None) for id in self.index.get(word, list())})
        
        return to_ret

    def add(self, document_id, document):
        """
        Add a document string to the index
        """
        for token in self.tokenizer(document):
            token = token.lower()
            if token in self.stopwords:
                continue
 
            if self.stemmer:
                token = self.stemmer.stem(token)
 
            if document_id not in self.index.get(token, list()):
                if not self.index.has_key(token):
                    self.index[token] = list()
                self.index[token].append(document_id)
 
        self.documents[document_id] = document
 

#Create invertex index
index = Index(nltk.word_tokenize, 
              EnglishStemmer(), 
              nltk.corpus.stopwords.words('english'))

#Add documents
for id in os.listdir('tweets'):
    filename = 'tweets/%s' % id
    content = open(filename, 'rt').read()
    index.add(id, content)


#Search!
search_str = " ".join(sys.argv[1:])
print "Searching \"%s\"" % search_str

results = index.lookup(search_str)

#Prettify to print, please
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results)


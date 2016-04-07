import sys
from nltk.stem.snowball import EnglishStemmer
from nltk.stem.porter import *

snowball = EnglishStemmer()
porter = PorterStemmer()

words = ['has', 'extremming', 'running', 'generously', 'ambitiously']

if len(sys.argv)>1:
    words = [sys.argv[1]]

for word in words:
    print "Stemming for %s" % word
    print "\tPorter: %s" % porter.stem(word)
    print "\tSnowball: %s" % snowball.stem(word)        

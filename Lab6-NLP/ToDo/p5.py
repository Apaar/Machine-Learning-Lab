import nltk

from nltk.corpus import inaugural
from nltk.util import ngrams

obama_words = inaugural.words("2009-Obama.txt")
fd_obama_words = nltk.FreqDist(w.lower() for w in obama_words)
token = fd_obama_words.most_common(50)

#Create your Unigrams
ugs = ngrams(token,1)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(ugs)
for k,v in fdist.items():
    print (k,v)

#Create your bigrams
bgs = ngrams(token,2)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
    print (k,v)

#Create your Trigrams
tgs = ngrams(token,3)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(tgs)
for k,v in fdist.items():
    print (k,v)

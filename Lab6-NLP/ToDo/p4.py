import nltk

from nltk.corpus import inaugural
from nltk.util import ngrams

obama_words = inaugural.words("2009-Obama.txt")
george_words = inaugural.words("1789-Washington.txt")
fd_george_words = nltk.FreqDist(w.lower() for w in george_words)
fd_obama_words = nltk.FreqDist(w.lower() for w in obama_words)

#fd_obama_words.plot(50)
print (fd_obama_words.most_common(50))
print (fd_george_words.most_common(50))

obama = [x[0] for x in fd_obama_words.most_common(50)]
george =  [x[0] for x in fd_george_words.most_common(50)]

print (list( set(obama) & set(george) ))

import nltk

from nltk.corpus import inaugural
from nltk.util import ngrams

def ex1(doc_name):
    doc_words = inaugural.words(doc_name)

    total_words = len(doc_words)

    my_dict = {}
    for i in doc_words:
        if i not in my_dict:
            my_dict[i]=1

    total_distinct_words = len(my_dict)
	
    # Return the word counts
    return (total_words, total_distinct_words)


speech_name = '2009-Obama.txt'
(tokens,types) = ex1(speech_name)
print ("Total words", tokens)
print ("Total distinct words", types)

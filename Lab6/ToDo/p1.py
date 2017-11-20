from nltk import word_tokenize

file_content = open("../input_text1.txt").read()
wordlist = word_tokenize(file_content)

print('\nTokens List:\n')
print(wordlist)

def getNGrams(input_list, n):
    print('\n',n,'_Grams:\n')
    return [input_list[i:i+n] for i in range(len(input_list)-(n-1))]

my_ngram_list = getNGrams(wordlist, 3)
my_ngram_dict = {}

for i in my_ngram_list:
	key = ' '.join(i)
	if key in my_ngram_dict:
		my_ngram_dict[key]+=1
	else:
		my_ngram_dict[key] = 1
		
print(my_ngram_dict)



import re
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

text = "Cherry blossom represents the nature of life and a season of renewal in Japanese culture. Last year, the season attracted nearly five million people and boosted the economy by about $2.7 billion, according to figures from Bloomberg"
text = text.replace('.',' ')

def find_ngrams(data,n):
    words = word_tokenize(data)
    regex_word = [w for w in words if re.search(r'[a-zA-Z0-9]+', w)]
    n_grams = list(ngrams(regex_word,n))
    return n_grams

print("Unigram = ",find_ngrams(text,1))
print("Bigram = ",find_ngrams(text,2))
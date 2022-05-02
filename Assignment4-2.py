import re
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder,BigramAssocMeasures
import operator

n=2
test_sentence = "I love X"
sentences = ["I love you!","I love mom.","I love you so much","I love dog.","I love mom so much.","John love you so bad."]

def find_ngrams(data,n):
    n_grams = []
    for i in data:
        words = word_tokenize(i)
        regex_word = [w for w in words if re.search(r'[a-zA-Z0-9]+', w)]
        for j in ngrams(regex_word,n):
            n_grams.append(j)
    return n_grams

def Unigram_Bigram_count(Unigram,Bigram):
    bigramCounts = {}
    unigramCounts = {}

    for i in Unigram:
        if i in unigramCounts:
            unigramCounts[i] += 1
        else:
            unigramCounts[i] = 1

    for j in Bigram:
        if (j[0],j[1]) in bigramCounts:
            bigramCounts[(j[0],j[1])] +=1
        else:
            bigramCounts[(j[0],j[1])] =1
    
    return unigramCounts, bigramCounts


def calcBigramProb(listOfBigrams, unigramCounts, bigramCounts,word):
    listOfProb = {}
    max_Prob_value = 0
    max_Prob_word = ""
    for bigram in listOfBigrams:
        if(bigram[0] == word): 
            listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word))
            if(listOfProb[bigram] > max_Prob_value):
                max_Prob_value = listOfProb[bigram]
                max_Prob_word = bigram[1]
    return listOfProb , max_Prob_word

test_sentence2 = test_sentence.split()
listOfUnigrams = [i[0] for i in find_ngrams(sentences,1)]
listOfBigrams = find_ngrams(sentences,n)

unigramCounts, bigramCounts = Unigram_Bigram_count(listOfUnigrams,listOfBigrams)
print("\n All the possible Bigrams are ",)
print(listOfBigrams)

print("\n Bigrams frequency ")
print(bigramCounts)

print("\n Unigrams frequency ")
print(unigramCounts)

bigramProb , max_Probability_word = calcBigramProb(listOfBigrams, unigramCounts, bigramCounts,test_sentence2[1])

print("\n Bigrams probability ")
print(bigramProb)

print(f"\n{test_sentence} : {test_sentence2[2]} should be '{max_Probability_word}'")



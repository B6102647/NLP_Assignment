import nltk
from nltk import edit_distance
from nltk.tokenize import word_tokenize

f = open('1-1000.txt','r')
wordFromDict = [line.rstrip() for line in f.readlines()]

inputString = "I opan a bax ant reed a leter"

listString = word_tokenize(inputString)
newString = ""

for i in listString :
    minVal = 100
    word = ""
    for j in wordFromDict :
        val =  edit_distance(i,j)
        if val < minVal: 
            minVal = val
            word = j
    newString += word + " "
    print(f"{i} can be replaced by ('{word}', {minVal})")

print("\nMispelled sentence is >> ",inputString)
print("New sentence is       >> ",newString)

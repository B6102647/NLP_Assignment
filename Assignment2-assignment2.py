import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import re
import csv
import pandas as pd

# Import csv file 
data = ""
with open('tweets_all.csv',errors="ignore") as myfile:
    reader = csv.reader(myfile,delimiter = '\n')
    for row in reader:
        data += row[0]

# Find number of sentence
sentence = sent_tokenize(data)
print("The number of sentences: ",len(sentence))

# Word tokenize
words = word_tokenize(data)

# Create a pattern to find words to search for
pattern = '[a-zA-Z]{3,}'
regex = re.compile(pattern)
search = regex.findall(data)

# Add stop word in english
stop_words = set(stopwords.words('english'))

# Filter to remove stop words 
wordsFiltered = []
for w in search:
    if w not in stop_words:
        wordsFiltered.append(w)

# Find the most used words
fdist = FreqDist(wordsFiltered)

# Sort the most used words
sortData = sorted(fdist.items(),key=lambda k:k[1] ,reverse=True)

# Show sort of the most used 20 words 
for i in range(20):
    print(sortData[i])

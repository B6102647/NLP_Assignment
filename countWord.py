from nbformat import read
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import re
import csv
import pandas as pd

# Set Data
data = "Rose color on the dial has lost at some places and it continues to happen at other areas too. I am really disappointed. OK quality for the price. The watch is light and looks good. It was simply scratched one the band and the color lost on some areas. Jeweler says a major part is broken and that watch is so badly assembled that repair is impossible. I LOVE THIS WATCH! WONDERFUL COLOR & VERY ELEGANT. Got this for my wife for Christmas. She loves everything about it. Beautiful was a bit too small. Needed to order extra links but I got it sorted and my mother in law loved it. It was a really pretty watch, but how do i order extra links for it ? Its a little tight."


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
        wordsFiltered.append(w.lower())

# Find the most used words
fdist = FreqDist(wordsFiltered)

# Sort the most used words
sortData = sorted(fdist.items(),key=lambda k:k[1] ,reverse=True)


# Show sort of the most used 20 words 
for i in range(len(sortData)):
    print(i," = ",sortData[i])

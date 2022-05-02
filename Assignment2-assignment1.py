import nltk
from nltk.tokenize import word_tokenize
import re
from nltk.corpus import gutenberg, nps_chat
# nltk.download() 

moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
# for w in moby: print(w, end = ' ')

data = []
for w in moby:
    if(re.search("^[0-9]{2}$",w)):
        data.append(w)
mylist = list(dict.fromkeys(data))
print(sorted(mylist))
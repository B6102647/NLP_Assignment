from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk, RegexpParser
from nltk.chunk import conlltags2tree, tree2conlltags
import re
from termcolor import colored

text = "President Joe Biden is expected to call for the most sweeping revamp of US benefits since the 1960s as he delivers his first address to a joint session of Congress."

tree = ne_chunk(pos_tag(word_tokenize(text)))
print(tree)

iob_tags = tree2conlltags(tree)
print(iob_tags)
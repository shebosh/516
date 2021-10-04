import nltk
nltk.download()
from nltk.book import *

#Ex. 24
sorted(w for w in set(text6) if w.endswith('ise'))  #words ending with ise
sorted(w for w in set(text6) if 'z' in w) #words containing z
sorted(w for w in set(text6) if 'pt' in w) #words containing pt
sorted(w for w in set(text6) if w.istitle()) #titlecase

#Ex. 25
sorted(item for item in set(sent) if item.startswith('sh')) #words beginning with sh
[w for w in sent if len(w)>4] #longer than 4 characters
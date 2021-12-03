import nltk

# Ex. 18 Bigrams
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
textWords = [w.lower() for w in webtext.words('pirates.txt')]
finder = BigramCollocationFinder.from_words(textWords)
finder.nbest(BigramAssocMeasures.likelihood_ratio, 50)

# Ex 19
# table of word frequencies by genre
religion_text = brown.words(categories='religion')
fdist = nltk.FreqDist(w.lower() for w in religion_text)
commons = ['hell', 'heaven', 'Lord', 'church', 'sin', 'angels']
for c in commons:
    print(c + ':', fdist[c], end=' ')

cfd = nltk.ConditionalFreqDist((genre, word)
            for fileid in gutenberg.fileids()
            for word in gutenberg.words(fileids)
fileids=['shakespeare-caesar.txt', 'shakespeare-hamlet.txt']
words=['tragedy', 'trouble', 'love', 'doubt']
cfd.tabulate(conditions=fileids, samples=words)

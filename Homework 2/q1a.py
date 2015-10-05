"""
Kya Miller
LING 539 Assignment 2
Q1A - Writes 100 most frequent unigrams, bigrams, and trigrams with their counts in descending order to output file
ngram_frequencies.txt in a simple table. Does the same thing for POS tags and saves to same file. The outputs are formatted
using tabs.
"""

import re
from collections import Counter


def makeTop100List(tokensList):
    frequencyDict = Counter()
    for token in tokensList:
        frequencyDict[token] += 1

    return frequencyDict.most_common(100)

filein = open('browntag_nolines.txt', 'r')
brownTagNoLines = filein.read()
filein.close()

outputFile = open('ngram_frequencies.txt', 'w')

wordsPOSTags = brownTagNoLines.split(' ')
wordsUnigrams = []
posTagsUnigrams = []

for token in wordsPOSTags:
    splitWordPOS = token.split('_', 1)
    word = splitWordPOS[0]
    tag = splitWordPOS[1]
    if re.search('_', tag):
        resplit = tag.split('_', 1)
        word = '%s%s' % (word, resplit[0])
        tag = resplit[1]
    wordsUnigrams.append(word)
    posTagsUnigrams.append(tag)

wordsBigrams = ['%s\t%s' % (wordsUnigrams[i], wordsUnigrams[i + 1]) for i in range(len(wordsUnigrams) - 1)]
wordsTrigrams = ['%s\t%s\t%s' % (wordsUnigrams[i], wordsUnigrams[i + 1], wordsUnigrams[i + 2]) for i in
                 range(len(wordsUnigrams) - 2)]

posTagsBigrams = ['%s\t%s' % (posTagsUnigrams[i], posTagsUnigrams[i + 1]) for i in range(len(posTagsUnigrams) - 1)]
posTagsTrigrams = ['%s\t%s\t%s' % (posTagsUnigrams[i], posTagsUnigrams[i + 1], posTagsUnigrams[i + 2]) for i in
                   range(len(posTagsUnigrams) - 2)]

wordsUnigramsTop100List = makeTop100List(wordsUnigrams)
wordsBigramsTop100List = makeTop100List(wordsBigrams)
wordsTrigramsTop100List = makeTop100List(wordsTrigrams)

posUnigramsTop100List = makeTop100List(posTagsUnigrams)
posBigramsTop100List = makeTop100List(posTagsBigrams)
posTrigramsTop100List = makeTop100List(posTagsTrigrams)

outputFile.write('Top 100 Unigrams (words)')
outputFile.write('\n--------\n')

for unigram in wordsUnigramsTop100List:
    formattedString = '%s\t%s\n' % (unigram[0], unigram[1])
    outputFile.write(formattedString)

outputFile.write('\n\n')
outputFile.write('Top 100 Bigrams (words)')
outputFile.write('\n--------\n')

for bigram in wordsBigramsTop100List:
    formattedString = '%s\t%s\n' % (bigram[0], bigram[1])
    outputFile.write(formattedString)

outputFile.write('\n\n')
outputFile.write('Top 100 Trigrams (words)')
outputFile.write('\n--------\n')

for trigram in wordsTrigramsTop100List:
    formattedString = '%s\t%s\n' % (trigram[0], trigram[1])
    outputFile.write(formattedString)

outputFile.write('\n\n')
outputFile.write('Top 100 Unigrams (pos)')
outputFile.write('\n--------\n')

for unigram in posUnigramsTop100List:
    formattedString = '%s\t%s\n' % (unigram[0], unigram[1])
    outputFile.write(formattedString)

outputFile.write('\n\n')
outputFile.write('Top 100 Bigrams (pos)')
outputFile.write('\n--------\n')

for bigram in posBigramsTop100List:
    formattedString = '%s\t%s\n' % (bigram[0], bigram[1])
    outputFile.write(formattedString)

outputFile.write('\n\n')
outputFile.write('Top 100 Trigrams (pos)')
outputFile.write('\n--------\n')

for trigram in posTrigramsTop100List:
    formattedString = '%s\t%s\n' % (trigram[0], trigram[1])
    outputFile.write(formattedString)

outputFile.close()

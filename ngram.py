import re
import nltk
import string
from nltk.collocations import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def getBigrams(data):
    
    #print("In getBigrams")
    data = data.lower()
    data_without_punc = "".join(c for c in data if c not in (string.punctuation))

    stopset = set(stopwords.words('english'))
##    bigram_measures = nltk.collocations.BigramAssocMeasures()
##    trigram_measures = nltk.collocations.TrigramAssocMeasures()

    tokens_all = word_tokenize(data_without_punc)
    tokens = [w for w in tokens_all if not w in stopset and not w.isdigit()]

    #make bigrams out of tokens
    bigrams = list(nltk.bigrams(tokens))
   
    return bigrams



def getTrigrams(data):
    
    #print("In getTrigrams")
    data_without_punc = "".join(c for c in data if c not in (string.punctuation))

    stopset = set(stopwords.words('english'))
##    bigram_measures = nltk.collocations.BigramAssocMeasures()
##    trigram_measures = nltk.collocations.TrigramAssocMeasures()

    tokens_all = word_tokenize(data_without_punc)
    tokens = [w for w in tokens_all if not w in stopset and not w.isdigit()]

    #make bigrams out of tokens
    trigrams = list(nltk.trigrams(tokens))
   
    return trigrams






def generateFreqDist(generateFreqDist_ngram):
    
    #print("in makeNgram() ")
##    bigram = nltk.bigrams(tokens)
##    trigram = nltk.trigrams(tokens) 

    fdist = nltk.FreqDist(generateFreqDist_ngram)
##    fdist_tri = nltk.FreqDist(trigram)

    list_ngram = []
##    list_trigram = []

    list_ngram = sorted(fdist.items(), key = lambda t:(-t[1],t[0]))               
##    list_trigram = sorted(fdist_tri.items(), key = lambda t:(-t[1],t[0]))               

    #print(tokens)
    #print(list_bigram)
    #print(list_trigram)
    return list_ngram
       

def main():
    print("main")
    out=open(r'C:\Python34\bigram.txt','w')
    freqDistBigrams=[]
    bigrams = []
    data = "What happened? What happened? I went back a second time!! I went ?and .ordered the 64567438 fried-chicken salad and the fried chicken sandwich for my bf. It wasn't as fresh and flavorful as the time before. Kind of a bummer. Maybe they got a new chef? What happened?"
    data2 = "What happened santosh"
##    x = tokenize(data)
##    print(type(x))
    bigrams.extend(getBigrams(data))
    bigrams.extend(getBigrams(data2))
    #bigrams=bigrams.append(makeNgram(tokens))
    freqDistBigrams = generateFreqDist(bigrams)
##    print(freqDistBigrams)
    for bigram in freqDistBigrams:
        out.write(str(bigram[0]) + "\n")
    out.close()

    bigramLookup={}

    lineNumber=0
    
    for line in open(r'C:\Python34\bigram.txt','r'):
        bigramLookup[line.rstrip("\n")]=lineNumber+1
        lineNumber += 1

    #print(bigramLookup)
        

    test_data="What the fuck just happened. What happened?"
    bigrams = []
    bigrams.extend(getBigrams(test_data))
    freqDistBigrams = generateFreqDist(bigrams)
    print(freqDistBigrams)
    print(bigramLookup)

    result = open(r'C:\Python34\bigramResult.txt','w')
    
    for bigram in freqDistBigrams:
        x=str(bigram[0])
        print("searching" + x)
        if x not in bigramLookup:
            print("not found")
            result.write(str(bigram[0])+ "," + str(100)+"\n")
        else:
            print("Found")
            result.write(str(bigram[0]) + "," + str(bigramLookup[x]) + "\n")

    print("Done")
    result.close()
        
    

if __name__=='__main__':
    main()
    

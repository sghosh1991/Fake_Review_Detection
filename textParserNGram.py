import os
import json
import offlineFeatures
import onlineFeatures
import hashlib
import re
import datetime
import traceback
from ranking import Ranking

#print(os.listdir())

totalReviews = 0
formatTimestamp = "%d%b%H%M%S"
timestamp = datetime.datetime.now()
pattern = r'[^ ]+'
path = r'C:\Python34\sampleData\Done2'
#path = r'C:\Users\Santosh\Documents\DataMining\project\raviData'
#outputFileRecommended = open(r'C:\Python34\bigramDataRecommended_' + timestamp.strftime(formatTimestamp) + '.txt','w')
#outputFileNonRecommended = open(r'C:\Python34\bigramDataNonRecommended_' + timestamp.strftime(formatTimestamp) + '.txt','w')
#print(str(totalReviews))



def bigramsRecommended():

    print("\nStarting Recommended Review Processing\n")
    outputFileRecommended = open(r'C:\Python34\bigramRecommended\bigramDataRecommended.txt','w')
    dataFiles = [(x) for x in os.listdir(path) if os.path.isfile(path+"\\"+x)]
    bigramsRecommended=[]
    reviewText=""
    totalReviews = 0
    #print(str(totalReviews))
        

    for p in dataFiles[0:len(dataFiles)]:

        print("Opening :" + p)

        try :
            
            with open(path+"\\"+p) as file:

                a = 1
            
                simpleJson = json.load(file)
                            
                for RecomendedReviewObject in simpleJson["Reccomnded"]:

                    totalReviews = totalReviews + 1
                    
                    #print(nonRecomendedReviewObject["ReviewComment"])
                    reviewText = RecomendedReviewObject["ReviewComment"]
                    
                    #hash the text to create unique ID
                    h = hashlib.md5(reviewText.encode('utf-8'))
                    h1 = hashlib.md5(p.encode('utf-8'))
                    
                    #ngram Feature
                    
                    bigramsRecommended.extend(offlineFeatures.BigramConstructor(reviewText))



                print("Processed :" + p)

            
        except UnicodeDecodeError as e:
            continue
        except KeyError:
            continue

        except Exception as e:
            print("Error in "+ reviewText)
            print(traceback.format_exc())
            outputFileRecommended.close()
            break

    #at this point all reviews in all files have been tokenised and bigrans collected
    #Make frequency dist of bigrams

    freqDistBigrams=offlineFeatures.nGramFreqDistGenerator(bigramsRecommended)

    for bigram in freqDistBigrams:

        try: 
            outputFileRecommended.write(str(bigram[0]) + ";" + str(bigram[1])+"\n")

        except UnicodeEncodeError as e:
            print("Error writing out" + str(bigram[0]))
            continue
        
    outputFileRecommended.close()

    print("Total Recommended Reviews Processed: " + str(totalReviews))







def bigramsNonRecommended():

    print("\nStarting Non Recommended Review Processing\n")
    outputFileNonRecommended = open(r'C:\Python34\bigramNonRecommended\bigramDataNonRecommended.txt','w',encoding='utf-8')
    dataFiles = [(x) for x in os.listdir(path) if os.path.isfile(path+"\\"+x)]
    bigramsNonRecommended=[]
    reviewText=""
    totalReviews = 0
        

    for p in dataFiles[0:len(dataFiles)]:

        print("Opening :" + p)

        try :
            
            with open(path+"\\"+p) as file:

                a = 1
            
                simpleJson = json.load(file)
                            
                for nonRecomendedReviewObject in simpleJson["nonReccomnded"]:

                    totalReviews = totalReviews + 1
                    
                    #print(nonRecomendedReviewObject["ReviewComment"])
                    reviewText = nonRecomendedReviewObject["ReviewComment"]
                    
                    #hash the text to create unique ID
                    h = hashlib.md5(reviewText.encode('utf-8'))
                    h1 = hashlib.md5(p.encode('utf-8'))
                    
                    #ngram Feature
                    
                    bigramsNonRecommended.extend(offlineFeatures.BigramConstructor(reviewText))



                print("Processed :" + p)

            
        except UnicodeDecodeError as e:
            continue
        except KeyError:
            continue

        except Exception as e:
            print("Error in "+ reviewText)
            print(traceback.format_exc())
            outputFileNonRecommended.close()
            break

    #at this point all reviews in all files have been tokenised
    #Make bigrams out of tokens

    #print(bigramsNonRecommended)
    freqDistBigrams=offlineFeatures.nGramFreqDistGenerator(bigramsNonRecommended)
    #print(freqDistBigrams)

    for bigram in freqDistBigrams:
        try:
            
            outputFileNonRecommended.write(str(bigram[0]) + ";" + str(bigram[1])+"\n")
        except UnicodeEncodeError as e:
            
            print("Error writing out" + str(bigram[0]))
            continue
            
    outputFileNonRecommended.close()

    print("Total Non Recommended Reviews Processed: " + str(totalReviews))





def giveScoreToEachReview():
    
    
    #code to make a dictionary out of the collected bigrams

    #Dictionary for Recommended reviews
    
    bigramLookup={}
    
    for line in open(r'C:\Python34\bigramRecommended\bigramsRecommendedTop500.csv','r'):

        temp = line.split('"')
        bigramLookup[temp[1]]=temp[2].rstrip("\n").lstrip(",")
    #print(bigramLookupRecommended)
        
    #scoreRecommended(bigramLookup)
    scoreNonRecommended(bigramLookup)
    #scoreNonRecommended(bigramLookup)
    #scoreRecommended(bigramLookup)
    
    return


   


def scoreRecommended(bigramLookupRecommended):


    print("In recommended review scoring function")
    grandTotal = 0
    #codde to loop over the files and collect bigrams for each
    #bigramsRecommended=[]
    result = open(r'C:\Python34\bigramscoreTestR_R.txt','w')
    pathToFiles=r'C:\Python34\sampleData\testingdataFile'
    
    dataFiles = [(x) for x in os.listdir(pathToFiles) if os.path.isfile(pathToFiles+"\\"+x)]
    a=0
    for p in dataFiles[0:len(dataFiles)]:

        print("Opening :" + p)

        totalReviews = 0

        try :
            
            with open(pathToFiles+"\\"+p) as file:

                a = 1
            
                simpleJson = json.load(file)
                            
                for RecomendedReviewObject in simpleJson["Reccomnded"]:

                    totalReviews = totalReviews + 1
                    grandTotal = grandTotal +1
                    bigramsRecommended=[]
                    
                    #print(nonRecomendedReviewObject["ReviewComment"])
                    reviewText = RecomendedReviewObject["ReviewComment"]
                    
                    #hash the text to create unique ID
                    h = hashlib.md5(reviewText.encode('utf-8'))
                    
                    
                    #ngram Feature
                    
                    bigramsRecommended.extend(offlineFeatures.BigramConstructor(reviewText))

                    #get freq dis of this review's bigrams
                    freqDistBigrams=offlineFeatures.nGramFreqDistGenerator(bigramsRecommended)

                    freqDistBigrams = convertToRanks(freqDistBigrams)


                    #print(freqDistBigrams)

                    #iterate over the createddistribution to gfind ngram distances

                    distFromRecommended=0
                    
                    for bigram in freqDistBigrams:
                        
                        x=str(bigram[0])
                        #print("searching" + x + "with score "+ str(bigram[1]))
                        if x not in bigramLookupRecommended:
                            #print("not found")
                            distFromRecommended = distFromRecommended + 500
                            #print(str(distFromRecommended))
                            
                        else:
                            #print("Found")
                            distFromRecommended = distFromRecommended + abs(int(bigramLookupRecommended[x])-bigram[1])
                            #print(str(distFromRecommended))
                    print("Review " + str(totalReviews) + " Done")

                    result.write(h.hexdigest()+ "," + str(distFromRecommended)+"\n")

                print("Processed " + p)

        except UnicodeDecodeError as e:
            
            print("Could not open " + p)
            continue
        except Exception as e:
            
            print(traceback.format_exc())
            result.close()
            break
    print("FUCKING " + str(grandTotal) + " Reviews")  
    result.close()





def scoreNonRecommended(bigramLookupRecommended):


    print("In non recommended review scoring function")
    grandTotal = 0
    #codde to loop over the files and collect bigrams for each
    
    result = open(r'C:\Python34\bigramscoreTestNR_R.txt','w')
    pathToFiles=r'C:\Python34\sampleData\testingdataFile'
    
    dataFiles = [(x) for x in os.listdir(pathToFiles) if os.path.isfile(pathToFiles+"\\"+x)]
    a=0
    for p in dataFiles[0:len(dataFiles)]:

        print("Opening :" + p)

        totalReviews = 0

        try :
            
            with open(pathToFiles+"\\"+p) as file:

                a = 1
            
                simpleJson = json.load(file)
                            
                for nonRecomendedReviewObject in simpleJson["nonReccomnded"]:

                    totalReviews = totalReviews + 1
                    grandTotal = grandTotal +1
                    bigramsNonRecommended=[]
                    
                    #print(nonRecomendedReviewObject["ReviewComment"])
                    reviewText = nonRecomendedReviewObject["ReviewComment"]
                    
                    #hash the text to create unique ID
                    h = hashlib.md5(reviewText.encode('utf-8'))
                    
                    
                    #ngram Feature
                    
                    bigramsNonRecommended.extend(offlineFeatures.BigramConstructor(reviewText))

                    #get freq dis of this review's bigrams
                    freqDistBigrams=offlineFeatures.nGramFreqDistGenerator(bigramsNonRecommended)

                    freqDistBigrams = convertToRanks(freqDistBigrams)


                    #print(freqDistBigrams)

                    #iterate over the createddistribution to gfind ngram distances

                    distFromRecommended=0
                    
                    for bigram in freqDistBigrams:
                        
                        x=str(bigram[0])
                        #print("searching" + x + "with score "+ str(bigram[1]))
                        if x not in bigramLookupRecommended:
                            #print("not found")
                            distFromRecommended = distFromRecommended + 500
                            #print(str(distFromRecommended))
                            
                        else:
                            #print("Found")
                            distFromRecommended = distFromRecommended + abs(int(bigramLookupRecommended[x])-bigram[1])
                            #print(str(distFromRecommended))
                    print("Review " + str(totalReviews) + " Done")

                    result.write(h.hexdigest()+ "," + str(distFromRecommended)+"\n")

                print("Processed " + p)

        except UnicodeDecodeError as e:
            
            print("Could not open " + p)
            continue
        except Exception as e:
            
            print(traceback.format_exc())
            result.close()
            break
    print("FUCKING " + str(grandTotal) + " Reviews")  
    result.close()











   
def convertToRanks(freqDistBigrams):

    #print("In RANKING")
    #print(freqDistBigrams)
    freqList = [x[1] for x in freqDistBigrams]
    #print(freqList)
    rankList = list(Ranking(freqList,start=1))
    #print(rankList)
    freDist_New = [tuple([x[0],y[0]]) for x,y in zip(freqDistBigrams,rankList)]
    #print(freDist_New)
    return freDist_New

    

    

def main():
    #bigramsRecommended()
    #bigramsNonRecommended()
    giveScoreToEachReview()

if __name__ == "__main__":
    main()

	
	

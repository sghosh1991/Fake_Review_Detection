import os
import json
import offlineFeatures
import onlineFeatures
import hashlib
import re
import datetime

#print(os.listdir())

totalReviews = 0
formatTimestamp = "%d%b%H%M%S"
timestamp = datetime.datetime.now()
pattern = r'[^ ]+'
path = r'C:\Python34\sampleData'
outputFile = open(r'C:\Python34\trainingDataOffline_' + timestamp.strftime(formatTimestamp) + '.txt','w')

to_write_header = "#reviewID,#businessID,Rating,#secondPronouns,#capitalWords,#excSentences,Length,EentityCount,SentimentScore,#reviewerFriend,reviewerReviewCount,Class(1-Spam/0-Genuine)\n"
outputFile.write(to_write_header)

dataFiles = [(x) for x in os.listdir(path) if os.path.isfile(path+"\\"+x)]

for p in dataFiles[0:len(dataFiles)]:

    print("Opening :" + p)

    try :
        
        with open(path+"\\"+p) as file:
            simpleJson = json.load(file)
            #print(str(type(simpleJson)))
            #print(str(type(simpleJson["nonReccomnded"])))

            for nonRecomendedReviewObject in simpleJson["nonReccomnded"]:
                
                
                #print(nonRecomendedReviewObject["ReviewComment"])
                reviewText = nonRecomendedReviewObject["ReviewComment"]

                #hash the text to create unique ID
                h = hashlib.md5(reviewText.encode('utf-8'))
                h1 = hashlib.md5(p.encode('utf-8'))

                #review features
                pronouns = offlineFeatures.getPersonalPronouns(reviewText)[0]
                rating = float(nonRecomendedReviewObject["Rating"])
                capitalWords = offlineFeatures.extractCapitalWords(reviewText)[1]
                excSentences = offlineFeatures.extractExclamationQuestionMarks(reviewText)[1]
                reviewLength = offlineFeatures.getReviewLength(reviewText)
                #online review features
##                entityCount = onlineFeatures.getEntity(reviewText)
##                review_sentimentScore = onlineFeatures.getSentiment(reviewText)

                #Dummy for preserving number of api calls to alchemy:
                entityCount = 1
                review_sentimentScore = 6.3

                #print("===Review features===")
                #print("Doc sentiment : " + str(review_sentimentScore) + " entity Count :" + str(entityCount) + " Capital Words: " + str(capitalWords)+ " Exc sentences :" + str(excSentences))
                

                #reviewer features
                #print("====Reviewer features====")
                
                reviewerFriendCount = int(re.findall(pattern,nonRecomendedReviewObject["friendCount"])[0])
                reviewerReviewCount = int(re.findall(pattern,nonRecomendedReviewObject["reviewCount"])[0])
                #print("Reviewer Friend Count : " + str(reviewerFriendCount))
                #print("Reviewer review count : " + str(reviewerReviewCount))
                totalReviews += 1

                to_write = h.hexdigest() + "," + h1.hexdigest() + "," + str(rating) + "," + str(pronouns) + "," + str(capitalWords) + "," + str(excSentences) + "," + str(reviewLength) + "," + str(entityCount) + "," + str(review_sentimentScore) + "," + str(reviewerFriendCount) + "," + str(reviewerReviewCount) + ",1" +"\n"
                #print(to_write)
                outputFile.writelines(to_write)



                #Recomended reviews

            for recomendedReviewObject in simpleJson["Reccomnded"]:
                
                   
                #print(recomendedReviewObject["ReviewComment"])
                reviewText = recomendedReviewObject["ReviewComment"]
                #hash the text to create unique ID
                h = hashlib.md5(reviewText.encode('utf-8'))
                h1 = hashlib.md5(p.encode('utf-8'))

                #review features
                pronouns = offlineFeatures.getPersonalPronouns(reviewText)[0]
                rating = float(recomendedReviewObject["Rating"])
                capitalWords = offlineFeatures.extractCapitalWords(reviewText)[1]
                excSentences = offlineFeatures.extractExclamationQuestionMarks(reviewText)[1]
                reviewLength = offlineFeatures.getReviewLength(reviewText)
                #online review features
##                entityCount = onlineFeatures.getEntity(reviewText)
##                review_sentimentScore = onlineFeatures.getSentiment(reviewText)

                #Dummy for preserving number of api calls to alchemy:
                entityCount = 1
                review_sentimentScore = 6.3

                #print("===Review features===")
                #print("Doc sentiment : " + str(review_sentimentScore) + " entity Count :" + str(entityCount) + " Capital Words: " + str(capitalWords)+ " Exc sentences :" + str(excSentences))
            

                #reviewer features
                #print("====Reviewer features====")
                
                reviewerFriendCount = int(re.findall(pattern,recomendedReviewObject["friendCount"])[0])
                reviewerReviewCount = int(re.findall(pattern,recomendedReviewObject["reviewCount"])[0])
                #print("Reviewer Friend Count : " + str(reviewerFriendCount))
                #print("Reviewer review count : " + str(reviewerReviewCount))
                totalReviews += 1

                to_write = h.hexdigest() + "," + h1.hexdigest() + "," + str(rating) + "," + str(pronouns) + "," + str(capitalWords) + "," + str(excSentences) + "," + str(reviewLength) + "," + str(entityCount) + "," + str(review_sentimentScore) + "," + str(reviewerFriendCount) + "," + str(reviewerReviewCount) + ",0" + "\n"
                outputFile.writelines(to_write)


    except UnicodeDecodeError as e:
        pass


print("Total Reviews Processed: " + str(totalReviews))            
outputFile.close()
	
	

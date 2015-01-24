import numpy as np
from sklearn.naive_bayes import GaussianNB
import configparser

config = configparser.ConfigParser()
config.read(r'C:\Python34\configFile.txt')

activeFeatureIndex = [int(config['FEATURES'][x]) for x in config['FEATURES']]


def trainNB():
    

    featureVector = []
    classVector = []
    temp= []
    headerLine = True


    #training
    train = open(r'C:\Python34\alchemyapi_python\TrainingDataDummy.csv')

    for line in train:
        if(headerLine):
            headerLine = False
        else:
            temp = line.split(",")
            x = [float(temp[i]) for i in activeFeatureIndex]
            #print(x)
            featureVector.append(x)
            #temp = [int(x) for x in line.split(",")[-1].rstrip("\n")]
            classVector.append(int(line.split(",")[-1].rstrip("\n")))

        
    fVector = np.array(featureVector)
    cVector = np.array(classVector)
    #print(classVector)
    print(fVector.shape)
    print(cVector.shape)

    clf = GaussianNB()
    clf.fit(fVector,cVector)
    train.close()

    return clf


def predictNB(clf):
    
    out = open(r'C:\Python34\alchemyapi_python\resultNB.txt','w')
    headerLine = True


    print("going to test")
    #print(activeFeatureIndex)

    #testing
    out.write("#reviewID;#businessID;Rating;#secondPronouns;#capitalWords;#excSentences;Length;EentityCount;SentimentScore;#reviewerFriend;reviewerReviewCount;Class\n")

    test = open(r'C:\Python34\alchemyapi_python\TestingDataDummy.csv')

    for line in test:

        if(headerLine):
            headerLine = False

        else:
            #print("-->" + line)
            tokens = line.split(",")
            #print(tokens)
            temp = [float(tokens[i]) for i in activeFeatureIndex]
            #print(x)
            #featureVector.append(temp)
            #print(str(type(clf.predict([temp]))))
            x = [temp]
            print(x)
            classPrediction = clf.predict(x)
        ##    print(type(classPrediction[0]))
        ##    print(classPrediction.shape)
        ##    print(classPrediction[0])
            out.write(str(tokens[0]) + ";" + str(tokens[1])+ ";" + str(tokens[2]) + ";" + str(tokens[3]) + ";" + str(tokens[4])+ ";" + str(tokens[5]) + ";" + str(tokens[6])+ ";" + str(tokens[7])+ ";" + str(tokens[8])+ ";" + str(tokens[9])+ ";" + str(tokens[10])+ ";" + str(classPrediction[0]) + "\n")


    out.close()
    test.close()



def predictNBKBest(clf,featureSelectorArray,outputFile):
    
    
    #out = open(r'C:\Python34\alchemyapi_python\resultNB.txt','w')
    headerLine = True


    print("going to test")
    print(featureSelectorArray)

    #testing
    outputFile.write("#reviewID;#businessID;Rating;#secondPronouns;#capitalWords;#excSentences;Length;EentityCount;SentimentScore;#reviewerFriend;reviewerReviewCount;Class\n")

    test = open(r'C:\Python34\alchemyapi_python\TestingData_New.csv')

    for line in test:

        if(headerLine):
            headerLine = False

        else:
            #print("-->" + line)
            tokens = line.split(",")
            #print(tokens)
            temp = [float(tokens[i+2]) for i,val in enumerate(featureSelectorArray) if val== True]
            #print(x)
            #featureVector.append(temp)
            #print(str(type(clf.predict([temp]))))
            x = [temp]
            #print(x)
            classPrediction = clf.predict(x)
        ##    print(type(classPrediction[0]))
        ##    print(classPrediction.shape)
        ##    print(classPrediction[0])
            outputFile.write(str(tokens[0]) + ";" + str(tokens[1])+ ";" + str(tokens[2]) + ";" + str(tokens[3]) + ";" + str(tokens[4])+ ";" + str(tokens[5]) + ";" + str(tokens[6])+ ";" + str(tokens[7])+ ";" + str(tokens[8])+ ";" + str(tokens[9])+ ";" + str(tokens[10])+ ";" + str(classPrediction[0]) + "\n")

    print("NB Classification Done")
    outputFile.close()
    test.close()
    return 0
    



def trainNBKBest(featureVector):
    clf = GaussianNB()
    clf.fit(featureVector,cVector)
    train.close()
    

def main():
    classifier = trainNB()
    
    predictNB(classifier)


    
if __name__ == "__main__":
    main()
    
    

    
    
    

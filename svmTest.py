from sklearn import svm
import numpy as np
import configparser

"""

==================================================
This module implements svm algorithm using sklearn package
======================================================
"""

def linearSVM(clf,featureSelectorArray,out):
    
       
    headerLine = True
    
    #Predicting
    test = open(r'C:\Python34\alchemyapi_python\TestingData_New.csv')
    out.write("reviewID;businessID;ClassPrediction\n")

    for line in test:

        if(headerLine):
            headerLine = False

        else:
            #print("-->" + line)
            tokens = line.split(",")
            #print(tokens)
            temp = [float(tokens[i+2]) for i,val in enumerate(featureSelectorArray) if val== True]
##            print(temp[0])
##            p=float(temp[0])
            #featureVector.append(temp)
            #print(str(type(clf.predict([temp]))))
            x = [temp]
            #print(x)
            classPrediction = clf.predict(x)
        ##    print(type(classPrediction[0]))
        ##    print(classPrediction.shape)
        ##    print(classPrediction[0])
            out.write(str(tokens[0]) + ";" + str(tokens[1])+ ";" + str(classPrediction[0]) + "\n")

    out.close()
    test.close()
    #train.close()
    print("SVM Classification Done")


if __name__ == "__main__":

    linearSVM()

    

    
    
    


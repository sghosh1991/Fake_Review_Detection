import json
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

   


def getEntity(text):

        try:
                response = alchemyapi.entities('text', text, {'sentiment': 1})
                count = 0
                if(response["status"] == 'OK'):
                        count = entityCount(response["entities"])
        except:
                pass
        return count


def getSentiment(text):

        try:
              response = alchemyapi.sentiment('text', text)
              sentimentScore = 0.0

              if(response["status"] == "OK"):
                      sentimentScore = scaleDocSentiment(response["docSentiment"])
        except:
                pass
        return sentimentScore
              

	
def getKeywords(text):
	
	response = alchemyapi.keywords('text', text, {'sentiment': 1})
	return response

def scaleDocSentiment(docSentiment):
        #print("sentiment")
        #print(str(type(docSentiment)))
        try:
                if(docSentiment["type"] =='positive'):
                        
                        return (3*float(docSentiment["score"])+7)

                elif(docSentiment["type"]=='negetive'):
                        
                        return (3*float(docSentiment["score"])+1)
                
                else:
                        return (float(docSentiment["score"])+5)
        except KeyError:
                return 0.0
	
def entityCount(entity):
        #print("entity")
        #print(entity)
        entities = [x for x in entity if x["type"] == "Company" or x["type"] == "Facility"]
        return len(entities)

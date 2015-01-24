import json
import re
import onlineFeatures
import ngram

def getReviewLength(reviewText):
	#This function returns the length of the review text
	
	return len(reviewText)


def getPersonalPronouns(reviewText):
	
	'''This function finds the number of personal pronounns like I,Me,myself,mine etc. in the review text'''
	
	#define patterns
	pattern_second_pronouns = r'\b(?:[Yy]our?|[uU])\b'
	pattern_first_pronouns = r'\b(?:[Ii]|[Mm][yYeE]|[Ww][eE]|[oO]ur|[Mm]ine|[uU][s])\b'
	
	
	match_second_pronouns = re.findall(pattern_second_pronouns,reviewText)
	match_first_pronouns = re.findall(pattern_first_pronouns,reviewText)
	
	#print(match_second_pronouns)
	#print(match_first_pronouns)
	
	#return a list l=[#secondPerPronoun,#firstPerPronoun]
	
	length = [len(match_second_pronouns),len(match_first_pronouns)]
	
	return (length)
	
	
def extarctAverageRating(reviewText):
		
		'''bleh'''
		
		#review_rating_pattern = r'"stars": [^,]+'
		#match_rating = re.findall(review_rating_pattern,reviewText)
		#print(match_rating)
		#rating = match_rating[0]
		#rating = rating[9:len(match_rating[0])]
		return reviewText["stars"]
		#print(rating)

def extractEntities(reviewText):
	
	'''This function takes the JSON resp (NOT the review text)of the alchemy getentity() and parses for Company entities'''
	
	response_entity = onlineFeatures.getEntity(reviewText)
	#print(str(type(response_entity["entities"])))
	x=[entity for entity in response_entity["entities"] if entity["type"]=="Company"]
	return (str(len(x)))
	
	
def extractCapitalWords(reviewText):
	
	pattern_capital=r'\b[A-Z]{2,}\b'
	pattern_words = r'\b[A-Za-z]+\b'
	
	
	match_capital=re.findall(pattern_capital,reviewText)
	match_words=re.findall(pattern_words,reviewText)
	
	#return a list L=[,#capital words,#words]
	
	return([len(match_words),len(match_capital)])
	


def extractExclamationQuestionMarks(reviewText):
	
	#define relevant patterns to match
	#ExcSentences --> the sentences that have ! ? in them
	
	pattern_sentence = re.compile(r'([\s]?[A-Za-z][^\.!?]*[\.!?])', re.M)
	pattern_ExcSentence = re.compile(r'([\s]?[A-Za-z][^\.!?]*[!?])', re.M)
	
	
	#Do matching
	
	
	match_sentences = re.findall(pattern_sentence,reviewText)
	match_ExcSentences = re.findall(pattern_ExcSentence,reviewText)
	
	
	#return a list L=[#sentence,#ExcSentence]
	
	return([len(match_sentences),len(match_ExcSentences)])
	
	

def main():
	for line in open("/home/santosh/dataMiningProject/alchemyapi_python/sampleReview.json"):
		my_data=json.loads(line)
		reviewText = my_data["text"]
		print(reviewText)
		#x=getPersonalPronouns(reviewText)
		#x=extarctAverageRating(my_data)
		#x=extractEntities(reviewText)
		#x=extractCapitalWords(reviewText)
		x=extractExclamationQuestionMarks(reviewText)
		print(x)

def BigramConstructor(reviewText):
        bigrams = ngram.getBigrams(reviewText)
        return bigrams

def nGramFreqDistGenerator(generateFreqDist_ngram):
        #print("\nIn Offline features make ngram tokens\n")
        return ngram.generateFreqDist(generateFreqDist_ngram)
        


if __name__=='__main__' :
	main()
	

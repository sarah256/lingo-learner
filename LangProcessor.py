import nltk
from TwitterClient import TwitterClient
from gensim.models.word2vec import Word2Vec
import gensim.downloader as api

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

class LangProcessor():
	'''
	Process through tweets
	'''
	def get_pos(self, query, tweets):
		'''
		Takes in list of tokenized tweets and finds the most
		commonly assigned part of speech to the slang word
		'''
		pos_dict = {}
		for tweet in tweets:
			if query in tweet:
				query_index = tweet.index(query)
				sent_pos = nltk.pos_tag(tweet)
				query_pos = sent_pos[query_index][1]
				if query_pos in pos_dict.keys():
					pos_dict[query_pos] += 1
				else:
					pos_dict[query_pos] = 1

		freq_key = ''
		freq_val = 0
		for key in pos_dict.keys():
			if pos_dict[key] > freq_val:
				pos_dict[key] = freq_val
				freq_key = key

		return freq_key

	def addtoCorpus(self, textfile, tweets):
		with open(textfile, "a") as file:
			for tweet in tweets:
				for word in tweet:
					file.write(word + ' ')
				file.write('\n')
			file.close()

	def build_model(self, corpus, query):
		model = Word2Vec(corpus)  # train a model from the corpus
		result = model.most_similar(query)
		# import pdb;pdb.set_trace()
		return result

	def generateDefinition(self, word, pos, synonyms):
		if "NN" in pos:
			return "A "+word+" is a "+synonyms[0]+", "+ synonyms[1]+", or "+synonyms[2]
		if "VB" in pos:
			return "To "+word+" is to "+synonyms[0]+", "+synonyms[1]+", or "+synonyms[2]
		if "JJ" in pos:
			return word + " means " + synonyms[0]+", "+synonyms[1]+", or "+synonyms[2]
		else:
			return synonyms[0]+", or "+synonyms[1]+", or "+synonyms[2]


def main():

	query = 'lit'
	# creating object of TwitterClient Class 
	api = TwitterClient() 
	# calling function to get tweets 
	tweets = api.get_tweets(query = query, count = 200) 

	langP = LangProcessor()
	pos = langP.get_pos(query, tweets)

	text = "corpus.txt"
	langP.addtoCorpus(text, tweets)
	list_of_lists = []
	with open("corpus.txt", "r") as f:
		for line in f:
			list_of_lists.append(line.split())
	model = langP.build_model(list_of_lists, query)
	similars = []
	similars.append(model[0][0])
	similars.append(model[1][0])
	similars.append(model[2][0])
	definition = langP.generateDefinition(query, pos, similars)
	print(definition)


if __name__ == "__main__": 
	# calling main function 
	main() 
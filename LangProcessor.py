import nltk
import TwitterClient
from gensim.models.word2vec import Word2Vec
import gensim.downloader as api

nltk.download('averaged_perceptron_tagger')


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
		return result


def main():

	query = 'lit'
	# creating object of TwitterClient Class 
	api = TwitterClient() 
	# calling function to get tweets 
	tweets = api.get_tweets(query = query, count = 200) 

	langP = LangProcessor()
	pos = langP.get_pos(query, tweets)

	text = "corpus.txt"
	newCorp = langP.addtoCorpus(text, tweets)
	model = langP.build_model



if __name__ == "__main__": 
	# calling main function 
	main() 
import nltk
from gensim.models.word2vec import Word2Vec
import gensim.downloader as api
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

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
					if word not in stop_words and not word.isdigit():
						file.write(word + ' ')
				file.write('\n')
			file.close()

	def build_model(self, corpus, query):
		model = Word2Vec(corpus)  # train a model from the corpus
		result = model.most_similar(query)
		# import pdb;pdb.set_trace()
		return result

	def generateDefinition(self, word, pos, synonyms):
		return word + ' relates to ' + synonyms[0] + ', '+ synonyms[1] + ', or ' + synonyms[2]


def main():
	return


if __name__ == "__main__": 
	# calling main function 
	main() 
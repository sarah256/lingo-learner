from flask import Flask, render_template, request, jsonify
from TwitterClient import TwitterClient
from LangProcessor import LangProcessor            
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/input", methods=["POST"])
def input_text():

	if request.method == "POST":
		print(request.form)
		data = request.form['submitText']
		print(data)
		query = data
		# creating object of TwitterClient Class 
		api = TwitterClient() 
		# calling function to get tweets 
		# for i in range(2):
		tweets = api.get_tweets(query = query, count = 100)

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
		# import pdb;pdb.set_trace()
		# return jsonify(isError=False,
		# 	message="Success",
		# 	statusCode=200,
		# 	stuff=data
		# 	), 200

	return render_template("define.html", definition=definition) 

if __name__ == "__main__":
    app.run(debug=True)
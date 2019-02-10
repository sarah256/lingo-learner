from flask import Flask, render_template, request, jsonify            
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
		# import pdb;pdb.set_trace()
		return jsonify(isError=False,
			message="Success",
			statusCode=200,
			data=[]
			), 200

	return 

if __name__ == "__main__":
    app.run(debug=True)
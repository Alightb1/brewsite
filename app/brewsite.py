from flask import Flask	
from flask import render_template 
import requests, json, warnings 
response = requests.get("https://api.openbrewerydb.org/v1/breweries")
beer_response = requests.get("https://api.sampleapis.com/beers/ale")

beer_data = json.loads(beer_response.content)
data = json.loads(response.content)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", user = "Anthony Lightbourn")

@app.route("/breweries")
def breweries():
	return render_template("breweries.html", content = data)

@app.route("/beer_types")
def beer_types():
	return render_template("beer_types.html", content = beer_data)


@app.route("/about")
def about():
	return render_template("about.html", user = "Anthony Lightbourn")





if __name__ == "__main__":
	app.run(debug=True)
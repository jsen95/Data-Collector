from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/success")
def success():
	return render_template("success.html")


if __name__ == '__main__':
	app.debug=True
	app.run()

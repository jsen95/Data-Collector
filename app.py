from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:justin0713@localhost/heightdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
	__tablename__="data"
	id=db.Column(db.Integer, primary_key=True)
	email_=db.Column(db.String(120), unique=True)
	height_=db.Column(db.Integer)

	def __init__(self, email_, height_):
		self.email_= email_
		self.height_= height_

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/success")
def success():
	return render_template("success.html")


if __name__ == '__main__':
	app.debug=True
	app.run()

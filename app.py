from flask import Flask,render_template,request

import os



app=Flask(__name__)


@app.route('/')
def hello():
			

	return render_template('home-page.html')


if __name__ == '__main__':
	app.run(debug=True)
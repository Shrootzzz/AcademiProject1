from flask import Flask

app = Flask(__name__)

@app.route('/')
def introduction():
	return"Calculate stuff using /operator/number1/number2"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2):
	output = number1+number2
	return '%d' % output

@app.route('/subtract/<int:number1>/<int:number2>')
def subtract(number1,number2):
	output = number1-number2
	return '%d' % output

@app.route('/multiply/<int:number1>/<int:number2>')
def multiply(number1,number2):

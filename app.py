from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html', name='William', school='Columbia College', place='New Zealand', nameList={'William': 175, 'Alina': 160, 'Amanda': 170, 'Bill': 180, 'William2': 174});

@app.route('/<inName>/<inSchool>/<inPlace>')
def personalised(inName):
	return render_template('me.html', name=inName, school=inSchool, place=inPlace, nameList={'William':175, 'Alina':160, 'Amanda':170, 'Bill':180, 'William2':174});

@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == "__main__":
	app.run()

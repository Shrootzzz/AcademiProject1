from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/experience')
def experience():
	return render_template('experience.html')

@app.route('/<inName>/<inSchool>/<inPlace>')
def personalised(inName):
	return render_template('me.html', name=inName, school=inSchool, place=inPlace, nameList={'William':175, 'Alina':160, 'Amanda':170, 'Bill':180, 'William2':174});

if __name__ == "__main__":
	app.run()

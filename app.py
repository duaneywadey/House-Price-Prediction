from flask import Flask, render_template, request
import joblib
import numpy as np


model = joblib.load('with_labels_house_price_ph')

app = Flask(__name__)
app.debug = True

# A must at all times
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def indexPage():
	
	# The form is here
    return render_template('index.html')

# Batangas	Bulacan	Cavite	Laguna	Manila	Pampanga	Quezon	Rizal
@app.route('/result' , methods=['POST', 'GET'])
def resultPage():
	a = request.form['a']
	b = request.form['b']
	c = request.form['c']
	d = int(request.form['d'])

	print(d)

	if d==1:
		arr = np.array([[a,b,c,1,0,0,0,0,0,0,0]], dtype=float)
		pred = model.predict(arr)
		predInt = int(pred)

	elif d==2:
		arr = np.array([[a,b,c,0,1,0,0,0,0,0,0]], dtype=float)
		pred = model.predict(arr)
		predInt = int(pred)

	elif d==3:
		arr = np.array([[a,b,c,0,0,1,0,0,0,0,0]], dtype=float)
		pred = model.predict(arr)
		predInt = int(pred)

	elif d==4:
		arr = np.array([[a,b,c,0,0,0,1,0,0,0,0]], dtype=float)
		pred = model.predict(arr)
		predInt = int(pred)

	elif d==5:
		arr = np.array([[a,b,c,0,0,0,0,1,0,0,0]], dtype=float)
		pred = model.predict(arr)
		predInt = int(pred)

	elif d==6:
		arr = np.array([[a,b,c,0,0,0,0,0,1,0,0]], dtype=float)
		pred = model.predict(arr)
		predInt = int(pred)

	elif d==7:
		arr = np.array([[a,b,c,0,0,0,0,0,0,1,0]], dtype=float)
		pred = model.predict(arr)
		predInt = int(pred)

	elif d==8:
		arr = np.array([[a,b,c,0,0,0,0,0,0,0,1]], dtype=float)
		pred = model.predict(arr)
		predInt = int(pred)

	else:
		arr = np.array([[a,b,c,0,0,0,0,0,0,0,0]], dtype=float)
		pred = model.predict(arr)
		predInt = int(pred)

	return render_template('result.html', data=predInt)



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request , jsonify
import pickle
from flask_cors import CORS,cross_origin
import sklearn


app = Flask(__name__)

@app.route('/',methods = ['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            pclass=float(request.form['pclass'])
            age = float(request.form['age'])
            sibSp = float(request.form['sibsp'])
            parch = float(request.form['parch'])
            fare = float(request.form['fare'])
            embarked = float(request.form['embarked'])
            sex = float(request.form['sex'])

            # NEW STUFFS
            filename = 'Decision_Tree_assignment1_final.sav'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[pclass,age,sibSp,parch,fare,embarked,sex]])
            print('prediction is', prediction)
            if prediction == [1]:
                res = 'Passanger has survived!'

            else:
                res = "Passanger has not survived!"

            # showing the prediction results in a UI
            return render_template('results.html',prediction = prediction,  res=res)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app
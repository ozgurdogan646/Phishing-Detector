from flask import Flask, request, render_template
from script.features import get_features
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('networkDeploy.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    path = "model/random_forest.joblib"
    prediction = get_predict(text, path)
    print(prediction)
    if prediction == 0:
        return render_template('result.html', p = True)
    else:
        return render_template('result.html', p = False)

def load_model(path):
    return joblib.load(path)

def get_predict(url, path):
    model = load_model(path)
    features = get_features(url)
    prediction = np.argmax(model.predict(features.reshape(-1,1)))
    return prediction
if __name__ == "__main__":
    app.run(debug=True)
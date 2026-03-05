from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs
        age = float(request.form['age'])
        gender = float(request.form['gender'])
        smoking = float(request.form['smoking'])
        exercise = float(request.form['exercise'])
        drinking = float(request.form['drinking'])
        bmi = float(request.form['bmi'])
        sleep = float(request.form['sleep'])
        junk = float(request.form['junk'])

        # Risk score calculation
        diabetes = hypertension = depression = 0

        if smoking == 1:
            diabetes += 20
            hypertension += 15
            depression += 10

        if bmi > 30:
            diabetes += 30
            hypertension += 25

        if sleep < 6:
            depression += 25

        if exercise == 0:
            diabetes += 10
            hypertension += 10

        if junk > 3:
            diabetes += 15
            hypertension += 10

        if age > 45:
            diabetes += 15
            hypertension += 20

        # Limit scores
        diabetes = min(diabetes, 100)
        hypertension = min(hypertension, 100)
        depression = min(depression, 100)

        return render_template("result.html",
                               diabetes=diabetes,
                               hypertension=hypertension,
                               depression=depression)

    except:
        return "Error in input values"


if __name__ == '__main__':
    app.run(debug=True)
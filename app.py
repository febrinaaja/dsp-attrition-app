from flask import Flask, render_template, request, redirect, url_for
from model.modeling import predict
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard')
def get_dashboard():
    return render_template('dashboard.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_view():
    if request.method == 'POST':

        form_data = request.form.to_dict()
        result = predict(form_data)

        return render_template('form_prediction.html', result=result)

    return render_template('form_prediction.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
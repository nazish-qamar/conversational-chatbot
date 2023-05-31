#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.pipeline.train_pipeline import TrainPipeline

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    if request.method == 'POST':
        # this is a generelized input class that can have multiple input fields
        user_data = CustomData(
            input=request.form.get('input')
        )

    message = user_data.get_data()
    predict_pipeline = PredictPipeline()
    response = predict_pipeline.predict(message)
    # user_input = request.form['input']
    # model = ModelTrainer()
    # response = model.infer(user_input)
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='train or predict')
    parser.add_argument("-c", '--choice', help='your choice, enter it')
    args = parser.parse_args()

    if args.choice == "train":
        print("You have chosen to train a new model. Please wait!!")
        training_obj = TrainPipeline()
        training_obj.call_train_workflow()
    elif args.choice == "predict":
        print("Predict app will start now!")
        print("Visit the URL 'http://localhost:5000/'")
        app.run(debug=True)
    else:
        print('Please pass "train" or "predict" argument')

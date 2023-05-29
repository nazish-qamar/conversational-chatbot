#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from src.components.model_trainer import ModelTrainer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    model = ModelTrainer()
    user_input = request.form['input']
    response = model.infer(user_input)
    return response


if __name__ == "__main__":
    app.run(debug=True)

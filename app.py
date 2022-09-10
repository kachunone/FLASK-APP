from flask import Flask, request
import numpy as np
import pandas as pd

app = Flask(__name__)

employee = pd.read_csv("EmployeeTeach.csv")
employee.head()

@app.route("/test")
def home():
    return "This is a test string"

@app.route("/search")
def search():
    answers = []
    answersFromUser = request.args.get('answers')
    print(answersFromUser)
    for i in range(len(answersFromUser)):
        answers.append(answersFromUser[i])
    return answers

if __name__ == '__main__':
    app.run()
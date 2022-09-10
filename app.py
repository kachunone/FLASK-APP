from flask import Flask, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

data = pd.read_csv('EmployeeTeach.csv')

skill_cats = ['algorithms','data_analytics','statistics','database_design','programming','communication','storytelling','time_management','neotiation','teamwork']

def recommender(input_array):
    skill_categories = data.columns[6:-1]
    sub_data = data[skill_categories].values
    cosine_simi = cosine_similarity(sub_data,input_array)
    cosine_simi = pd.DataFrame(cosine_simi,columns = ['value'])
    cosine_simi = cosine_simi.sort_values(by = 'value',ascending = False)
    recommendation = cosine_simi.head(5)
    return data[data.index.isin(recommendation.index)].to_json(orient='records')

@app.route("/test")
def home():
    return "you reached me!"

@app.route("/search")
def search():
    answers = []
    answersFromUser = request.args.get('answers')
    print(answersFromUser)
    for i in range(len(answersFromUser)):
        answers.append(int(answersFromUser[i]))
    return recommender([answers])

if __name__ == '__main__':
    app.run()
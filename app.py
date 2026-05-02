from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

app = Flask(__name__)

model_path = 'model/performance_model.pkl'
dataset_path = 'dataset/student_data.csv'

if not os.path.exists(model_path):
    df = pd.read_csv(dataset_path)
    X = df[['study_hours','attendance','previous_score']]
    y = df['final_score']
    model = LinearRegression()
    model.fit(X,y)
    os.makedirs('model', exist_ok=True)
    pickle.dump(model, open(model_path,'wb'))
else:
    model = pickle.load(open(model_path,'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    study = float(data.get('study',0))
    attendance = float(data.get('attendance',0))
    previous = float(data.get('previous',0))
    prediction = model.predict([[study,attendance,previous]])[0]
    return jsonify({'predicted_marks': round(prediction,2)})

if __name__ == '__main__':
    app.run(debug=True)

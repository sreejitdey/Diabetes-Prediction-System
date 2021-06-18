import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from flask import Flask, request, render_template

dataset = pd.read_csv('dataset/train_dataset.csv', index_col = 0)

x = dataset.iloc[:, : 16].values
y = dataset.iloc[:, 16].values

scaler = StandardScaler()
scaler.fit_transform(x)

model = tf.keras.models.load_model('model/project_model.h5')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET'])
def detect():
    BMI_LIMIT = 30;
    height = float(request.form.get("height"))
    weight = int(request.form.get("weight"))
    BMI = weight / (height * height)
    v16 = 0;
    if BMI >= BMI_LIMIT:
        v16 = 1
    else:
        v16 = 0
    v1 = int(request.form.get("v1"))
    v2 = int(request.form.get("v2"))
    v3 = int(request.form.get("v3"))
    v4 = int(request.form.get("v4"))
    v5 = int(request.form.get("v5"))
    v6 = int(request.form.get("v6"))
    v7 = int(request.form.get("v7"))
    v8 = int(request.form.get("v8"))
    v9 = int(request.form.get("v9"))
    v10 = int(request.form.get("v10"))
    v11 = int(request.form.get("v11"))
    v12 = int(request.form.get("v12"))
    v13 = int(request.form.get("v13"))
    v14 = int(request.form.get("v14"))
    v15 = int(request.form.get("v15"))
    x_test = np.array([v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16])
    y_pred = model.predict(scaler.transform([x_test]))
    if y_pred[0][0] <= 0.5:
        result = "Congratulations!! You are safe ✅"
    else:
        result = "⚠️ Warning!! You have chance of having diabetes"
    return render_template('result.html', OUTPUT = '{}'.format(result))

if __name__ == "__main__":
    app.run()

from flask import Flask,render_template,request,url_for
import pickle
import numpy as np

app=Flask(__name__)

model=pickle.load(open("modeldeploy.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    try:
        int_features=[int(i) for i in request.form.values()]
        final_features=[np.array(int_features)]
        prediction=model.predict(final_features)

        output=prediction[0]
    except Exception:
        return "please check if the values is correct or not"
        
    return render_template('predict.html',prediction_text="salary is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)

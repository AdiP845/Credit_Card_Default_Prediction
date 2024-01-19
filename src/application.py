from flask import Flask,request,render_template,jsonify
from prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            LIMIT_BAL=float(request.form.get('limit_bal')),
            SEX = float(request.form.get('sex')),
            EDUCATION = float(request.form.get('education')),
            MARRIAGE = float(request.form.get('marriage')),
            AGE = float(request.form.get('age')),
            PAY_1 = float(request.form.get('pay_1')),
            PAY_2 = float(request.form.get('pay_2')),
            PAY_3 = float(request.form.get('pay_3')),
            PAY_4 = float(request.form.get('pay_4')),
            PAY_5 = float(request.form.get('pay_5')),
            PAY_6 = float(request.form.get('pay_6')),
            BILL_AMT1 = float(request.form.get('bill_amt1')),
            BILL_AMT2 = float(request.form.get('bill_amt2')),
            BILL_AMT3 = float(request.form.get('bill_amt3')),
            BILL_AMT4 = float(request.form.get('bill_amt4')),
            BILL_AMT5 = float(request.form.get('bill_amt5')),
            BILL_AMT6 = float(request.form.get('bill_amt6')),
            PAY_AMT1 = float(request.form.get('pay_amt1')),
            PAY_AMT2 = float(request.form.get('pay_amt2')),
            PAY_AMT3 = float(request.form.get('pay_amt3')),
            PAY_AMT4 = float(request.form.get('pay_amt4')),
            PAY_AMT5 = float(request.form.get('pay_amt5')),
            PAY_AMT6 = float(request.form.get('pay_amt6'))
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)
        if results == 1:
            results = "Customer will default the payment next month"
        else:
            results = "Customer will not default the payment next month"    

        return render_template('form.html',final_result=results)
    

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
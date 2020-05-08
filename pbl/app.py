from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
app.secret_key = "MEET"


@app.route('/')
def page_Load():
    return render_template("home.html")


@app.route('/predict', methods=["POST"])
def predict():
    # if request.form["fn"] != "" and request.form["ln"] != "" and request.form["un"] != "" and request.form[
    #     "pwd"] != "":
    MinTemp = request.form["MinTemp"]
    MaxTemp = request.form["MaxTemp"]
    Rainfall = request.form["Rainfall"]
    WindGustSpeed = request.form["WindGustSpeed"]
    WindSpeed9am = request.form["WindSpeed9am"]
    WindSpeed3pm = request.form["WindSpeed3pm"]
    Humidity9am = request.form["Humidity9am"]
    Humidity3pm = request.form["Humidity3pm"]
    Pressure9am = request.form["Pressure9am"]
    Pressure3pm = request.form["Pressure3pm"]
    Cloud9am = request.form["Cloud9am"]
    Cloud3pm = request.form["Cloud3pm"]
    Temp9am = request.form["Temp9am"]
    Temp3pm = request.form["Temp3pm"]
    RainToday = request.form["RainToday"]
    RISK_MM = request.form["RISK_MM"]


    # load the model from disk
    filename = r'weather.sav'
    loaded_model = pickle.load(open(filename, 'r+b'))
    x_new = pd.DataFrame({'MinTemp': [MinTemp],
                          'MaxTemp': [MaxTemp],
                          'Rainfall': [Rainfall],
                          'WindGustSpeed': [WindGustSpeed],
                          'WindSpeed9am': [WindSpeed9am],
                          'WindSpeed3pm': [WindSpeed3pm],
                          'Humidity9am': [Humidity9am],
                          'Humidity3pm': [Humidity3pm],
                          'Pressure9am': [Pressure9am],
                          'Pressure3pm': [Pressure3pm],
                          'Cloud9am': [Cloud9am],
                          'Cloud3pm': [Cloud3pm],
                          'Temp9am': [Temp9am],
                          'Temp3pm': [Temp3pm],
                          'RainToday': [RainToday],
                          'RISK_MM': [RISK_MM]
                          })
    result = loaded_model.predict(x_new)
    print(x_new)

    return render_template('predict.html',
                           PRIDICTED=result)

    # return "<table><tr><td>Year </td><td>{} </td></tr><tr><td>Present Price</td> <td> {}</td></tr><tr><td>Kms Driven</td> <td> {} </td></tr><tr><td>Fuel Type </td> <td>{} </td></tr><tr><td>Seller Type </td><td> {}</td></tr><tr><td>Transmission </td><td> {}</td></tr><tr><td>Owner </td><td> {}</td></tr><tr><td>Predicted Selling Price </td><td> {}</td></tr></table>".format(
    #     Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, result)


if __name__ == '__main__':
    app.run(debug=True)

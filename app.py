# doing necessary imports
from flask import Flask, render_template, request, jsonify, Response, url_for, redirect
from flask_cors import CORS, cross_origin
import pandas as pd

from MaintenancePrediction import MaintenancePrediction
from logger_class import Logger
import Constants

app = Flask(__name__)  # initialising the flask app with the name 'app'
log = Logger("IndexPage")
mai = MaintenancePrediction()


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
    log.add_info_log(Constants.URL_HIT)
    return render_template('index.html')


@app.route('/profiling', methods=['POST', 'GET'])
@cross_origin()
def doProfiling():
    # pro = mai.do_profiling()
    log.add_info_log("Did Profiling")
    return render_template('Profilereport.html')


@app.route('/description', methods=['POST', 'GET'])
@cross_origin()
def description():
    return render_template('description.html')


@app.route('/prediction', methods=['POST', 'GET'])
@cross_origin()
def prediction():
    if request.method == 'POST':
        try:
            ptemp = request.form['ptemp'].replace(" ", "")
            rspeed = request.form['rspeed'].replace(" ", "")
            torque = request.form['torque'].replace(" ", "")
            toolwear = request.form['toolwear'].replace(" ", "")
            twf = request.form['twf'].replace(" ", "")
            hdf = request.form['hdf'].replace(" ", "")
            pwf = request.form['pwf'].replace(" ", "")
            osf = request.form['osf'].replace(" ", "")
            rnf = request.form['rnf'].replace(" ", "")

            data = {'Process temperature [K]': [ptemp],
                    'Rotational speed [rpm]': [rspeed],
                    'Torque [Nm]': [torque],
                    'Tool wear [min]': [toolwear],
                    'TWF': [twf],
                    'HDF': [hdf],
                    'PWF': [pwf],
                    'OSF': [osf],
                    'RNF': [rnf]
                    }
            res = mai.predict_air_temp(data)

        except Exception as e:
            log.add_exception_log(Constants.EXCEPTION_PREDICTION + " prediction()")
            return 'something is wrong'
    return '''<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h3> Predicted Air Temprature [K] :</h3> <h1> {}</h1>
</body>
</html>'''.format(res)


if __name__ == '__main__':
    app.run()

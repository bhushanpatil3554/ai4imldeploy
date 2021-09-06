import os

import pandas as pd
import numpy as np

import pickle

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import Constants
from logger_class import Logger

log = Logger("MaintenancePrediction")


class MaintenancePrediction:
    '''def do_profiling(self):
        """
        This function will do data Profiling which provides some Insights of data.
        :return:
        """
        try :
            pf = ProfileReport(self.load_data())
            nm = "report.html"
            pf.to_file("templates/report.html")
            return nm

        except Exception as e:
            log.add_exception_log(e)'''
    def load_data(self):
        try:
            data_file = open('static/ai4i2020.csv', 'r')
            df = pd.read_csv(data_file)
            return df
        except Exception as e:
            log.add_exception_log(e)
            return "Error"


    def predict_air_temp(self, data):
        try:
            data = pd.DataFrame(data)

            model = pickle.load(open('static/linear.pickle', 'rb'))
            pred = model.predict(data)
            print("Prediction ", pred)
            log.add_info_log("Prdicted value is {}".format(pred)  )
            return pred
        except Exception as e:
            log.add_exception_log(e)
            return pred


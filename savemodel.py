from model import predict, save_score_data, get_metrics, train_model
import os
import json
import pickle
import sys
#from flask import jsonify

#defining sample forecasts dictionary
#this is here simply so we can get some sample data when we call this endpoint
forecasts = [{ 'name': 'sample','length': 5}]

#define models (only one for now)
models = [{ 'id': 1, 'model_type': 'time series model with fbprophet'}]

# start the app!
if __name__ == '__main__':
    train_model(sys.argv[1], ['ds', 'y'])

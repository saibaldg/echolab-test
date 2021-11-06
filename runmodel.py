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

#retrieve models
def get_models():
    return json.dumps(models)

#define how to get created forecasts
def get_forecasts():
    return json.dumps(forecasts)

#define how to post forecasts
def create_forecast(data):
    # store forecast name and length for future reference
    forecasts.append(data)

     # load the model from disk
    loaded_model = pickle.load(open('model.sav', 'rb'))

    # create prediction of specified length (in weeks)
    #pred = predict(1, loaded_model)
    pred = predict(data["length"], loaded_model)

    print(pred.to_csv(index=False))
    # save forecast to file
    file_name = data['name']
    #pred.to_csv(file_name, index=False)
    pred.to_csv(r'./{}'.format(file_name), index=False)
    return '', 'Success'

#post actual data to create model score
def post_scores(data):
    #get name of forecast
    forecast_name = data['forecast_name']
    #save score data as csv
    save_score_data(data)
    #execute function that compares forecast data to actual
    get_metrics(forecast_name)

    return 'Success'

#retrieve list of reports available
def get_reports():
    #show list of all reports that can be generated
    ls_dir=os.listdir('/tmp/data/metrics')
    ls_files=[x.split('.')[0] for x in ls_dir if not x.startswith('.')]
    report_list = [x.split("metrics_")[1] for x in ls_files]

    return json.dumps(report_list)

#retrieve report by name
def get_report(name):
    #get list of all reports that can be created
    ls_dir=os.listdir('/tmp/data/metrics')
    ls_files=[x.split('.')[0] for x in ls_dir if not x.startswith('.')]
    report_list = [x.split("metrics_")[1] for x in ls_files]

    # Check if a name was provided as part of the URL.
    # If name is provided/exists in our list, generate visuals and return report.
    # If no name is provided, display an error in the browser.
    if name in report_list:
        return send_from_directory('/tmp/data/visuals/', '%s_graph.html' % name, as_attachment=True)
        #return "report is good"
    else:
        return "Error: No forecast name provided. Please specify one."

# start the app!
if __name__ == '__main__':
    #train_model('initial_data.csv', ['ds', 'y'])
    #print(get_models())  
    #currentDirectory = os.getcwd()
    #print(currentDirectory)
    #print(sys.argv[1]) 
    forecast = sys.argv[1] 
    data = {"name": "output.csv", "length": int(forecast)} 
    data1 = {"forecast_name": "twelve-week", "values": [{"date": "2018-10-05", "value":80},{"date": "2018-10-12", "value":90},{"date": "2018-10-19", "value":80},{"date": "2018-10-26", "value":70},{"date": "2018-11-02", "value":60},{"date": "2018-11-09", "value":50},{"date": "2018-11-16", "value":40},{"date": "2018-11-23", "value":30},{"date": "2018-11-30", "value":20},{"date": "2018-12-07", "value":10},{"date": "2018-12-14", "value":20},{"date": "2018-12-21", "value":30}]}
    create_forecast(data)
    #post_scores(data1)

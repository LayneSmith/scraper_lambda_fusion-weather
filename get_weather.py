# weather underground api key: db1844735e5c9433
# imports
from urllib.request import urlopen
import json
from io import StringIO

def get_weather_data():
    # get the forecast from this url
    forecast = urlopen('http://api.wunderground.com/api/db1844735e5c9433/forecast10day/q/TX/Plano.json')

    # read the results
    json_string = forecast.read()

    # parse to actual json object
    parsed_json = json.loads(json_string)

    forecast.close()

    # sample
    # location = parsed_json['location']['city']
    # temp_f = parsed_json['current_observation']['temp_f']
    # print "Current temperature in %s is: %s" % (location, temp_f)
    ten_day_forecast = parsed_json['forecast']['simpleforecast']['forecastday']

    # Save payload_array into StringIO() and output as text string
    si = StringIO()
    json.dump(ten_day_forecast, si)

    payload = si.getvalue()

    # print(payload)
    return payload

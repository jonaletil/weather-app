import configparser
from nose.tools import assert_true
import requests

# api key for weather api
config = configparser.ConfigParser()
config.read('api_keys.cfg')
api_key = config['OPENWEATHER']['API_KEY']

# url data
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q=Tuebingen&&units=metric&appid='
API = BASE_URL + api_key


def test_request_response():
    # Send a request to the API
    response = requests.get(API)

    # Confirm that the request completed
    assert_true(response.ok)

import configparser
import sys
import requests
from helpers import helper
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

# api key for weather api
config = configparser.ConfigParser()
config.read('api_keys.cfg')
api_key = config['OPENWEATHER']['API_KEY']

# url data
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q=Tuebingen&&units=metric&appid='
API = BASE_URL + api_key

# api call scheduler
scheduler = BlockingScheduler()


@scheduler.scheduled_job(IntervalTrigger(minutes=5))
def get_weather_data():
    """Gets weather data from API.

    This function makes an API request to a URL,
    stores data as an JSON object and calls write_to_db func.
    """

    result = requests.get(API)
    if result.status_code != 200:
        e = result.json()
        print('Error code: %s %s' % (e['cod'], e['message']))
        sys.exit()

    data = result.json()

    # Save data to database
    write_to_db(data)


def write_to_db(data):
    """Inserts data into database

    This function inserts data from API call into database.

    Args:
        data (dict): weather data dict
    """

    connection = helper.get_db_connection()
    cur = connection.cursor()

    description = data['weather'][0]['description']
    icon_code = data['weather'][0]['icon']
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']

    cur.execute('INSERT INTO tubingen_weather'
                ' (description,'
                'icon_code, temperature, feels_like, temp_min, temp_max, humidity, pressure, wind_speed, sunrise, '
                'sunset) '
                ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (description, icon_code, temperature, feels_like, temp_min, temp_max, humidity, pressure, wind_speed,
                 sunrise, sunset))

    connection.commit()
    connection.close()


if __name__ == '__main__':
    # makes first request
    get_weather_data()
    # schedules request task
    scheduler.start()

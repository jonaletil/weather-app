import numpy as np


class WeatherInfo:
    """Common base class for Weather"""

    def __init__(self, time, description, temp, feels_like, temp_min, temp_max, humidity, pressure, wind_speed):
        self.time = time
        self.description = description
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.humidity = humidity
        self.pressure = pressure
        self.wind_speed = wind_speed

    def display_current(self):
        print("Latest weather information for Tübingen at %s: \n"
              "Temperature: %s°C \n"
              "Feels like %s°C. %s. \n"
              "The high temp will be %s°C, the low temp will be %s°C. \n"
              "Humidity: %s%% \n"
              "Wind: %skm/h"
              % (self.time,
                 self.temp.astype(np.int64),
                 self.feels_like.astype(np.int64),
                 self.description.capitalize(),
                 self.temp_max.astype(np.int64),
                 self.temp_min.astype(np.int64),
                 self.humidity,
                 self.wind_speed.astype(np.int64)))

    def get_current(self):
        return [self.temp.astype(np.int64),
                self.feels_like.astype(np.int64),
                self.temp_min.astype(np.int64),
                self.temp_max.astype(np.int64),
                self.humidity.astype(np.int64),
                self.pressure.astype(np.int64)]

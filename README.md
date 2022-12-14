# CLI Weather App
Simple CLI weather App written in Python

## Project description
The task of the project was to build a command line app that displays the weather for the city of Tübingen.
It is also possible to compare the current weather with historical data.

The weather information are automatically queried regularly (every 5min) and a database is updated with it.
To fetch the weather data, OpenWeather API has been used.

The CLI App has the following functionalities:

- Command to query the latest data point:
  ```bash
  python app.py --latest
  ```
  OR
  ```bash
  python app.py -l
  ```
- Command to compare the current weather with an average of the last week (last 7 days), month and year 
  ```bash
  python app.py --compare
  ```
  OR
  ```bash
  python app.py -c
  ```
- Command to display the average temperature for a certain month of a certain year 
  ```bash
  python app.py --average 12 2000
  ```
  OR
  ```bash
  python app.py -a 12 2000
  ```
 
## Project files/folders: 
- db:
  - create_db.py: creates database and database table
  - schema.sql: contains table schema
- helpers:
  - helper.py: contains helper functions
- historic_data:
  - tubingen-historic-data.csv: contains Tübingen weather information from 1979 in csv format
- tests: contains unit test for API
- api_keys.cfg: contains OpenWeather API key
- app.py: contains function to handle user arguments and displaying weather information
- Dockerfile: contains the commands to assemble an docker image
- get_data.py: contains functions to read API data and saves these into database
- requirements.txt: contains required python libraries
- Weather.py: Weather class

 
## How to Run:
There are 2 ways how to set up and run the app:
##### Using git clone:
```
1. git clone https://github.com/jonaletil/weather-app.git
2. cd weather-app
3. docker build -t weather-app .
4. docker run -d --name weather-app weather-app
5. docker exec -it weather-app bash
6. python app.py --latest --compare --average 12 2000
```
##### or using DockerHub image:
```
1. docker pull jonaletil/weather-app:1.0
2. docker run -d --name weather-app jonaletil/weather-app:1.0
3. docker exec -it weather-app bash
4. python app.py --latest --compare --average 12 2000
```



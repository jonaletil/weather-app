# weather-app
Simple CLI weather app written in Python

## Project description
Task of the project was to build a command-line app that presents the weather for the city of Tübingen.
It is also possible to compare the current weather to historic data.

The weather information are automatically queried regularly and a database is updated with it.
To fetch the weather data, OpenWeather API has been used.

The CLI App has the following functionalities:

- Command to query the latest data point (*python app.py --latest*)
- Command to compare the current weather with an average of the last week (last 7 days), month and year (*python app.py --compare*)
- Command to display the average temperature for a certain month of a certain year (*python app.py --average*)
 
## Project files/folders: 
- db:
  - create_db.py: creates database and database table
  - schema.sql: contains table schema
- helpers:
  - helper.py: contains helper functions
- historic_data:
  - tubingen-historic-data.csv: contains Tübingen weather information from 1979 in csv format
- api_keys.cfg: contains OpenWeather API key
- app.py: contains function to handle user arguments and displaying weather information
- Dockerfile: contains the commands to assemble an docker image
- get_data.py: contains functions to read API data and saves these into database
- requirements.txt: contains required python libraries
- Weather.py: Weather class

 
## How to Run:
1. git clone https://github.com/jonaletil/weather-app.git
2. cd weather-app
3. docker build -t weather-app .
4. docker run -d --name weather-app weather-app
5. docker exec -it weather-app bash
6. python app.py --latest --compare --average 12 2000
or
- docker pull jonaletil/weather-app:1.0



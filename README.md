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
1. Add AWS IAM credentials in *dl.cfg* file
2. Specify output path in the *main* function of *etl.py* file 
3. run *etl.py* file

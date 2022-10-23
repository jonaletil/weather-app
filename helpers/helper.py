import pandas as pd
import sqlite3


def get_db_connection():
    """
    - Connects to database
    - Returns db connection
    """
    connection = sqlite3.connect('db/weather.db')

    return connection


def get_historic_data():
    """
    - Reads in data from csv into dataframe
    - Adds year and month columns to dataframe
    - Returns dataframe
    """
    df = pd.read_csv('historic_data/tubingen-historic-data.csv')

    df['day'] = pd.to_datetime(df['dt'], unit='s').dt.day
    df['year'] = pd.to_datetime(df['dt'], unit='s').dt.year
    df['month'] = pd.to_datetime(df['dt'], unit='s').dt.month

    return df


def handle_input_errors(err):
    """
    - Handles user arg errors
    - Prints error text
    """
    if err == 'month_error':
        print('Month must be in range 1-12')

    if err == 'year_error':
        print('Year must be in range 1979-2022')

    if err == 'no_data':
        print('No data find for selected period')

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

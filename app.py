import argparse
import calendar
import tabulate
import pandas as pd
import numpy as np
from datetime import datetime
from helpers import helper
from Weather import WeatherInfo


def read_user_cli_args():
    """Reads user arguments.

    Returns:
        parser
    """

    parser = argparse.ArgumentParser(
        description='Gets latest weather information for Tübingen. '
                    'Compares the current weather with an average of the last week (last 7 days), month and year. '
                    'Displays the average temperature for a certain month of a certain year. Data is limited to years '
                    'from 1979 until today '
    )

    parser.add_argument(
        '-l',
        '--latest',
        action='store_true',
        help='Gets last weather information for Tübingen.',
    )

    parser.add_argument(
        '-c',
        '--compare',
        action='store_true',
        help='Compares the current weather with an average of the last week (last 7 days), month and year.',
    )

    parser.add_argument(
        '-a',
        '--average',
        nargs=2,
        metavar=('1', '2021'),
        help='Displays the average temperature for a certain month of a certain year. Data is limited to years '
             'from 1979 until today',
    )

    return parser


def handle_user_args():
    """Handles user arguments."""

    user_args = read_user_cli_args().parse_args()

    if (not user_args.latest) & (not user_args.compare) & (not user_args.average):
        read_user_cli_args().print_help()

    if user_args.latest:
        display_current_weather()

    if user_args.compare:
        compare_weather()

    if user_args.average:
        handle_averages(user_args)


def query_last_data_point():
    """Query the latest data point.

    Returns:
        pandas dataframe
    """

    return pd.read_sql_query('SELECT *'
                             ' FROM tubingen_weather '
                             'ORDER BY ID DESC LIMIT 1',
                             helper.get_db_connection())


def get_current_weather():
    """Returns current weather information."""

    last_data_point = query_last_data_point()

    current_weather = WeatherInfo(
        datetime.strptime(last_data_point['created'][0], '%Y-%m-%d %H:%M:%S').time(),
        last_data_point['description'][0],
        last_data_point['temperature'][0],
        last_data_point['feels_like'][0],
        last_data_point['temp_min'][0],
        last_data_point['temp_max'][0],
        last_data_point['humidity'][0],
        last_data_point['pressure'][0],
        last_data_point['wind_speed'][0]
    )

    return current_weather


def display_current_weather():
    """Displays current weather information to the console."""

    print('=' * 20)
    WeatherInfo.display_current(get_current_weather())
    print('=' * 20)


def compare_weather():
    """ Outputs comparison between current weather with an average of the last week, month and year."""

    table_rows = ['Temperature (avg °C)', 'Feels/Felt Like (avg °C)', 'Temperature Min (min °C)',
                  'Temperature Max (max °C)', 'Humidity (avg %)', 'Pressure (avg hPa)']
    table_columns = ['Current', 'Last Week', 'Last Month', 'Last Year']

    # get historic data dataframe
    df = helper.get_historic_data()

    last_year = datetime.now().year - 1

    if datetime.now().month != 1:
        last_month = datetime.now().month - 1
    else:
        last_month = 12

    # get dataframes for last week, month and year
    last_week_df = df.iloc[-168:]
    last_month_df = df[(df.month == last_month) & (df.year == last_year)]
    last_year_df = df[df.year == last_year]

    # save averages to variables
    current_data = WeatherInfo.get_current(get_current_weather())
    last_week_data = get_average(last_week_df)
    last_month_data = get_average(last_month_df)
    last_year_data = get_average(last_year_df)

    # join all average data to dataframe
    df = pd.DataFrame(list(zip(current_data, last_week_data, last_month_data, last_year_data)),
                      index=table_rows, columns=table_columns)

    # print table to the console
    print('-' * 85)
    print('Comparison between current weather with an average of the last week, month and year.')
    print('-' * 85)
    print(tabulate.tabulate(df, tablefmt='simple_grid', headers=table_columns))


def get_average(df):
    """Returns averages.

    Args:
        df (df) : dataframe.
    """

    temp_avg = df.temp.mean().astype(np.int64)
    temp_feels_like = df.feels_like.mean().astype(np.int64)
    temp_min_avg = df.temp_max.min().astype(np.int64)
    temp_max_avg = df.temp_max.max().astype(np.int64)
    avg_humidity = df.humidity.mean().astype(np.int64)
    avg_pressure = df.pressure.mean().astype(np.int64)

    averages = [temp_avg, temp_feels_like, temp_min_avg, temp_max_avg, avg_humidity, avg_pressure]

    return averages


def handle_averages(user_args):
    """Handles average user arguments and input errors

    This function calculates average temperature for a certain month
     of a certain year and outputs it to console.

    Args:
        user_args (obj) : user arguments
    """
    month = int(user_args.average[0])
    year = int(user_args.average[1])

    if month not in range(1, 13):
        helper.handle_input_errors('month_error')
        return

    if year not in range(1979, 2023):
        helper.handle_input_errors('year_error')
        return

    if (year == 2022) and (month not in range(1, 11)):
        helper.handle_input_errors('no_data')
        return

    display_avg_temp(month, year)


def display_avg_temp(month, year):
    """Gets average temperature for a certain month of a certain year

    This function calculates average temperature for a certain month
     of a certain year and outputs it to console.

    Args:
        month (int) : Month number.
        year (int) : Year number.
    """
    # get historic data dataframe
    df = helper.get_historic_data()

    # filter for month and year
    df = df[(df.month == month) & (df.year == year)]

    # get average
    avg_temp = df.temp.mean().astype(np.int64)

    # print to console
    print('=' * 20)
    print('Average temperature for %s %s: %s°C'
          % (calendar.month_name[month], year, avg_temp))
    print('=' * 20)


if __name__ == '__main__':
    handle_user_args()

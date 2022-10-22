import sqlite3


def create_database():
    """
    - Creates the weather database
    - Creates the tubingen_weather table
    - Inserts information into the weather table
    """

    # Create database
    connection = sqlite3.connect('db/weather.db')

    # Create table
    try:
        with open('db/schema.sql') as f:
            connection.executescript(f.read())
    except Exception:
        print('file not found')

    # Commit and close connection
    connection.commit()
    connection.close()


if __name__ == '__main__':
    create_database()

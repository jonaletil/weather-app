DROP TABLE IF EXISTS tubingen_weather;

CREATE TABLE tubingen_weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR NOT NULL,
    icon_code VARCHAR,
    temperature FLOAT NOT NULL,
    feels_like FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    humidity INTEGER,
    pressure INTEGER,
    wind_speed FLOAT,
    sunrise TIMESTAMP,
    sunset TIMESTAMP
);

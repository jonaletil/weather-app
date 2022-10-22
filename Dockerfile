FROM python:3.8
LABEL maintainer="Josip Naletilic"

COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt

# create the database
RUN python db/create_db.py

# command to run on container start
ENTRYPOINT [ "python", "get_data.py" ]

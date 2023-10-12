# Data Pipeline
## Overview
This project is designed to be a simple implementation of a data pipeline. The idea is to have data from API, data file 
and database (MongoDB) sources extracted and uploaded into bucket storage (MinIO) and then transformed and loaded into a 
'data warehouse' (Postgres DB). The extracts will be performed regularly and orchestrated by Apache Airflow.
## How to run locally
- Clone the git repo `git clone git@bitbucket.org:RobBailiff/data-pipeline.git`
- Navigate to the root folder (`data-pipeline` by default)
- Start the project services with `docker-compose up`
- Listed below are the web links for the different containers:
  - Airflow: <http://localhost:8080>
  - Minio Endpoint: <http://localhost:9000>
  - Minio Console: <http://localhost:9001>
  - MongoDB Endpoint: <http://localhost:27017>
  - Mongo Express: <http://localhost:8081>
  - Postgres Endpoint: <http://localhost:5432>
  - Postgres Admin: <http://localhost:5050>
- Once the containers are running log into the admin apps with the following details:
  - Minio Console:
    - Username: `minio`
    - Password: `minio123`
  - Mongo Express:
    - Username: `admin`
    - Password: `admin123`
  - Postgres Admin:
    - Username: `pgadmin4@pgadmin.org`
    - Password: `admin`
- Install `python 3.8` and `poetry` dependency manager
- Install dependencies `poetry install`
- Run the script with `poetry run python src/main.py`
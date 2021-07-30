# Postgres Database
import psycopg2
from sqlalchemy import create_engine, engine, func, inspect

engine =psycopg2.connect(
    database = "postgres" , 
    user = "miranda",
    password = "password1",
    host = "music-kpop.cgfelcbkvk1j.us-east-2.rds.amazonaws.com",
    port = '5432')
#Import dependencies
import os
import pandas as pd
from flask import Flask, render_template, request, jsonify
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import psycopg2

#Import Postgress database connection
from config import engine

#Flask Setup
app = Flask(__name__)
                                                       
#Create route that renders index.html template
@app.route('/')
def index():
    return render_template('index.html')

#Query the database 
@app.route('/popularity')
def popularity():
    results = pd.read_sql("SELECT * FROM popular_songs WHERE popularity >'95'", con=engine)
    results_json=results.to_dict(orient="records")
    return jsonify(results_json)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
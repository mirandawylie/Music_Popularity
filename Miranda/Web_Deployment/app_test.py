#Import dependencies
import os
from flask import Flask, render_template, request

#Import Postgress database connection
from config import database

#Flask Setup
app = Flask(__name__)

#Database Setup
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = database

#Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Database object
db = SQLAlchemy(app)

engine=create_engine

#Create route that renders index.html template
@app.route('/')
def index():
    return render_template('index.html')

#Query the database 
@app.route('/popularity')
def popularity():
    results = db.session.query(popularity >=75).all()

if __name__ == '__main__':
    app.debug = True
    app.run()
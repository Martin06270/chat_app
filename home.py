from flask import Flask, render_template, url_for, request, redirect 
from kafka import KafkaConsumer
from kafka import KafkaProducer
import os
import time 
import json 
import pymongo

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route("/")
@app.route("/home")
@app.route("/inscription")
def home():
    return render_template("home.html")

@app.route("/inscription")
def inscription():
    return render_template("inscription.html") 

@app.route("/connexion")
def connexion():
    return render_template("connexion.html")

# ip: localhost (127.0.0.1) and port 5000

if __name__ == "__main__":
    app.run(debug=True,threaded=True)

# To run this file, use the command: python home.py
# To run the Flask app, make sure you have Flask installed in your environment.
# You can install Flask using pip: pip install Flask
# Make sure Kafka and MongoDB are running before starting this Flask app.




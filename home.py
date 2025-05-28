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
def home():
    return "Hi"

# ip: localhost (127.0.0.1) and port 5000

if __name__ == "__main__":
    app.run(debug=True,threaded=True)



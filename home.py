# Importation des modules nécessaires

from flask import Flask, render_template, url_for, request, redirect 
from kafka import KafkaConsumer
from kafka import KafkaProducer
import os
import time 
import json 
import pymongo

# Création de l'application Flask

app = Flask(__name__)
# Définition d'une clé secrète pour la gestion des sessions
app.secret_key = 'any random string'
# Définition des routes pour la page d'accueil et la page d'inscription
@app.route("/")
@app.route("/home")
@app.route("/inscription")
def home():
    return render_template("home.html")
# Route pour la page d'accueil avec un message de bienvenue
@app.route("/inscription", methods=['GET', 'POST'])

# Route pour la page d'inscription
def inscription():
    return render_template("inscription.html") 

@app.route("/inscription_check", methods=['GET', 'POST'])
def inscription_check():
    return render_template("inscription.html") 

@app.route("/connexion", methods=['GET', 'POST'])
def connexion():
    return render_template("connexion.html")

# ip: localhost (127.0.0.1) and port 5000
# Route pour la page de connexion
if __name__ == "__main__":
    app.run(debug=True,threaded=True)

# To run this file, use the command: python home.py
# To run the Flask app, make sure you have Flask installed in your environment.
# You can install Flask using pip: pip install Flask
# Make sure Kafka and MongoDB are running before starting this Flask app.




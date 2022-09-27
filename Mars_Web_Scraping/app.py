# 1. imports


from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo

from bs4 import BeautifulSoup as bs
import requests
import os



import pandas as pd


# Import function
import scrape_mars


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")



# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    mars_web_data = mongo.db.collection.find_one()

    return render_template("index.html", mars=mars_web_data)


# # Define what to do when a user hits the /scrape route

@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update_one({}, {"$set": mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)

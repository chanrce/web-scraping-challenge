from flask import Flask, render_template_redirect
from flask_pymongo import PyMongo
#Importing scrape_mars, where the function "scrape" is defined
import scrape_mars

app=Flask(__name__)

#root route
@app.route("/")




#scrape route

@app.route("/scrape")
def scrape():
    #Getting scraped data by calling the function "scrape" from scrape_mars.py
    scrape_mars.scrape

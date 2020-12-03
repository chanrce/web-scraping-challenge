from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#Importing scrape_mars, where the function "scrape" is defined
import scrape_mars

app=Flask(__name__)

#Setup Mongo connection using PyMongo
mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_app")


#root route
@app.route("/")




#scrape route
@app.route("/scrape")
def scrape():
    #Getting scraped data by calling the function "scrape_web" from scrape_mars.py
    m_data = scrape_mars.scrape_web()

    #Storing value in Mongo as a Python dict
    mongo.db.collection.update({}, m_data, upsert=True)

    #Redirect back to home page
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)

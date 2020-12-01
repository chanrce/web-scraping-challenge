from flask import Flask

app=Flask(__name__)

#root route
@app.route("/"):




#scrape route

@app.route("/scrape")
def scrape():
    #importing scrape_mars python file
    import scrape_mars.py
    
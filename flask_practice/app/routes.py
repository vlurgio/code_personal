from app import app
from pandas import read_csv


@app.route("/")
@app.route("/index")
def index():
    return str(read_csv("targeted_sentiment_gpe_News.csv"))
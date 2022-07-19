from flask import Flask
from requests import get
from json import loads

app = Flask(__name__)

@app.route("/cat")
def get_fact():
    return fetch_fact()

def fetch_fact():
    res = get("https://catfact.ninja/fact")
    fact = loads(res.text)['fact']
    return fact
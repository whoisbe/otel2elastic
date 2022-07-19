from opentelemetry import trace # OpenTelemetry imports
from flask import Flask
from requests import get
from json import loads

tracer = trace.get_tracer(__name__) # Acquire a tracer
app = Flask(__name__)

@app.route("/cat")
def get_fact():
    return fetch_fact()

def fetch_fact():
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("fetch_fact") as apispan:
        res = get("https://catfact.ninja/fact")
        fact = loads(res.text)['fact']
        apispan.set_attribute("fact.value", fact)
        return fact
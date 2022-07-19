# Instrument a Flask application to send traces to OpenTelemetry collector

 1. We are now ready to instrument a small python application using OpenTelemetry to get traces and send it to the collector.
 2. Change into the `Code` directory. Open the file `app.py` using your favorite code editor and examine the code.
 3. This app makes an external api call to obtain some data and returns part of the data. 
 4. As of now, there's no instrumentation in this code. You will need to install some libraries that's required to instrument this code.
 5. First, let's create a Python environment by running the following inside the Code directory

```bash
cd Code
python3 -m venv .
source ./bin/activate
pip install --upgrade pip
```
 6. Let's then install Flask, Requests and OpenTelemetry by running the following

```bash
pip install flask
pip install requests
pip install opentelemetry-distro
pip install opentelemetry-exporter-otlp
```
 7. Let's now open `app.py` back up and instrument it to get tracing telemetry. Modify the code as seen below to initialize a tracer and use 

```python
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
```
8. Use the `opentelemetry-bootstrap` command to automatically detect supported libraries and install associated instrumentation.

```bash
opentelemetry-bootstrap -a install
```
 9. Finally you can use `opentelemetry-instrument` to run the flask application along with instrumentation to get traces.

```bash
opentelemetry-instrument --metrics_exporter none flask run
```

 10. Now access http://127.0.0.1:5000/cat in your browser and refresh a few times to learn about some random cat facts and also send some traces to Elastic Observability.
 11. Get back to your Elastic deployment and navigate to Observability > APM > Traces app using the side navigation.
 12.  You should be able to see traces corresponding to the number of times you accessed the /cat endpoint.
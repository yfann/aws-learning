from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo

from jaeger_client import Config
from flask_opentracing import FlaskTracer
from opentracing import tracer
# from prometheus_client import Counter, Histogram
from prometheus_flask_exporter import PrometheusMetrics
# import time
import logging

app = Flask(__name__)
metrics = PrometheusMetrics(app)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)

# FLASK_REQUEST_LATENCY = Histogram('flask_request_latency_seconds', 'Flask Request Latency',
#                 ['app','method', 'endpoint'])
# FLASK_REQUEST_COUNT = Counter('flask_request_count', 'Flask Request Count',
#                 ['app','method', 'endpoint', 'http_status'])
# FLASK_REQUEST_FAIL_COUNT = Counter('flask_request_fail_count', 'Flask Request Fail Count',
#                 ['app','method', 'endpoint', 'http_status'])

# @app.before_request
# def before_request():
#     request.start_time = time.time()

# @app.after_request
# def after_request(response):
#     request_latency = time.time() - request.start_time
#     FLASK_REQUEST_LATENCY.labels("test",request.method, request.path).observe(request_latency) 
#     if response.status_code == 200:
#         FLASK_REQUEST_COUNT.labels("test",request.method, request.path, response.status_code).inc()
#     else:
#         FLASK_REQUEST_FAIL_COUNT.labels("test",request.method, request.path, response.status_code).inc()
#     return response



@app.route("/")
def homepage():
    return "Hello World"


@app.route("/api")
def my_api():
    answer = "something"
    with tracer.start_span("api") as span:
        span.set_tag("api", answer)
    return jsonify(repsonse=answer)


@app.route("/api2")
def my_api2():
    answer = "api2"
    # parent_span = tracer.get_span()
    test = request.args.get('test')
    with tracer.start_span("api2") as span:
        span.set_tag("api2", answer)
        if test is None:
            logging.info("test parameter is None")
            span.set_tag("error", True)
            span.set_tag("description", "test parameter is None")
        else:
            span.set_tag("test",test)
        
    return jsonify(repsonse=answer)


@app.route("/error")
def error():
    logging.info("500 error happens")
    with tracer.start_span("error") as span:
        span.set_tag("error", True)
        span.set_tag("description", "500 error happens")
    return "server error", 500


@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})




def initialize_trace(service):
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)

    config = Config(
        config={"sampler": {"type": "const", "param": 1,}, "logging": True,},
        service_name="service",
    )

    return config.initialize_tracer()  # also sets opentracing.tracer


# starter code
tracer = initialize_trace("test-svc")

# flask_tracer = FlaskTracer(initialize_trace, True, app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


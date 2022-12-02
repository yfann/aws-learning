**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

![Alt text](./answer-img/all-components.png)

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

![Alt text](./answer-img/grafana-homepage.png)

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![Alt text](./answer-img/basic-dashboard.png)

![Alt text](./answer-img/grafana_datasource.png)

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

+ Latency:  the average response latency in a month
+ Throughput:  the average request per minute in a month
+ error rate: error response(status code:5xx)/all response * 100% in a month 

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

+ error per second
+ average response time
+ requests per second
+ request duration
+ total requests per minute

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![Alt text](./answer-img/dashboard-for-CLI.png)

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

![Alt text](./answer-img/tracing1.png)

![Alt text](./answer-img/Tracing-our-Flask-App.png)


## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

![Alt text](./answer-img/jaeger-in-Dashboards.png)

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:  500 error code

Date: 11/28/2022

Subject: 500 error code

Affected Area: backend service

Severity: 2

Description:  response get 500 error code on /api2


![Alt text](./answer-img/tracing1.png)


![Alt text](./answer-img/tracing2.png)

## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

SLI:
+ avarage Latency/30d
+ availability/30d
+ avarage Response time/30d


## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

+ requests above 500ms
    + to measure the latency of requests

+ error rate
    + to measure the availability


## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  


![Alt text](./answer-img/final-dashboard.png)
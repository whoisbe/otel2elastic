# Overview

Our goal is to learn how to send OpenTelemetry data to Elastic Observability for analysis. We will do that using a hands-on approach of setting up the following data pipeline and learn about relevant concepts, required installations, configurations and options along the way. The pipeline consists of a simple Flask web application that will run in your host machine. The code will require instrumentation to export spans via OTLP. This data will be be sent to a local OpenTelemetry collector which will also require seting up in the same host as a container using a docker image. The collector should be configured to export the telemetry data to the final destination for analysis which is an Elastic observability deployment. 

![data pipeline](pipeline.svg)

In this guide, you will set up the pipeline in the following sequence.

 1. [Set up an Elastic deployment](deploy.md) that will serve as the final destination for telemetry data
 2. [Set up OpenTelemetry collector](collect.md) and configure it to export telemetry data to Elastic APM server
 3. [Instrument a Flask application](instrument.md) to send traces to the OpenTelemetry collector


[Previous](../README.md) \| [Next](deploy.md)
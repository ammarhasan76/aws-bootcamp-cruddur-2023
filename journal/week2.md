# Week 2 — Distributed Tracing

04/03/2023  
Watched Week 2 Live-Stream Video (Distributed Tracing)  
https://www.youtube.com/watch?v=2GD9xCzRId4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=30  
Study Notes:

## Introdcution


*"For code there is a debugger, for everything else there is observability"*

Old world: logging   
New world: distributed tracing (example frontend + backend)

![image](https://user-images.githubusercontent.com/22940535/222910581-400fc3bb-fb6f-4bd1-bde6-de84dd1cd5b0.png)

![image](https://user-images.githubusercontent.com/22940535/222910922-69964c0d-d3e0-462a-b435-bac00cfb8d37.png)

A span = a single unit of work in a request/trace

Can spot error/failures and/or which part of a request is slow

Instrumentation = code/software/service that performs the tracing/observability

## HoneyComb

### Setup API Key environement variable in Workspace

*note: OTEL = opentelemetry"

Action:
In UI, create a new 'bootcamp' env

*note: standard env vars naming for the API key is: honeycomb_api_key*  
`export HONEYCOMB_API_KEY="8Or1b0hpzLK7wCrUJW4wsB"`

*note: export means that env var is available in all the shells for that host

*note gp env is to add something to the gitpod.yml file so it doesn't need to keep getting defined every time you start a new Workspace*  
`gp env HONEYCOMB_API_KEY="<removed>"`

*note: gp env stores the variable in Variables in https://gitpod.io/user/variables*

### Add refences to environment variables in applicaation code

Action: (add OTEL_SERVICE_NAME to docker compose yml, you need a different service name for each service in your solution, so far we are adding to the backend-flask container)
`OTEL_SERVICE_NAME: "backend-flask"`  
`OTEL_EXPORTER_OTLP_ENDPOINT: "https://api.honeycomb.io"`  
`OTEL_EXPORTER_OTLP_HEADERS: "x-honeycomb-team=${HONEYCOMB_API_KEY}"`

### Setup configuration to end data to 'bootcamp' environement in Honeycomb

#### Install Packages

Action: (install python packages required to instrument and export telemetry to honeycomb to requirements.txt in ./backend-flask)  
```opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests```


Action: (install python dependencies)  
```cd ./backend-flask```
```pip install -r requirements.txt```


#### Initialise Packages
Action: (add packages to app.py and initialise objects)  


```/# Honeycomb - OTEL
/# Packages
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor```


```/# Honeycomb - OTEL
/# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)```


```/# Honeycomb - OTEL
/# Initialize automatic instrumentation with Flask
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()```

*note: reference: (https://docs.honeycomb.io/getting-data-in/opentelemetry/python/)*

Action: (npm install - due to in dev container we mapped the local volume so it's missing from the container build???)  
`cd ../frontend-react-js/'
`npm i`

*Note to self to look into: From livestream chatIuliana Silvasan: I've added 'npm install' via ENTRYPOINT script*

Action:  
*edited app.py for the span processors*

Action:
*ran docker compose up*
*checked honeycomb for data successfully*











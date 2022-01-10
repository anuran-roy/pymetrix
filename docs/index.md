<!-- # Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files. -->

# Pymetrix-Python

[![Docs](https://img.shields.io/website?color=whi&down_color=red&down_message=Offline&label=Docs&logo=readthedocs&logoColor=white&style=for-the-badge&up_color=green&up_message=Online&url=https%3A%2F%2Fanuran-roy.github.io%2Ftags%2Fpymetrix%2F)](https://anuran-roy.github.io/tags/pymetrix/)
## What is Pymetrix?

**Pymetrix** (previously known as **Analyx**) is a plug-and-play analytics library written in Python.

## How to use it

Pymetrix is really easy to integrate with your projects. Here's an example:

Let's say you want to monitor a method ``foo()`` defined as:

```python
from random import randint

def foo():
    print(f"Hello world {randint(0,1000000)}!")
```

After adding the required lines, the code will look something like this:

```python
from random import randint
from pymetrix.metrics import Metrics

metricman = Metrics(loc=__file__)
foo_obj = None

def foo():
    print(f"Hello world {randint(0,1000000)}!")
    if foo_obj is None:
        ep1 = endpoints.Endpoint(endpoint="/", id=foo)
        foo_obj = flow.FlowNode(ep1, name="Object1")

    metricman.add_to_analytics(foo_obj, layerName="foo")
```


## Using with various Web Frameworks

Pymetrix can be used in conjunction with other frameworks as well, including web frameworks. The following examples will illustrate it more clearly.

### 1. Using with Django

**[Django](https://www.djangoproject.com/)** is the most popular framework of choice for a vast majority of Python web developers, often dubbed as "the framework for perfectionists with deadlines". It is a clean, concise and opinionated framework that enforces code reusability, modularity and code readability. It has an intuitive directory structure, and a large ecosystem of plugins tailor-made for it. Besides those, the usual Python libraries that can be used in tandem with it for designing business logic as well.

Being a library, you can import Pymetrix on any file that will be executed by the server on calling the endpoints. This is usually the ``views.py`` file in a standard Django project.

A sample ``views.py`` in Django with Pymetrix (Tested on Django 4.0.0):

```python
from django.shortcuts import render, HttpResponse
from django.http import StreamingHttpResponse

from typing import Dict, List, Any, Tuple, NewType

from pymetrix import metrics, endpoints, flow
import pymetrix.visualize as vs

# Create your views here.


metricman = metrics.Metrics(loc="Test")  # Initialize the Pymetrix Metrics object


def blog(request):
    # Other code
    ...
    node2: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/blog", id=blog), name="Blog"
    )
    metricman.add_to_analytics(
        node2
    )  # Add the function to the graph corresponding to the metricman object

    # any return stuff
    return HttpResponse("<h1>Blog works!</h1>")


def about(request):
    # Other code
    ...
    node3: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/about", id=about), name="About"
    )
    metricman.add_to_analytics(
        node3
    )  # Add the function to the graph corresponding to the metricman object

    # any return stuff
    return HttpResponse("<h1>About works!</h1>")


def contact(request):
    # Other code
    ...
    node4: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/contact", id=contact), name="Contact"
    )
    metricman.add_to_analytics(
        node4
    )  # Add the function to the graph corresponding to the metricman object

    # any return stuff
    return HttpResponse("<h1>Contact works!</h1>")


def collaborations(request):
    # Other code
    ...
    node6: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/collaborations", id=collaborations),
        name="Collaborations",
    )
    metricman.add_to_analytics(
        node6
    )  # Add the function to the graph corresponding to the metricman object

    # any return stuff
    return HttpResponse("<h1>Collaborations works!</h1>")


def events(request):
    # Other code
    ...
    node5: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/events", id=events), name="Events"
    )
    metricman.add_to_analytics(
        node5
    )  # Add the function to the graph corresponding to the metricman object

    # any return stuff
    return HttpResponse("<h1>Events works!</h1>")


def home(request):
    node1: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/home1", id=home), name="Home"
    )
    metricman.add_to_analytics(
        node1
    )  # Add the function to the graph corresponding to the metricman object

    return HttpResponse("<h1>Home works!</h1>")


# The methods below won't be added for metrics


def someMethod(request):
    ...


class someClass:
    ...


def anotherMethod(request):
    ...


def aThirdMethod(request):
    ...

```

Although I haven't tested it yet, owing to the nature of the ``metricman`` object, I think it can be used in the top level ``urls.py`` for being used over the entire project - one that has multiple Django Apps into it.

Also, do check out **[Pymetrix Django Dashboard](https://github.com/anuran-roy/pymetrix-dashboard-django.git)**

### 2. Using with FastAPI

**[FastAPI](https://fastapi.tiangolo.com/)** is a micro web framework built on top of Pydantic and Starlette. It claims to be the fastest Pythonic web framework out there for building APIs, and adheres to the OpenAPI standards. It provides two UIs for testing the APIs made through it - Redoc and SwaggerUI. It also provides a lot of functionalities out of the box, such as asynchronous calls, which speeds up API calls, sometimes tremendously. It can be used both with ASGI and WSGI.

Integrating Pymetrix with FastAPI is as easy as it is in Django, if not easier.

```python
from fastapi import FastAPI, status
from pymetrix import metrics, endpoints, flow
from fastapi.responses import ORJSONResponse

app = FastAPI()


metricman = metrics.Metrics(loc="Test")


@app.get("/home", status_code=status.HTTP_200_OK, response_class=ORJSONResponse)
async def home():
    node1: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/home", id=home), name="Home"
    )
    metricman.add_to_analytics(node1)

    return {"response": status.HTTP_200_OK, "message": "This is the home page"}


@app.get("/contact", status_code=status.HTTP_200_OK, response_class=ORJSONResponse)
async def contact():
    node2: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/contact", id=contact), name="Contact"
    )
    metricman.add_to_analytics(node2)

    return {"response": status.HTTP_200_OK, "message": "This is the contact page"}


@app.get("/collaborations", status_code=status.HTTP_200_OK, response_class=ORJSONResponse)
async def collaborations():
    node3: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/collaborations", id=collaborations),
        name="Collaborations",
    )
    metricman.add_to_analytics(node3)

    return {
        "response": status.HTTP_200_OK,
        "message": "This is the collaborations page",
    }


@app.get("/events", status_code=status.HTTP_200_OK, response_class=ORJSONResponse)
async def events():
    node4: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/events", id=events), name="Events"
    )
    metricman.add_to_analytics(node4)

    return {"response": status.HTTP_200_OK, "message": "This is the events page"}


@app.get("/blog", status_code=status.HTTP_200_OK, response_class=ORJSONResponse)
async def blog():
    node5: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/blog", id=blog), name="Blog"
    )
    metricman.add_to_analytics(node5)

    return {"response": status.HTTP_200_OK, "message": "This is the blog page"}


@app.get("/about", status_code=status.HTTP_200_OK, response_class=ORJSONResponse)
async def about():
    node6: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/about", id=about), name="About"
    )
    metricman.add_to_analytics(node6)

    return {"response": status.HTTP_200_OK, "message": "This is the about page"}


@app.get("/statistics", status_code=status.HTTP_200_OK, response_class=ORJSONResponse)
async def get_statistics():
    return {"response": status.HTTP_200_OK, "message": metricman.aggregate()}

```

Now we start the ``uvicorn`` server using:

```sh
uvicorn main:app --port 8000 --reload
```

Now going to ``localhost:8000/statistics`` will give you the aggregate hits on each endpoint.

Also, here we are serializing the data [using orjson, instead of regular JSON](#orjson-note)

Just like the case with Django, you can initialize a Pymetrix object in the main.py file and then import into other scripts from there, if you want a centralized view. But you're also free to take a modular approach with your project by initializing the Pymetrix objects within each module - your skills are your limit.

### 3. Using with Starlite

**[Starlite](https://goldziher.github.io/starlite/)** is the new challenger in town for Web API frameworks. It's similar to FastAPI in the aspect that it's based on Starlette and Pydantic. But it has a fundamental philosophical difference - Starlite is opinionated, while FastAPI is not. 

According to the maker of Starlite, Na'aman Hirschfeld (who is also an online friend of mine 😎):

> The intention behind Starlite was to create a higher level opinionated API framework. I placed opinionated in bold because in my view, being opinionated regarding how certain things should be done and shouldn’t be done, and establishing best practices, is one of the most important things a framework can do.

So let's see how Pymetrix works with Starlite:

```python
from starlite import Starlite, get
from pymetrix import metrics, endpoints, flow
from typing import Dict

metricman = metrics.Metrics(loc="Test")


@get(path="/home")
def home() -> Dict:
    node1: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/home", id=home), name="Home"
    )
    metricman.add_to_analytics(node1)
    return {"response": 200, "message": "Home Page Works"}


@get(path="/contact")
def contact() -> Dict:
    node2: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/contact", id=contact), name="Contact"
    )
    metricman.add_to_analytics(node2)
    return {"response": 200, "message": "Contact Page Works"}


@get(path="/collaborations")
def collaborations() -> Dict:
    node3: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/collaborations", id=collaborations),
        name="Collaborations",
    )
    metricman.add_to_analytics(node3)
    return {"response": 200, "message": "Collaborations Page Works"}


@get(path="/events")
def events() -> Dict:
    node4: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/events", id=events), name="Events"
    )
    metricman.add_to_analytics(node4)
    return {"response": 200, "message": "Events Page Works"}


@get(path="/blog")
def blog() -> Dict:
    node5: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/blog", id=blog), name="Blog"
    )
    metricman.add_to_analytics(node5)
    return {"response": 200, "message": "Blog Page Works"}


@get(path="/about")
def about() -> Dict:
    node6: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/about", id=about), name="About"
    )
    metricman.add_to_analytics(node6)
    return {"response": 200, "message": "About Page Works"}


@get(path="/statistics")
def statistics() -> Dict:
    node2: flow.FlowNodeType = flow.FlowNode(
        endpoints.Endpoint(endpoint="/contact", id=contact), name="Contact"
    )
    metricman.add_to_analytics(node2)
    return {"response": 200, "message": metricman.time_series()}


app = Starlite(
    route_handlers=[home, contact, collaborations, events, blog, about, statistics]
)
```

Do note that Starlite uses the orjson library for its responses by default.

#### Orjson Note
In **[orjson](https://pypi.org/project/orjson/)**, the response is a JSON byte string and not a object. This dramatically speeds up the serialization process.
<!-- For looking into what more Pymetrix can do, head to ``tests/flow_test.py``. -->
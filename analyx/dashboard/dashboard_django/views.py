from django.shortcuts import render, HttpResponse

from typing import Dict, List, Any, Tuple, NewType
from . import models

import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go
import networkx as nx
from pyvis.network import Network
import json

from analyx import metrics, endpoints, flow
import analyx.visualize as vs
# Create your views here.


metricman = metrics.Metrics(loc="Test")


def foo1():
    print("Bar")


def foo2():
    print("Bar2")


def foo3():
    print("Bar3")


def foo4():
    print("Bar4")


def foo5():
    print("Bar5")


def foo6():
    print("Bar6")


def blog(request):
    # Other code

    node2 = flow.FlowNode(endpoints.Endpoint(endpoint="/blog", id=blog), name="Blog")
    metricman.add_to_analytics(node2)

    # any return stuff
    return HttpResponse("<h1>Blog works!</h1>")


def about(request):
    # Other code

    node3 = flow.FlowNode(endpoints.Endpoint(endpoint="/about", id=about), name="About")
    metricman.add_to_analytics(node3)

    # any return stuff
    return HttpResponse("<h1>About works!</h1>")


def contact(request):
    # Other code

    node4 = flow.FlowNode(endpoints.Endpoint(endpoint="/contact", id=contact), name="Contact")
    metricman.add_to_analytics(node4)

    # any return stuff
    return HttpResponse("<h1>Contact works!</h1>")


def collaborations(request):
    # Other code

    node6 = flow.FlowNode(endpoints.Endpoint(endpoint="/collaborations", id=collaborations), name="Collaborations")
    metricman.add_to_analytics(node6)

    # any return stuff
    return HttpResponse("<h1>Collaborations works!</h1>")


def events(request):
    # Other code

    node5 = flow.FlowNode(endpoints.Endpoint(endpoint="/events", id=events), name="Events")
    metricman.add_to_analytics(node5)

    # any return stuff
    return HttpResponse("<h1>Events works!</h1>")


def home(request):
    node1 = flow.FlowNode(endpoints.Endpoint(endpoint="/home1", id=home), name="Home")
    metricman.add_to_analytics(node1)

    return HttpResponse("<h1>Home works!</h1>")


def dashboard(request):
    # G = nx.random_geometric_graph(20, 0.25)

    graph = metricman.graph.visualize
    # print(f"\n{graph}\n")

    plot = vs.directed_pyvis(graph)

    return render(request, "dashboard_django/index.html", {
        "plot": plot
    })

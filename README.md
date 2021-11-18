# Analyx-Python

## What is Analyx?

**Analyx** is a plug-and-play analytics library written in Python.

## How to use it

Analyx is really easy to integrate with your projects. Here's an example:

Let's say you want to monitor a method ``foo()`` defined as:

```
from random import randint

def foo():
    print(f"Hello world {randint(0,1000000)}!")
```

After adding the required lines, the code will look something like this:

```
from random import randint
from metrics.metrics import Metrics

metricman = Metrics(__file__)
foo_obj = None

def foo():
    print(f"Hello world {randint(0,1000000)}!")
    if foo_obj is None:
        ep1 = endpoints.Endpoint(endpoint="/", id=foo)
        foo_obj = flow.FlowNode(ep1, name="Object1")
    metricman.add_to_analytics(foo_obj, layerName="foo")
```

You can access the metrics of ``foo()`` from the ``metricman`` object with:

```
metricman.display(id='foo')
```

To get all the metrics of all the methods at once:

```
metricman.display()
```

For looking into what more Analyx can do, head to ``tests/flow_test.py``.
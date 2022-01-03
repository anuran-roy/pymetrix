# Pymetrix-Python

[![Docs](https://img.shields.io/website?color=whi&down_color=red&down_message=Offline&label=Docs&logo=readthedocs&logoColor=white&style=for-the-badge&up_color=green&up_message=Online&url=https%3A%2F%2Fanuran-roy.github.io%2Ftags%2Fanalyx%2F)](https://anuran-roy.github.io/tags/pymetrix/)
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

```python
metricman.display(id='foo')
```

To get all the metrics of all the methods at once:

```python
metricman.display()
```

For looking into what more Pymetrix can do, head to ``tests/flow_test.py``.
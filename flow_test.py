from analyx import flow, endpoints  # , metrics
# import json


def foo():
    print("Bar")


def foo2():
    print("Bar2")


def foo3():
    print("Bar3")

graph = flow.Flow(name="TestGraph")
# metricman = metrics.Metrics()

l1 = flow.FlowLayer(label="Layer1")
ep = endpoints.Endpoint(endpoint="/", id=foo)
obj = flow.FlowNode(ep, name="Object1")
l1.addNode(obj)
graph.addLayer(l1)

l2 = flow.FlowLayer(label="Layer2")
ep2 = endpoints.Endpoint(endpoint="/home", id=foo2)
obj2 = flow.FlowNode(ep2, name="Object2")
l2.addNode(obj2)
graph.addLayer(l2)

l3 = flow.FlowLayer(label="Layer3")
ep3 = endpoints.Endpoint(endpoint="/events", id=foo3)
obj3 = flow.FlowNode(ep3, name="Object3")
obj2.comesBefore(obj3)
obj2.comesBefore(obj)
l3.addNode(obj2)
l3.addNode(obj3)
# l3.addNode(obj3)

graph.addLayer(l3)
# graph.addLayer(l3)

print(graph.exists(instance=obj3))
print(obj3)  # .prettyprint()

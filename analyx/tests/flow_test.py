from analyx import flow, endpoints  # , metrics
# import json

graph = flow.Flow(name="TestGraph")
# metricman = metrics.Metrics()

l1 = flow.FlowLayer(label="Layer1")
ep = endpoints.Endpoint(endpoint="/", id=__file__)
obj = flow.FlowNode(ep, name="Object1")
l1.addNode(obj)
graph.addLayer(l1)

l2 = flow.FlowLayer(label="Layer2")
ep2 = endpoints.Endpoint(endpoint="/home", id=__file__)
obj2 = flow.FlowNode(ep2, name="Object2")
l2.addNode(obj2)
graph.addLayer(l2)

l3 = flow.FlowLayer(label="Layer3")
ep3 = endpoints.Endpoint(endpoint="/events", id=__file__)
obj3 = flow.FlowNode(ep3, name="Object3")
l3.addNode(obj2)
l3.addNode(obj3)
# l3.addNode(obj3)

graph.addLayer(l3)
# graph.addLayer(l3)

print(graph.search(instance=obj3))
graph.prettyprint()

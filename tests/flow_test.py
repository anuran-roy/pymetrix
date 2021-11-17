from analyx import flow, endpoints  # , metrics
from .plugins.test_plugin import test_plugin
# import json
# import networkx
import networkx as nx
import matplotlib.pyplot as plt


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

graph = flow.Flow(name="TestGraph")
# metricman = metrics.Metrics()

l1 = flow.FlowLayer(label="Layer1")
ep1 = endpoints.Endpoint(endpoint="/", id=foo1)
obj1 = flow.FlowNode(ep1, name="Object1")
l1.addNode(obj1)
graph.addLayer(l1)

l2 = flow.FlowLayer(label="Layer2")
ep2 = endpoints.Endpoint(endpoint="/home", id=foo2)
obj2 = flow.FlowNode(ep2, name="Object2")
l2.addNode(obj2)
graph.addLayer(l2)

l3 = flow.FlowLayer(label="Layer3")
ep3 = endpoints.Endpoint(endpoint="/events", id=foo3)
obj3 = flow.FlowNode(ep3, name="Object3")
l3.addNode(obj2)
l3.addNode(obj3)
# l3.addNode(obj3)

l4 = flow.FlowLayer(label="Layer4")
ep4 = endpoints.Endpoint(endpoint="/collabs", id=foo4)
obj4 = flow.FlowNode(ep4, name="Object4")

l5 = flow.FlowLayer(label="Layer5")
ep5 = endpoints.Endpoint(endpoint="/events", id=foo5)
obj5 = flow.FlowNode(ep5, name="Object5")

obj2.comesBefore(obj3)
obj2.comesBefore(obj1)
obj2.comesBefore(obj4)
obj3.comesBefore(obj5)
obj3.comesBefore(obj4)
obj1.comesBefore(obj4)
obj4.comesAfter(obj5)
obj5.comesAfter(obj1)
obj5.comesAfter(obj2)
obj5.comesBefore(obj2)

graph.addLayer(l3)
graph.addLayer(l4)
graph.addLayer(l5)

print(graph.exists(instance=obj2))
print(graph.serialize)  # .prettyprint()
# print(graph.pretty_serialize)
graph.prettyprint()
print(graph.visualize)
# print(json.dumps(graph.pretty_serialize, indent=4))


#Block to visualize network
G = nx.DiGraph()
net = graph.visualize

G.add_nodes_from([x[0] for x in net])
for x in net:
    G.add_edge(x[0], x[1])
nx.draw(G,with_labels=True)
plt.draw()
plt.show()
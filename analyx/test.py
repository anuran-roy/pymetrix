from analyx import metrics, flow, endpoints
# import plotly.express as px
# import plotly.io as pio
import networkx as nx
# import matplotlib.pyplot as plt
# from endpoints import Endpoint

g = nx.DiGraph()
a = metrics.Metrics(__file__, db="")

graph = flow.Flow()

l1 = flow.FlowLayer(label="Layer1")
ep = endpoints.Endpoint(endpoint="/", id=__file__)
obj = flow.FlowNode(ep)
l1.addNode(obj)
graph.addLayer(l1)

l2 = flow.FlowLayer(label="Layer2")
ep2 = endpoints.Endpoint(endpoint="/home", id=__file__)
obj2 = flow.FlowNode(ep2)
l2.addNode(obj2)
graph.addLayer(l2)

l3 = flow.FlowLayer(label="Layer3")
ep3 = endpoints.Endpoint(endpoint="/events", id=__file__)
obj3 = flow.FlowNode(ep3)
l3.addNode(obj2)
l3.addNode(obj3)

graph.addLayer(l3)


def foo():
    print("bar")
    a.add_to_analytics([foo])


a.display()
# data = graph._graph
# print("[")
# for i in data:
#     print(f"  {i}")
# print("]")
serial = graph.serialize
for i in serial:
    print(i)
# fig = px.scatter(graph.serialize())

print(graph.exists(obj3))
# g.add_nodes_from(serial[0][0].keys())
# nx.draw(g, with_labels=True)
# plt.draw()
# plt.show()
# pio.write_image(fig, "fig.png")

for i in range(5):
    foo()
    a.display()

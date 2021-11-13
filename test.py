from analyx import metrics, flow, endpoints
import plotly.express as px
import plotly.io as pio
# from endpoints import Endpoint
graph = flow.Flow()
ep = endpoints.Endpoint(name="/")
obj = flow.FlowObject(ep)
graph.addLayer([obj])
ep2 = endpoints.Endpoint(name="/home")
obj2 = flow.FlowObject(ep2)
graph.addLayer([obj2])
ep3 = endpoints.Endpoint(name="/events")
obj3 = flow.FlowObject(ep3)
graph.addLayer([obj2, obj3])
# data = graph._graph

# print("[")
# for i in data:
#     print(f"  {i}")
# print("]")

print(graph.serialize())
fig = px.scatter(graph.serialize())
pio.write_image(fig, "fig.png")

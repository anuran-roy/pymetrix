import networkx as nx
from pyvis.network import Network

import matplotlib.pyplot as plt
from typing import List, Any, Tuple, Dict
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go

def directed_graph(connections: List[Tuple]) -> None:
    G = nx.DiGraph()

    G.add_nodes_from([x[0] for x in connections])
    for x in connections:
        G.add_edge(x[0], x[1])

    nx.draw(G, with_labels=True)
    plt.draw()
    plt.show()
    plt.clf()


def undirected_graph(connections: List[Tuple]) -> None:
    G = nx.Graph()

    G.add_nodes_from([x[0] for x in connections])
    for x in connections:
        G.add_edge(x[0], x[1])
    nx.draw(G, with_labels=True)
    plt.draw()
    plt.show()
    plt.clf()


# def directed_plotly(connections: List[Tuple], **kwargs) -> None:
#     G = nx.DiGraph()

#     G.add_nodes_from([x[0] for x in connections])
#     for x in connections:
#         G.add_edge(x[0], x[1])

#     print(f"\n{G.nodes()}\n")
#     print(f"\n{G.edges()}\n")
#     # G = nx.random_geometric_graph(5, 0.5)
#     print(f"Graph:\n\n{G.edges.data()}")
#     # print(f"{G.}")

#     edge_x = []
#     edge_y = []

#     for edge in G.edges():
#         x0, y0 = edge
#         # x1, y1 = G.nodes[edge[1]]['pos']
#         edge_x.append(x0)
#         # edge_x.append(x1)
#         edge_x.append(None)
#         edge_y.append(y0)
#         # edge_y.append(y1)
#         edge_y.append(None)

#     # print(f"\n\n{edge_x}")
#     # print(f"\n\n{edge_y}")

#     edge_trace = go.Scatter(
#         x=edge_x, y=edge_y,
#         line=dict(width=0.5, color='#888'),
#         # hoverinfo='none',
#         mode='lines')

#     node_x = []
#     node_y = []
#     for node in G.edges():
#         x, y = node
#         node_x.append(x)
#         node_y.append(y)

#     node_trace = go.Scatter(
#         x=node_x, y=node_y,
#         mode='markers',
#         hoverinfo='text',
#         marker=dict(
#             showscale=True,
#             # colorscale options
#             # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
#             # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
#             # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
#             colorscale='YlOrRd',
#             reversescale=True,
#             color=[],
#             size=10,
#             colorbar=dict(
#                 thickness=15,
#                 title='Node Connections',
#                 xanchor='left',
#                 titleside='right'
#             ),
#             line_width=2))

#     edge_x = []
#     edge_y = []
#     for edge in G.edges():
#         x0, y0 = edge
#         # x1, y1 = G.nodes[edge[1]]['pos']
#         edge_x.append(x0)
#         # edge_x.append(x1)
#         edge_x.append(None)
#         edge_y.append(y0)
#         # edge_y.append(y1)
#         edge_y.append(None)

#     edge_trace = go.Scatter(
#         x=edge_x, y=edge_y,
#         line=dict(width=0.5, color='#888'),
#         # hoverinfo='none',
#         mode='lines')

#     node_x = []
#     node_y = []
#     for node in G.edges():
#         x, y = node
#         node_x.append(x)
#         node_y.append(y)

#     node_trace = go.Scatter(
#         x=node_x, y=node_y,
#         mode='markers',
#         hoverinfo='text',
#         marker=dict(
#             showscale=True,
#             # colorscale options
#             #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
#             #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
#             #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
#             colorscale='YlOrRd',
#             reversescale=True,
#             color=[],
#             size=10,
#             colorbar=dict(
#                 thickness=15,
#                 title='Node Connections',
#                 xanchor='left',
#                 titleside='right'
#             ),
#             line_width=2))

#     fig = go.Figure(data=[edge_trace, node_trace],
#              layout=go.Layout(
#                 title='Network graph made with Python',
#                 titlefont_size=16,
#                 showlegend=False,
#                 hovermode='closest',
#                 margin=dict(b=20,l=5,r=5,t=40),
#                 annotations=[dict(
#                     text="",  # "Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
#                     showarrow=False,
#                     xref="paper", yref="paper",
#                     x=0.005, y=-0.002)],
#                 xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#                 yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
#                 )

#     fig.update_layout(
#         height="800", width="1000",
#     )

#     plot = pyo.plot(fig, include_plotlyjs=True, output_type='div')

#     return plot


def directed_pyvis(connections: List[Tuple], **kwargs) -> str:
    G = nx.DiGraph()

    # G.add_nodes_from([x[0] for x in connections])

    for x in connections:
        G.add_node(x[0], data=x[2])  # , label=f'{x[0]}, hits={x[2]["endpoint"]["hits"]}', size=x[2]["endpoint"]["hits"]*15)
        G.add_node(x[1], data=x[3])  # , label=f'{x[1]}, hits={x[3]["endpoint"]["hits"]}', size=x[3]["endpoint"]["hits"]*15)

    for x in connections:
        G.add_edge(x[0], x[1])

    nt = Network(directed=True)
    nt.from_nx(G)

    if "buttons" in kwargs.keys():
        nt.show_buttons(kwargs["buttons"])
    
    nt.toggle_physics(status=False)
    # nt.toggle_hide_edges_on_drag(status=True)
    # nt.toggle_hide_nodes_on_drag(status=True)

    # graph = nt.html  # .replace("body>", "div>").replace("html>", "div>")
    print("\nMaking Pyvis Network...\n")

    print(str(nt.html))
    nt.save_graph("nx.html")

    return open("nx.html", "r").read()

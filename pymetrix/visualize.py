import networkx as nx
from pyvis.network import Network

import matplotlib.pyplot as plt
from typing import List, Tuple, Dict


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


def directed_pyvis(connections: List[Tuple], **kwargs) -> str:
    G = nx.DiGraph()

    # G.add_nodes_from([x[0] for x in connections])

    for x in connections:
        G.add_node(
            x[0], data=x[2]
        )  # , label=f'{x[0]}, hits={x[2]["endpoint"]["hits"]}', size=x[2]["endpoint"]["hits"]*15)
        G.add_node(
            x[1], data=x[3]
        )  # , label=f'{x[1]}, hits={x[3]["endpoint"]["hits"]}', size=x[3]["endpoint"]["hits"]*15)

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

    print(nt.html)
    nt.save_graph("nx.html")

    return open("nx.html", "r").read()

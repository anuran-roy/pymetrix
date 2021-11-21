import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Any, Tuple, Dict


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

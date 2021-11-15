from .endpoints import EndpointType
from typing import List, Dict, Any, NewType
from uuid import uuid4


class FlowNode:
    def __init__(self, endpoint: EndpointType, **kwargs):
        self._id = kwargs["id"] if "name" in kwargs.keys() else uuid4()
        self.endpoint = endpoint
        self._parents: List = []
        self._children: List = []
    
    def __str__(self):
        print(f"Node ID: {self._id}")
        print(f"Corresponding Endpoint: \n{self.endpoint}")
        print(f"Parent Nodes: {self._parents}")
        print(f"Child Nodes: {self._children}")

    # def __repr__(self):
    #     pass

    @property
    def parents(self):
        return self._parents

    @parents.setter
    def parents(self, parents):
        if type(parents) == type([]):
            self._parents += parents
        else:
            self._parents.append(parents)

    @property
    def children(self):
        return self._children

    @children.setter
    def next(self, children_ob):
        if type(children_ob) == type([]):
            self._children += children_ob
        else:
            self._children.append(children_ob)

    @property
    def serialize(self) -> Dict:
        return {
            'node_id': self._id,
            'parents': self._parents,
            'next': self._children,
        }

    def search(self, **kwargs):
        print(f"\t\t-> Searching at Node level... Node {self._id}")
        k = set(kwargs.keys())
        if "endpoint_id" in k:
            if self.endpoint.id == kwargs["endpoint_id"]:
                return self
            else:
                return None

        if "endpoint" in k:
            if self.endpoint.endpoint == kwargs["endpoint"]:
                return self
            else:
                return None

        if "instance" in k and type(kwargs["instance"]) == type(EndpointType):
            if self.endpoint == kwargs["instance"]:
                return self
            else:
                return None

        if "instance" in k and type(kwargs["instance"]) == type(self):
            if self == kwargs["instance"]:
                return self
            else:
                return None

        if "node" in k:
            if self._id == kwargs["node_id"]:
                return self
            else:
                return None

        if "parents" in k:
            if set(kwargs["parents"]).issubset(set(self._parents)):
                return self
            else:
                return None

        if "children" in k:
            if set(kwargs["children"]).issubset(set(self._children)):
                return self
            else:
                return None

        return None


FlowNodeType = NewType('FlowNodeType', FlowNode)


class FlowLayer:
    def __init__(self, **kwargs):
        self._name = kwargs["label"] if "label" in kwargs.keys() else uuid4()
        self._previous = kwargs["previous"] if "previous" in kwargs.keys() else None
        self._next = kwargs["next"] if "next" in kwargs.keys() else None
        self._nodes: List = []

    def addNode(self, node: FlowNodeType, index=-1):
        if index != -1:
            self._nodes.add(index, node)
        else:
            self._nodes.append(node)

    @property
    def nodes(self):
        return self._nodes

    @property
    def length(self):
        return len(self._nodes)

    @property
    def serialize(self) -> Dict:
        serialized_layer: List = []

        for i in self._nodes:
            serialized_layer.append(i.serialize)

        return {
            'layer_id': self._name,
            'nodes': serialized_layer
            }

    def search(self, **kwargs):
        print(f"\t->Searching at FlowLayer level: Layer {self._name}...")
        k = set(kwargs.keys())

        if "label" in k:
            if self._name == kwargs["label"]:
                return self
            else:
                return None

        if "instance" in k:
            if type(self) == type(kwargs["instance"]):
                return self

        results = []
        ct = 1
        for i in self._nodes:
            print(f"\t\t->Searching node {ct}")
            ob = i.search(**kwargs)

            if ob is not None:
                results.append(ob)

            ct += 1

        if results == []:
            return None
        else:
            return results


FlowLayerType = NewType('FlowLayerType', FlowLayer)


class Flow:
    def __init__(self, **kwargs):
        self._name = kwargs["name"] if "name" in kwargs.keys() else uuid4()
        self._graph: List = []

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, graphobj):
        self._graph = graphobj

    # @property
    def addLayer(self, layer, **kwargs):
        if "index" in kwargs.keys():
            left = self._graph[:kwargs["index"]]
            right = self._graph[kwargs["index"]:]
            left.append(layer)
            self._graph = left + right
        else:
            self._graph.append(layer)

    @property
    def serialize(self) -> Dict:
        layers: List = []
        for i in self._graph:
            layers.append(i.serialize)
        return {
            "flow_id": self._name,
            "layers": layers
        }

    # Search methods:

    def search(self, **kwargs):
        print("Searching at Graph level...")
        results = []
        for i in self._graph:
            ob = i.search(**kwargs)

            if ob is not None:
                results.append(ob)

        if results == []:
            return None
        else:
            return results

    def exists(self, **kwargs):
        try:
            if self.search(**kwargs) is not None:
                return True
            else:
                return False
        except Exception:
            return None

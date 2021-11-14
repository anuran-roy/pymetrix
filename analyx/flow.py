from .endpoints import EndpointType
from typing import List, Dict, Any, NewType
from uuid import uuid4


class FlowNode:
    def __init__(self, endpoint: EndpointType):
        self._id = endpoint
        self._previous: List = []
        self._next: List = []

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, parents):
        if type(parents) == type([]):
            self._previous += parents
        else:
            self._previous.append(parents)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, children):
        if type(children) == type([]):
            self._next += children
        else:
            self._next.append(children)

    @property
    def serialize(self) -> Dict:
        return {
            'node_id': self._id,
            'previous': self._previous,
            'next': self._next,
        }

    def search(self, endpoint: EndpointType):
        if self._id == endpoint:
            return self
        else:
            return None

    def search(self, **kwargs):
        k = set(kwargs.keys())
        if "id" in k:
            if self._id.id == kwargs["id"]:
                return self
            else:
                return None

        if "endpoint" in k:
            if self._id.endpoint == kwargs["endpoint"]:
                return self
            else:
                return None

        if "instance" in k:
            if self._id == kwargs["instance"]:
                return self
            else:
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
        k = set(kwargs.keys())
        pass

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

    # Search by endpoint name
    def search(self, endpoint: str):
        for i in range(len(self._graph)):
            for j in range(len(self._graph[i])):
                flownode = self._graph[i][j]
                ep = flownode.id
                if ep.id == endpoint:
                    return [i, j, ep]

        return None

    # # Search by Endpoint object
    # def search(self, endpoint: EndpointType):
    #     for i in range(len(self._graph)):
    #         for j in range(len(self._graph[i])):
    #             flownode = self._graph[i][j]
    #             ep = flownode.id
    #             if ep == endpoint:
    #                 return [i, j, ep]

    #     return None

    # # Search by FlowNode object
    # def search(self, flownode: FlowNodeType):
    #     for i in range(len(self._graph)):
    #         for j in range(len(self._graph[i])):
    #             flownd = self._graph[i][j]
    #             if flownd == flownode:
    #                 return [i, j, flownd]

    #     return None

    def exists(self, obj: Any):
        try:
            if self.search(obj) is not None:
                return True
            else:
                return False
        except Exception:
            return False

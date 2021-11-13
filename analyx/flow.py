from .endpoints import Endpoint

class FlowObject:
    def __init__(self, endpoint):
        self.id = endpoint
        self._previous = []
        self._next = []

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
            self._previous += children
        else:
            self._previous.append(children)

class Flow:
    def __init__(self):
        self.init = None
        self._graph = []

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
    
    def serialize(self):
        graph_dict = {}
        layers = list()
        for i in range(len(self._graph)):
            layer = list()
            for j in range(len(self._graph[i])):
                ele = self._graph[i][j].__dict__ # Dictionary of FlowObject instance
                ele["id"] = ele["id"].__dict__ if type(ele["id"]) != type({}) else ele["id"]# Dictionary of Endpoint instance
                # print(ele)
                layer.append(ele)
            layers.append(layer)

        return layers

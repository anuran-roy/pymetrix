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
    def graph(self, layer):
        pass
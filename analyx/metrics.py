from .endpoints import Endpoint
from .flow import Flow, FlowNode, FlowLayer, FlowNodeType, FlowLayerType, Flow, FlowType
from .settings import PLUGINS
from typing import List, Dict, Any
from .plugins import PluginType
from . import errors
from uuid import uuid4


class MetricsBase:
    def __init__(self, **kwargs):
        self._plugins: List = list(PLUGINS)
        # for plg in self._plugins:
        #     globals()[lib] = __import__(plg)
        print(f"\n\nPlugins list: {self._plugins}\n\n")
        
        name = kwargs["name"] if "name" in kwargs.keys() else uuid4()
        self._graph = Flow(name=name)

    @property
    def plugins(self):
        return self._plugins
    
    # def addPlugin(self, plg: PluginType):
    #     if plg in self.plugins:
    #         raise errors.PluginAlreadyExists(which=plg._metadata["plugin"])



class Metrics(MetricsBase):
    def __init__(self, loc, **kwargs):
        super().__init__()
        self.id = loc
        self.endpoints: List = []
        self.db = kwargs["db"] if "db" in kwargs.keys() else None
    
    def add_to_analytics(self, node: FlowNodeType, layerName: str = str(uuid4().hex), **kwargs):
        layer_query = self._graph.search(label=layerName)
        layer_to_add_to = None

        if layer_query is None:
            layer_to_add_to = FlowLayer(label=layerName)
        else:
            layer_to_add_to = layer_query[0]
        
        if layer_to_add_to.search(instance=node) is None:
            layer_to_add_to.addNode(node)
        else:
            node._endpoint.hits += 1

        if layer_query == None:
            self._graph.addLayer(layer_to_add_to)


    def display(self, **kwargs):

        # print(f"\n\n{self.id}\n\n")
        ep = None

        if 'id' in kwargs.keys():
            for i in self.endpoints:
                if i['id'] == kwargs['id']:
                    ep = [i]
                    break
        else:
            ep = self.endpoints

        print("\n\nId:\tHits\n")

        for i in ep:
            data = i['endpoint'].stats()

            for j in data.keys():
                print(f"{j}: {data[j]}", end="\t")

            print()

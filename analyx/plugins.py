from .flow import FlowNode, FlowNodeType, FlowLayer, FlowLayerType
from typing import List, Dict, Any, Tuple, NewType
from datetime import datetime


class Plugin:
    def __init__(self):
        self.nodes_to_monitor: List = []
        self.layers_to_monitor: List = []
        self._metadata = {
            "plugin": "My awesome plugin",
            "description": "This is my awesome new plugin",
            "added_on": datetime.now(),
        }

    @property
    def nodeAttributes(self):
        return self.nodes_to_monitor[0].__dict__.keys()

    @property
    def layerAttributes(self):
        return self.layers_to_monitor[0].__dict__.keys()

    @property
    def metadata(self):
        return self._metadata

    def setMetadata(self, metadata_dict):
        pass

    def createSchema(self, details_dict):
        pass

    def addNode(self, node: FlowNodeType):
        self.nodes_to_monitor.append(node)

    def addEntry(self, entry):
        pass

    def results(self):
        return {}


PluginType = NewType("PluginType", Plugin)

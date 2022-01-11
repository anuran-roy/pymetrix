from typing import List, Dict, Any, Tuple, NewType
from datetime import datetime

class Plugin:
    def __init__(self) -> None:
        self.nodes_to_monitor: List = []
        self.layers_to_monitor: List = []
        self._metadata: Dict = {
            "plugin": "My awesome plugin",
            "description": "This is my awesome new plugin",
            "added_on": datetime.now(),
        }

    @property
    def nodeAttributes(self) -> List:
        return self.nodes_to_monitor[0].__dict__.keys()

    @property
    def layerAttributes(self) -> List:
        return self.layers_to_monitor[0].__dict__.keys()

    @property
    def metadata(self):
        return self._metadata

    def setMetadata(self, metadata_dict) -> Any:
        pass

    def createSchema(self, details_dict) -> Any:
        pass

    def addNode(self, node: FlowNodeType) -> None:
        self.nodes_to_monitor.append(node)

    def addEntry(self, entry) -> Any:
        pass

    def results(self) -> Dict:
        return {}


PluginType = NewType("PluginType", Plugin)

if __name__ == "__main__":
    PluginType = NewType("PluginType", Plugin)

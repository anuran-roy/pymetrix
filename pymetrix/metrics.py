from pymetrix.flow import (
    Flow,
    # FlowNode,
    FlowLayer,
    FlowNodeType,
    FlowLayerType,
    FlowType,
)

# from time import sleep
from pymetrix.settings import PLUGINS  # , set_path
from typing import List, Dict, Any
from pymetrix.plugins import PluginType
from pymetrix.database import StorageHandler

# from functools import lru_cache
from datetime import datetime, timedelta

# from . import errors
from uuid import uuid4

# import .database


class MetricsBase:
    def __init__(self, **kwargs):
        # set_path()
        self._plugins: List = list(PLUGINS)

        print(f"\n\nPlugins list: {self._plugins}\n\n")

        name = kwargs["name"] if "name" in kwargs.keys() else str(uuid4().hex)
        self._graph: FlowType = Flow(name=name)

    @property
    def plugins(self) -> List[PluginType]:
        return self._plugins

    # def addPlugin(self, plg: PluginType):
    #     if plg in self.plugins:
    #         raise errors.PluginAlreadyExists(which=plg._metadata["plugin"])


class Metrics(MetricsBase):
    def __init__(self, loc, **kwargs):
        super().__init__()
        self.id: str = loc
        self.endpoints: List = []
        self.db = kwargs["db"] if "db" in kwargs.keys() else None
        self.last_inserted: FlowNodeType = None

    @property
    def graph(self) -> FlowType:
        return self._graph

    def add_to_analytics(
        self, node: FlowNodeType, layerName: str = str(uuid4().hex), **kwargs
    ):
        layer_query: Any = self._graph.search(label=layerName)
        layer_to_add_to: FlowLayerType = None

        if layer_query is None:
            layer_to_add_to = FlowLayer(label=layerName)
        else:
            layer_to_add_to = layer_query[0]

        if layer_to_add_to.search(instance=node) is None:
            layer_to_add_to.addNode(node)

        # node._endpoint.hits += 1

        if layer_query is None:
            self._graph.addLayer(layer_to_add_to)

        if self.last_inserted is not None:
             self.last_inserted._children.append(node)
           
        self.last_inserted = node

    def display(self, **kwargs) -> None:

        print(f"\n\n{self.id}\n\n")
        # ep = None
        nodes_hit_list: List[Dict] = self._graph.gethits
        
        print("\n\nId:\t\tHits\n")

        if "id" in kwargs.keys():
            for i in nodes_hit_list:
                if i["id"] == kwargs["id"]:
                    print(f'{i["id"]}\t\t{i["hits"]}')
        else:
            for i in nodes_hit_list:
                # print(i)
                print(f'{i["id"]}\t\t{i["hits"]}')

    def time_series(self, **kwargs) -> Dict:
        dct: Dict = {"id": self.id}

        nodes_hit_list: List[Dict] = self._graph.gethits
        dct["nodes"] = nodes_hit_list
        return dct

    def aggregate(self) -> Dict:
        nodes_hit_list: List[Dict] = self._graph.gethits

        return [
            {"id": x["id"], "hits": x["hits"]} for x in nodes_hit_list
        ]

    def pipeline(self, data: str = "time_series", mode: str = "live", **kwargs) -> List:
        last_var = {"id": None, "hits": None, "time": None}

        none_var = {"id": None, "hits": None, "time": None}
        if mode == "live":
            interval: float = (
                1.0 if "interval" not in kwargs.keys() else kwargs["interval"]
            )
            if data == "time_series":
                if "duration" in kwargs.keys():
                    dest = datetime.now() + timedelta(seconds=kwargs["duration"])
                    while datetime.now() <= dest:
                        ts = self.time_series()["nodes"]
                        if len(ts) > 0:
                            # print(f"\nTime Series Data: {ts[-1]}\n")
                            if last_var["time"] != ts[-1]["time"]:
                                last_var = dict(ts[-1])
                                yield ts[-1]
                                # sleep(interval)
                        else:
                            yield none_var
                            # sleep(interval)

                else:
                    while True:
                        ts = self.time_series()["nodes"]
                        if len(ts) > 0:
                            # print(f"\nTime Series Data: {ts[-1]}\n")
                            if last_var["time"] != ts[-1]["time"]:
                                last_var = dict(ts[-1])
                                yield ts[-1]
                                # sleep(interval)
                        else:
                            yield none_var
                            # sleep(interval)

            elif data == "aggregate":
                if "duration" in kwargs.keys():
                    dest = datetime.now() + timedelta(seconds=kwargs["duration"])
                    while datetime.now() <= dest:
                        yield self.aggregate()
                        # sleep(interval)
                else:
                    while True:
                        yield self.aggregate()
                        # sleep(interval)

        elif mode == "snapshot":
            if data == "time_series":
                return self.time_series()
            elif data == "aggregate":
                return self.aggregate()


if __name__ == "__main__":
    print("Hi!")

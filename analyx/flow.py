from analyx import settings, errors
from analyx.endpoints import EndpointType
from typing import List, Dict, Any, NewType
from uuid import uuid4
import json
# import pprint
from datetime import datetime

class FlowNode:
    def __init__(self, endpoint: EndpointType, **kwargs):
        self._name = kwargs["name"] if "name" in kwargs.keys() \
            else str(uuid4().hex)
        self._endpoint: EndpointType = endpoint
        self._parents: List = []
        self._children: List = []
        self.last_inserted: Any = None
        self._marked: int = 0
        self.time: str = str(datetime.now())

    def __str__(self):
        # print(f"Node ID: {self._name}")
        # print(f"Corresponding Endpoint: {self._endpoint}")
        # print(f"Parent Nodes: {self._parents}")
        # print(f"Child Nodes: {self._children}")

        return f'"node_id": {self._name}, "endpoint": {self._endpoint}, "parents": {self._parents}, "children": {self._children}'

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
    def children(self, children_ob):
        if type(children_ob) == type([]):
            self._children += children_ob
        else:
            self._children.append(children_ob)

    def comesBefore(self, inserted_node):
        if settings.VERBOSE:
            print("comesBefore function invoked!Inserted node=\n")
            print(inserted_node)
        if inserted_node not in self._children:
            if settings.VERBOSE:
                print("Branch 1 invoked!")
            self._children.append(inserted_node)
            inserted_node._parents.append(self)
        else:
            raise errors.DuplicateError(
                what=inserted_node._name,
                where=f"list of children of {self._name}"
            )

    def comesAfter(self, inserted_node):
        if settings.VERBOSE:
            print("comesAfter function invoked!Inserted node=\n")
            print(inserted_node)
        if inserted_node not in self._children:
            if settings.VERBOSE:
                print("Branch 1 invoked!")
            self._parents.append(inserted_node)
            inserted_node.children.append(self)
        else:
            raise errors.DuplicateError(
                what=inserted_node._name,
                where=f"list of children of {self._name}"
            )

    @property
    def serialize(self) -> Dict:
        return {
            "node_id": self._name,
            "parents": self._parents,
            "children": self._children,
            "endpoint": self._endpoint.serialize,
        }

    def search(self, **kwargs):
        if settings.VERBOSE:
            print(f"\t\t-> Searching at Node level... Node {self._name}")
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
            if self._name == kwargs["node_id"]:
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

    @property
    def pretty_serialize(self):
        return {
            "node_id": self._name,
            "parents": [x._name for x in self._parents],
            "children": [x._name for x in self._children],
            "endpoint": self._endpoint.pretty_serialize,
        }

    @property
    def visualize(self):
        nodes_pairs = []
        nodes_pairs += [(self._name, x._name, self.pretty_serialize, x.pretty_serialize) for x in self._children]
        nodes_pairs += [(x._name, self._name, x.pretty_serialize, self.pretty_serialize) for x in self._parents]

        return nodes_pairs

    def prettyprint(self):
        print("\n\n=================== Node Contents ===================\n\n")
        print(json.dumps(self.pretty_serialize, indent=4))

    @property
    def gethits(self):
        return {
            "id": self._name,
            "hits": self._endpoint.hits,
            "time": self.time
            }


FlowNodeType = NewType("FlowNodeType", FlowNode)


class FlowLayer:
    def __init__(self, **kwargs):
        self._name = kwargs["label"] if "label" in kwargs.keys()\
            else str(uuid4().hex)
        self._previous = kwargs["previous"] if "previous" in kwargs.keys()\
            else None
        self._next = kwargs["next"] if "next" in kwargs.keys() else None
        self._nodes: List = []

    def addNode(self, node: FlowNodeType, index=-1):
        if node not in self._nodes:
            if index != -1:
                self._nodes.add(index, node)
            else:
                self._nodes.append(node)
        else:
            raise errors.DuplicateError(what=node._name, where=self._name)

    @property
    def nodes(self):
        return self._nodes

    @property
    def length(self):
        return len(self._nodes)

    @property
    def gethits(self) -> List:
        nodes_hit_list: List = []
        for i in self._nodes:
            nodes_hit_list.append(i.gethits)

        return nodes_hit_list

    @property
    def serialize(self) -> Dict:
        serialized_layer: List = []

        for i in self._nodes:
            serialized_layer.append(i.serialize)

        return {"layer_id": self._name, "nodes": serialized_layer}

    @property
    def pretty_serialize(self) -> Dict:
        serialized_layer: List = []

        for i in self._nodes:
            serialized_layer.append(i.pretty_serialize)

        return {"layer_id": self._name, "nodes": serialized_layer}

    @property
    def visualize(self):
        nodes_pairs = []
        for i in self._nodes:
            nodes_pairs += i.visualize

        return nodes_pairs

    def search(self, **kwargs):
        if settings.VERBOSE:
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
            if settings.VERBOSE:
                print(f"\t\t->Searching node {ct}")
            ob = i.search(**kwargs)

            if ob is not None:
                results.append(ob)

            ct += 1

        if results == []:
            return None
        else:
            return results

    def prettyprint(self):
        print("\n\n=================== Layer Contents ===================\n\n")
        print(json.dumps(self.pretty_serialize, indent=4))


FlowLayerType = NewType("FlowLayerType", FlowLayer)


class Flow:
    def __init__(self, **kwargs):
        self._name = kwargs["name"] if "name" in kwargs.keys()\
            else str(uuid4().hex)
        self._graph: List = []

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, graphobj):
        self._graph = graphobj

    @property
    def gethits(self) -> List:
        nodes_hit_list: List = []
        for i in self._graph:
            nodes_hit_list += i.gethits

        return nodes_hit_list

    # @property
    def addLayer(self, layer: FlowLayerType, **kwargs):
        if layer not in self._graph:
            if "index" in kwargs.keys():
                left = self._graph[: kwargs["index"]]
                right = self._graph[kwargs["index"]:]
                left.append(layer)
                self._graph = left + right
            else:
                self._graph.append(layer)
        else:
            raise errors.DuplicateError(what=layer._name, where=self._name)

    @property
    def serialize(self) -> Dict:
        layers: List = []
        for i in self._graph:
            layers.append(i.serialize)
        return {"flow_id": self._name, "layers": layers}

    @property
    def pretty_serialize(self) -> Dict:
        layers: List = []
        for i in self._graph:
            layers.append(i.pretty_serialize)
        return {"flow_id": self._name, "layers": layers}

    @property
    def visualize(self):
        nodes_pairs = []
        for i in self._graph:
            nodes_pairs += i.visualize

        return nodes_pairs

    # Search methods:

    def search(self, **kwargs):
        if settings.VERBOSE:
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

    def detect_remove_cycles(self):
        for i in self._graph:
            pass

    def exists(self, **kwargs):
        try:
            if self.search(**kwargs) is not None:
                return True
            else:
                return False
        except Exception:
            return None

    def prettyprint(self):
        print("\n\n=================== Graph Contents ===================\n\n")
        print(json.dumps(self.pretty_serialize, indent=4))


FlowType = NewType("FlowType", Flow)


if __name__ == "__main__":
    print("Hi!")

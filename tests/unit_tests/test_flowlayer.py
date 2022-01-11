from pymetrix.endpoints import Endpoint, EndpointType

from pymetrix.flow import (
    FlowNode,
    FlowNodeType,
    FlowLayer,
    FlowLayerType,
)


def foo1():
    print("Foo1")


def test_flowLayer_creation():
    l1: FlowLayerType = FlowLayer(label="Layer1")
    ep1: EndpointType = Endpoint(endpoint="/", id=foo1)
    obj1: FlowNodeType = FlowNode(ep1, name="Object1")
    l1.addNode(obj1)

    assert l1.length == 1


def test_flowLayer_nodes():
    l1: FlowLayerType = FlowLayer(label="Layer1")
    ep1: EndpointType = Endpoint(endpoint="/", id=foo1)
    obj1: FlowNodeType = FlowNode(ep1, name="Object1")
    l1.addNode(obj1)

    assert isinstance(l1.nodes, list) and len(l1.nodes) == 1


def test_flowLayer_gethits():
    l1: FlowLayerType = FlowLayer(label="Layer1")
    ep1: EndpointType = Endpoint(endpoint="/", id=foo1)
    obj1: FlowNodeType = FlowNode(ep1, name="Object1")
    l1.addNode(obj1)

    assert isinstance(l1.gethits, list) and len(l1.gethits) == 1


def test_flowLayer_visualize():
    l1: FlowLayerType = FlowLayer(label="Layer1")
    ep1: EndpointType = Endpoint(endpoint="/", id=foo1)
    obj1: FlowNodeType = FlowNode(ep1, name="Object1")
    l1.addNode(obj1)

    assert isinstance(l1.visualize, list) and len(l1.gethits) == 1


def test_flowLayer_serialize():
    l1: FlowLayerType = FlowLayer(label="Layer1")
    ep1: EndpointType = Endpoint(endpoint="/", id=foo1)
    obj1: FlowNodeType = FlowNode(ep1, name="Object1")
    l1.addNode(obj1)

    assert (
        l1.serialize["nodes"][0] == obj1.serialize
        and isinstance(l1.serialize, dict)
        and ["layer_id", "nodes"] == list(l1.serialize.keys())
    )

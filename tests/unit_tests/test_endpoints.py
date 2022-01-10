import pytest

from pymetrix.endpoints import Endpoint, EndpointType


class TestClass:
    def foo1(self):
        print("Foo1")

    def test_endpoint_creation(self):
        ep1: EndpointType = Endpoint(endpoint="Foo1", id=self.foo1)
        assert isinstance(ep1, Endpoint)

    def test_endpoint_init(self):
        ep1: EndpointType = Endpoint(endpoint="Foo1", id=self.foo1)
        assert ep1.hitcount == 1

    def test_endpoint_serialization(self):
        ep1: EndpointType = Endpoint(endpoint="Foo1", id=self.foo1)

        assert ["endpoint_function", "hits", "endpoint"] == list(ep1.serialize.keys())

    def test_endpoint_pretty_serialization(self):
        ep1: EndpointType = Endpoint(endpoint="Foo1", id=self.foo1)

        assert ["endpoint_function", "hits"] == list(ep1.pretty_serialize.keys())

    def test_stats(self):
        ep1: EndpointType = Endpoint(endpoint="Foo1", id=self.foo1)

        assert ep1.stats()["hits"] == 0 and ["id", "hits"] == list(ep1.stats().keys())

    def test_get_endpoint(self):
        ep1: EndpointType = Endpoint(endpoint="Foo1", id=self.foo1)

        assert ep1.get_endpoint() == "Foo1"

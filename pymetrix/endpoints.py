from typing import NewType, Dict  # , List


class Endpoint:
    def __init__(self, **kwargs):
        self.hits = kwargs["hits"] if "hits" in kwargs.keys() else 0
        self.endpoint = kwargs["endpoint"] if "endpoint" in kwargs.keys() else None
        self.id = kwargs["id"] if "id" in kwargs.keys() else None

    @property
    def hitcount(self) -> int:
        self.hits += 1
        print("Hitcount executed!")
        return self.hits

    # @property
    def get_endpoint(self) -> callable:
        return self.endpoint

    # @endpoint.setter
    def set_endpoint(self, val) -> None:
        self.endpoint = val

    def run(self, **kwargs):
        _ = (
            self.endpoint(**kwargs)
            if self.endpoint is not None
            else print("Please append a function to run")
        )

    def stats(self) -> Dict:
        return {
            "id": self.id,
            "hits": self.hits,
        }

    @property
    def serialize(self) -> Dict:
        return {
            "endpoint_function": f"{self.id}",
            "hits": self.hits,
            "endpoint": self.endpoint,
        }

    @property
    def pretty_serialize(self) -> Dict:
        return {"endpoint_function": f"{self.id}", "hits": self.hits}


EndpointType = NewType("EndpointType", Endpoint)

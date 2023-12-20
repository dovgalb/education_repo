from typing import Protocol, TypeVar


class Rider(Protocol):
    def ride(self, param: str):
        ...


def print_ride(instance: Rider):
    instance.ride()


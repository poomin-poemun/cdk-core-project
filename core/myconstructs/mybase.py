from typing import Any


class MyBase:
    def __init__(self, obj: Any, name: str):
        self.obj = obj
        self.name = name
        self.myif = {}

    def create(self) -> Any:
        pass

    def get_name(self) -> str:
        return self.name

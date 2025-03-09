from typing import Any

from constructs import Construct


class MyBase:
    def __init__(self, construct: Construct, name: str):
        self.construct = construct
        self.name = name
        self.myif = {}

    def create(self, myif: dict) -> Any:
        tmpdict: dict ={"scope": self.construct}
        tmpif: dict = {**tmpdict,**myif}
        self.myif = myif
        return self._rsc_(rscif=tmpif, myif=self.myif)

    def _rsc_(self, rscif: dict, myif: dict) -> Any:
        pass

    def get_name(self) -> str:
        return self.name

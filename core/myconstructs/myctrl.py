import sys
from typing import Any

from aws_cdk import Stack, Tags

from core.basetypes.mycommon import MyCommonIF
from core.myconstructs.mybase import MyBase
from core.utils.reprice import rep_rice


class MyCtrl:
    def __init__(self, config: dict):
        self.config: dict = config
        self.common = MyCommonIF(**config["common"])

    def create(self, base: MyBase) -> Any:
        myif = self.get_myif(name=base.get_name())
        tmp = base.create(myif=myif)
        tmpret, tmpconfig = rep_rice(self.config)
        self.config = tmpconfig
        return tmp

    def get_myif(self, name: str):
        tmp: Any = None
        try:
            for leaf in name.split("."):
                if tmp is None:
                    tmp = self.config[leaf]
                else:
                    tmp = tmp[leaf]
        except KeyError as e:
            print(e)
            print(f"Error not found key from yaml file check name:{name} keyword:{leaf}")
            sys.exit("error end.")
        return tmp

    def add_common_tags(self, stack: Stack):
        if self.common.tags is not None:
            for key,value in self.common.tags.items():
                Tags.of(stack).add(key=key,value=value)
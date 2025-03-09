from typing import Mapping, Optional

from pydantic import BaseModel


class MyCommonIF(BaseModel):
    region: str
    account: str
    tags : Optional[Mapping[str,str]] = None

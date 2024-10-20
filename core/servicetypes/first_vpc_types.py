from typing import Mapping,Sequence,Optional
from pydantic import BaseModel
from core.basetypes.mycommon import MyCommonIF
from core.basetypes.myec2 import MyVPCIF


class FirstVpcIF(BaseModel):
      vpcs: Optional[Mapping[str,MyVPCIF]] = None

class FirstVpcTypes(BaseModel):
    common: MyCommonIF
    firstvpc : FirstVpcIF
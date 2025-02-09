from typing import Mapping,Sequence,Optional
from pydantic import BaseModel
from core.basetypes.mycommon import MyCommonIF
from core.basetypes.myec2 import (
     MyVPCIF,
     MyRouteTableIF,
     MyRouteIF,
     MyInternetGatewayIF,
     MyVPCGatewayAttachmentIF
)


class FirstVpcIF(BaseModel):
      vpcs: Optional[Mapping[str,MyVPCIF]] = None
      route_tables: Optional[Mapping[str,MyRouteTableIF]] = None
      igws: Optional[Mapping[str,MyInternetGatewayIF]] = None
      routes: Optional[Mapping[str,MyRouteIF]] = None
      vpcgatewayattachs: Optional[Mapping[str,MyVPCGatewayAttachmentIF]] = None

class FirstVpcTypes(BaseModel):
    common: MyCommonIF
    firstvpc : FirstVpcIF
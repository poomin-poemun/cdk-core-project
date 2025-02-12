import re
from enum import Enum
from typing import Any

import simplejson as json


class RepRiceRslt(Enum):
    OK = 0
    NG = 1
    NOTFUND = 2


def rep_rice(trg_config: dict):
    rtn_code = RepRiceRslt.NG
    rtn_config: dict = trg_config
    flg_success: bool = False
    flg_notfind: bool = False
    pattern = "\\{\\{[a-zA-Z0-9\\.\\-_\\[\\]]+\\}\\}"
    jsondata: str = json.dumps(trg_config)
    result = re.finditer(pattern, jsondata)
    # ヒットした文字列をループして置換してく
    for one_rslt in result:
        # ヒットした文字列を取得
        match_str: str = one_rslt.group()
        tmprep_str = match_str.replace("{{", "")
        trg_str = tmprep_str.replace("}}", "")
        flg, value = getvalue(trg_config, trg_str)
        if flg:
            tmpconfig_json = jsondata.replace(match_str, value)
            jsondata = tmpconfig_json
            rtn_config = json.loads(jsondata)
            flg_success = True
        else:
            flg_notfind = True
    if flg_notfind:
        if flg_success:
            rtn_code = RepRiceRslt.OK
        else:
            rtn_code = RepRiceRslt.NOTFUND
    else:
        if flg_success:
            rtn_code = RepRiceRslt.OK
    return rtn_code, rtn_config


def getvalue(matchdict: dict, target: str):
    tmp: Any = None
    flg: bool = True
    for leaf in target.split("."):
        if tmp is None:
            if leaf in matchdict:
                tmp = matchdict[leaf]
            else:
                flg = False
                break
        else:
            if leaf in tmp:
                tmp = tmp[leaf]
            else:
                flg = False
                break
    return flg, tmp

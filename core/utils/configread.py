from pathlib import Path

import yaml

from core.utils.reprice import rep_rice


def configread(filename: str) -> dict:
    tmpconfig: dict = {}
    with open(filename, encoding="utf-8") as file:
        tmpconfig = yaml.safe_load(file)
    tmpret, config = rep_rice(tmpconfig)

    return config

def configread2(path: str, filename: str) -> dict:
    tmpconfig: dict = {}

    tmplist: dict = {}
    list_file=path + "/" + filename

    with open(list_file, encoding="utf-8") as file:
        tmplist = yaml.safe_load(file)

    tmpcmn: dict = {}
    common_file=path + "/" + tmplist["common"]

    with open(common_file, encoding="utf-8") as file:
        tmpcmn = yaml.safe_load(file)

    tmpconfig.update(tmpcmn)

    stacks=tmplist["stacks"]
    for onestack in stacks:
        tmpstack: dict = {}
        stack_file=path + "/" + onestack
        with open(stack_file, encoding="utf-8") as file:
            tmpstack = yaml.safe_load(file)
        tmpconfig.update(tmpstack)

    tmpret, config = rep_rice(tmpconfig)

    return config
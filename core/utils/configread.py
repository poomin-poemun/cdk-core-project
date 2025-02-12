from pathlib import Path

import yaml

from core.utils.reprice import rep_rice


def configread(filename: str) -> dict:
    tmpconfig: dict = {}
    with open(filename, encoding="utf-8") as file:
        tmpconfig = yaml.safe_load(file)
    tmpret, config = rep_rice(tmpconfig)

    return config

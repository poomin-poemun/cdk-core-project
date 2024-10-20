import yaml
import jinja2
from pathlib import Path


def configread(filename:str):
    yml_file = Path(filename)
    yml_name = yml_file.name
    yml_path = yml_file.parent
    with open(filename, encoding='utf-8')as file:
        tmpconfig = yaml.safe_load(file)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(yml_path))
    template = env.get_template(yml_name)
    config = yaml.safe_load(template.render(**tmpconfig))
    return config
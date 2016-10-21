import json
import yaml
from pprint import pprint



with open ("json-exercise6") as f:
     exercise7json = json.load(f)

pprint(exercise7json)


with open ("yaml-exercise6") as f:
     exercise7yaml = yaml.load(f)

pprint(exercise7yaml)

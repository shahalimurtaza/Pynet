
import yaml
import json



exercise6 = [ 1, 2, 3, 4, 5, { 'key1': 'lock1', 'key2': 2 } , 'some string']

with open ("yaml-exercise6", "w") as f:
    f.write(yaml.dump(exercise6, default_flow_style=False))


with open ("json-exercise6", "w") as f:
     json.dump(exercise6, f)


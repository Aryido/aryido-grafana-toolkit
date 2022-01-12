import json
import os

class Writer:

    @staticmethod
    def write(path, dashboard_json:json):
        with open(path,"w") as f:
            f.write(json.dumps(dashboard_json, indent=4))

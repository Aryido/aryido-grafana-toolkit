from os import walk
from os.path import join
import json


class DashBoardLoader:

    def __init__(self, path: str):
        self.path = path

    def collect_dashboard_path_list(self) -> list:
        paths = []
        for root, dirs, files in walk(self.path):
            for f in files:
                paths.append(join(root, f))           
        return paths


    def collect_dashboard_json_dict(self) -> dict:
        paths = self.collect_dashboard_path_list()
        json_object_dict = {}
        for path in paths:
            with open(path) as f:
                json_object_dict.update({path: json.load(f)})
        return json_object_dict

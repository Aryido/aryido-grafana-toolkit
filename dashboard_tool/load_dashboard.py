from pathlib import Path
import json


class DashBoardLoader:

    def __init__(self, path):
        self.path = path

    def get_dashboard_path_list(self):
        paths = Path(self.path).glob('**/*')
        return [path for path in paths if path.is_file()]

    def get_dashboard_json_list(self):
        paths = self.get_dashboard_path_list()
        json_object_list = []
        for path in paths:
            with open(path) as f:
                json_object_list.append(json.load(f))
        return json_object_list

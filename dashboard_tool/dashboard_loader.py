from pathlib import Path
import json


class DashBoardLoader:

    def __init__(self, path: str):
        self.path = path

    def collect_dashboard_path_list(self) -> list:
        paths = Path(self.path).glob('**/*')
        return [path for path in paths if path.is_file()]

    def collect_dashboard_json_dict(self) -> dict:
        paths = self.collect_dashboard_path_list()
        json_object_dict = {}
        for path in paths:
            with open(path) as f:
                json_object_dict.update({path: json.load(f)})
        return json_object_dict

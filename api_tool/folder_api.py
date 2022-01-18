import json
from api_tool.base_api import BaseApi
import requests


class FolderApi(BaseApi):
    def __init__(self, base_url, token):
        super(FolderApi, self).__init__(base_url, token)

    def find_all_folders(self):
        base_url = self.base_url
        url = base_url + "/api/folders"
        response = requests.get(url, headers=self.generate_header())
        return json.loads(response.text)

    def create_folder(self, title, uid=None):
        base_url = self.base_url
        url = base_url + "/api/folders"
        json_data = dict(title=title)
        if uid is not None:
            json_data["uid"] = uid
        response = requests.post(url, json=json_data, headers=self.generate_header())
        return json.loads(response.text)

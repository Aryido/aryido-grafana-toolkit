import json
from api_tool.base_api import BaseApi
import requests


class DataSourceApi(BaseApi):
    def __init__(self, base_url, token):
        super(DataSourceApi, self).__init__(base_url, token)

    def find_all_datasource(self):
        base_url = self.base_url
        url = base_url + "/api/datasources"
        response = requests.get(url, headers=self.generate_header())
        return json.loads(response.text)

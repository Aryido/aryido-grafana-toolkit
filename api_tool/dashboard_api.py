import json
from api_tool.base_api import BaseApi
import requests


class DashboardApi(BaseApi):
    def __init__(self, base_url, token):
        super(DashboardApi, self).__init__(base_url, token)

    def find_dashboard(self, uid):
        base_url = self.base_url
        url = base_url + "/api/dashboards/uid/{0}".format(uid)
        response = requests.get(url, headers=self.generate_header())
        return json.loads(response.text)

    def create_dashboard(self, dashboard_json):
        search_dashboard_json = self.find_dashboard(dashboard_json["uid"])
        if search_dashboard_json is None:
            dashboard_json.pop("uid")
            base_url = self.base_url
            url = base_url + "/api/dashboards/import"
            response = requests.post(
                url, json=dashboard_json, headers=self.generate_header())
            return json.loads(response.text)
        else:
            raise Exception("exist {0} dashboard...".format(
                dashboard_json["uid"]))

    def update_dashboard(self, dashboard_json):
        search_dashboard_json = self.find_dashboard(dashboard_json["uid"])
        if search_dashboard_json is not None:
            base_url = self.base_url
            url = base_url + "/api/dashboards/db"
            response = requests.post(
                url, json=dashboard_json, headers=self.generate_header())
            return json.loads(response.text)
        else:
            raise Exception("not find dashboard...")

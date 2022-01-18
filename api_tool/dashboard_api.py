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
        if response.status_code == 404 and response.reason == "Not Found":
            return None   
        return json.loads(response.text)
       

    def create_dashboard(self, dashboard_json, folderId=None, folderUid=None):
        uid = dashboard_json["uid"]
        search_dashboard_json = self.find_dashboard(uid)
        if search_dashboard_json is None:
            dashboard_json.pop("id")
            data = {
                "dashboard": dashboard_json,
            }
            if folderId is not None and folderUid is not None:
                data["folderId"] = folderId
                data["folderUid"] = folderUid

            base_url = self.base_url
            url = base_url + "/api/dashboards/import"

            response = requests.post(url, json=data, headers=self.generate_header())
            return json.loads(response.text)
        else:
            raise Exception(f"exist {uid} dashboard...")

    def update_dashboard(self, dashboard_json):
        uid = dashboard_json["uid"]
        search_dashboard_json = self.find_dashboard(uid)
        if search_dashboard_json is not None:
            data = {
                "dashboard": dashboard_json,
            }
            base_url = self.base_url
            url = base_url + "/api/dashboards/db"
            response = requests.post(url, json=data, headers=self.generate_header())
            return json.loads(response.text)
        else:
            raise Exception(f"not find dashboard {uid}...")

from dashboard_tool import dashboard_loader
from dashboard_tool import dashboard_editor
from dashboard_tool import writer

new_variable = {
        "auto": False,
        "auto_count": 30,
        "auto_min": "10s",
        "current": {
          "selected": False,
          "text": "utc0",
          "value": "utc0"
        },
        "description": "Default value : utc0",
        "hide": 0,
        "name": "timeZone",
        "options": [
          {
            "selected": True,
            "text": "utc0",
            "value": "utc0"
          },
          {
            "selected": False,
            "text": "utc8",
            "value": "utc8"
          }
        ],
        "query": "utc0, utc8",
        "queryValue": "",
        "refresh": 2,
        "skipUrlSync": False,
        "type": "interval"
      }


if __name__ == '__main__':

    path = "D:\\workspace\\docker-workspace\\Grafana-Dashboard-Config\\Operation\\provisioning\\dashboards\\swagger\\fews-dataset\observed"

    dashboard_loader = dashboard_loader.DashBoardLoader(path)
    dict = dashboard_loader.collect_dashboard_json_dict()
    for (p, dashboard_json) in dict.items():
        dashboard_json = dashboard_editor.create_variable(dashboard_json,new_variable)
        writer.write(p, dashboard_json)
from dashboard_tool import dashboard_loader
from dashboard_tool import panel_editor
from dashboard_tool import writer


if __name__ == '__main__':

    path = "D:\\workspace\\docker-workspace\\Grafana-Dashboard-Config\\Operation\\provisioning\\dashboards\\swagger\\fews-dataset\observed"

    dashboard_loader = dashboard_loader.DashBoardLoader(path)
    dict = dashboard_loader.collect_dashboard_json_dict()
    # for (p, dashboard_json) in dict.items():
    #     #need to change
    #     panel_editor.add_dataSource_parameter(dashboard_json)
    #     writer.write(p, dashboard_json)

    for (p, dashboard_json) in dict.items():
        #need to change
        panel_editor.add_query_parameter_into_content2(dashboard_json)
        writer.write(p, dashboard_json)

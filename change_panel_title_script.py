from dashboard_tool import dashboard_loader
from dashboard_tool import panel_editor
from dashboard_tool import writer


if __name__ == '__main__':

    path = "D:\\workspace\\docker-workspace\\Grafana-Dashboard-Config\\Operation\\provisioning\\dashboards\\swagger\\fews-dataset\observed"

    dashboard_loader = dashboard_loader.DashBoardLoader(path)
    dict = dashboard_loader.collect_dashboard_json_dict()
    # for (p, dashboard_json) in dict.items():
    #     panel_editor.edit_title(
    #         dashboard_json,
    #         "time-zero[compact] with range and locationId",
    #         "row",
    #         lambda v: "time-zero[compact] with range and location"
    #     )

    #     writer.write(p, dashboard_json)

    for (p, dashboard_json) in dict.items():
        panel_editor.edit_panel_title_in_row(
            dashboard_json,
            "time-zero[compact] with range",
            "Responses",
            "fondus-jsonpretty-panel",
            lambda v: "API Response"
        )
        writer.write(p, dashboard_json)

    for (p, dashboard_json) in dict.items():
        panel_editor.edit_panel_title_in_row(
            dashboard_json,
            "time-zero[compact] with range and location",
            "Responses",
            "fondus-jsonpretty-panel",
            lambda v: "API Response Query with ${locationId}"
        )
        writer.write(p, dashboard_json)


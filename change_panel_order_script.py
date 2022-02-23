from dashboard_tool import dashboard_loader
from dashboard_tool import panel_editor
from dashboard_tool import writer


if __name__ == '__main__':

    path = "D:\\workspace\\docker-workspace\\Grafana-Dashboard-Config\\Operation\\provisioning\\dashboards\\swagger\\fews-dataset\observed"

    dashboard_loader = dashboard_loader.DashBoardLoader(path)
    dict = dashboard_loader.collect_dashboard_json_dict()
    for (p, dashboard_json) in dict.items():
        panel_editor.edit_row_gridPos(
            dashboard_json,
            "latest",
            6
        )

        panel_editor.edit_row_gridPos(
            dashboard_json,
            "latest with location",
            7
        )

        panel_editor.edit_row_gridPos(
            dashboard_json,
            "time-zero",
            8
        )

        panel_editor.edit_row_gridPos(
            dashboard_json,
            "time-zero with location",
            9
        )

        panel_editor.edit_row_gridPos(
            dashboard_json,
            "time-zero with range",
            10
        )

        panel_editor.edit_row_gridPos(
            dashboard_json,
            "time-zero with range and location",
            11
        )

        panel_editor.edit_row_gridPos(
            dashboard_json,
            "time-zero[compact] with range",
            12
        )

        panel_editor.edit_row_gridPos(
            dashboard_json,
            "time-zero[compact] with range and location",
            13
        )
        writer.write(p, dashboard_json)

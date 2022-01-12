from dashboard_tool import loader
from dashboard_tool import dashboard_editor
from dashboard_tool import panel_editor
from dashboard_tool import writer


if __name__ == '__main__':

    path = "D:\workspace\docker-workspace\Grafana-Dashboard-Config\Operation\provisioning\dashboards\swagger"

    dashboard_loader = loader.DashBoardLoader(path)

    dict = dashboard_loader.collect_dashboard_json_dict()

    for (path, dashboard_json) in dict.items():
        dashboard_json = dashboard_editor.edit_title(
            dashboard_json,
            lambda title: "FEWS "+title
        )

        dashboard_json = dashboard_editor.edit_variable(
            dashboard_json,
            "dataset",
            "variable",
            lambda v: "${" + v + "}"
        )

        dashboard_json = dashboard_editor.edit_variable(
            dashboard_json,
            "dataset",
            "variable",
            lambda v: "\"" + v
        )

        panel_editor.edit_dataSource(
            dashboard_json,
            "P4A126EC1F9644871",
            "fewstaiwan-dataflow-dataset-service-taichung"
        )

        writer.write(path, dashboard_json)
        break

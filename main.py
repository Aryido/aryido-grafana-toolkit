import pathlib
from dashboard_tool import dashboard_loader
from dashboard_tool import dashboard_editor
from dashboard_tool import panel_editor
from dashboard_tool import writer


if __name__ == '__main__':

    path = "D:\\workspace\\docker-workspace\\Grafana-Dashboard-Config\\Operation\\provisioning\\dashboards\\swagger"
    #path = "D:\\workspace\\docker-workspace\\Grafana-Dashboard-Config\\Operation\\provisioning\\dashboards\\swagger\\fews-dataset\\simulated"

    dashboard_loader = dashboard_loader.DashBoardLoader(path)

    dict = dashboard_loader.collect_dashboard_json_dict()
    
    for (path, dashboard_json) in dict.items():
        # dashboard_json = dashboard_editor.edit_title(
        #     dashboard_json,
        #     lambda title: "FEWS "+title
        # )

        # dashboard_json = dashboard_editor.edit_variable(
        #     dashboard_json,
        #     "dataset",
        #     "variable",
        #     lambda v: "${" + v + "}"
        # )

        #dashboard_json = panel_editor.edit_dataSource(
        #     dashboard_json,
        #     "P4A126EC1F9644871",
        #     "fewstaiwan-dataflow-dataset-service-taichung"
        # )

        # dashboard_json = dashboard_editor.replace_string(
        #     dashboard_json,
        #     'gateway.fondus.com.tw',
        #     'gateway:8080',
        #     lambda v: v
        # )

        writer.write(path, dashboard_json)


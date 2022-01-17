import pathlib
import requests
import json
from dashboard_tool import dashboard_loader
from dashboard_tool import dashboard_editor
from dashboard_tool import panel_editor
from dashboard_tool import writer
from api_tool import datasource_api


if __name__ == '__main__':

    api_key="eyJrIjoiOWduMGtIb0tLVzdSNlJVeTVFMllkVmY3WGc4QTJVS3AiLCJuIjoiZ3JhZmFuYS1weXRob24tdG9vbGtpdCIsImlkIjoxfQ=="
    
    datasource_api = datasource_api.DataSourceApi("http://localhost:3000/grafana" , api_key)
    datasource_list = datasource_api.find_all_datasource()
    list = []
    for datasource in datasource_list:
        obj = {
            "name": datasource["name"],
            "uid": datasource["uid"]
        }
        list.append(obj)
    
    #print(list)


    path = "D:\\workspace\\docker-workspace\\Grafana-Dashboard-Config\\Operation\\provisioning\\dashboards\\swagger"
    #path = "D:\\workspace\\docker-workspace\\Grafana-Dashboard-Config\\Operation\\provisioning\\dashboards\\swagger\\fews-dataset\\simulated"

    dashboard_loader = dashboard_loader.DashBoardLoader(path)

    dict = dashboard_loader.collect_dashboard_json_dict()
    
    for (p, dashboard_json) in dict.items():
        # dashboard_json = dashboard_editor.edit_title(
        #     dashboard_json,
        #     lambda title: "FEWS " + title
        # )

        # dashboard_json = dashboard_editor.edit_variable(
        #     dashboard_json,
        #     "dataset",
        #     "variable",
        #     lambda v: "${" + v + "}"
        # )

        # dashboard_json = panel_editor.edit_dataSource(
        #     dashboard_json,
        #     "P4A126EC1F9644871",
        #     "fewstaiwan-dataflow-dataset-service-taichung"
        # )

        # dashboard_json = dashboard_editor.replace_string(
        #     dashboard_json,
        #     'fondus-jsontext-panel',
        #     'fondus-jsonpretty-panel',
        #     lambda v: v
        # )

        # writer.write(path, dashboard_json)
       
        dashboard_json.pop("id")
        datadb = {
                "dashboard": dashboard_json,
                }
        response=requests.post("http://localhost:3000/grafana/api/dashboards/import", json = datadb, headers={
        "Accept": "application/json",
        "Content-Type": "application/json",
        'Authorization': "Bearer eyJrIjoiOWduMGtIb0tLVzdSNlJVeTVFMllkVmY3WGc4QTJVS3AiLCJuIjoiZ3JhZmFuYS1weXRob24tdG9vbGtpdCIsImlkIjoxfQ=="
        })
        print(response)
       

    # response  = requests.get("http://localhost:3000/grafana/api/datasources", headers={
    #     "Accept": "application/json",
    #     "Content-Type": "application/json",
    #     'Authorization': api_key
    #     })
    # print(response.text)

    



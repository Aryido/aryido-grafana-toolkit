from dashboard_tool import dashboard_loader
from api_tool import dashboard_api
from api_tool import folder_api

if __name__ == '__main__':
    api_key = "eyJrIjoiREJNeTR4WURPdTFMMUdHQThCSjBObmREc0pZd1VZRnMiLCJuIjoidXBMb2FkRGFzaEJvYXJkIiwiaWQiOjF9"
    dashboard_api = dashboard_api.DashboardApi("http://localhost:3000/grafana", api_key)
    folder_api = folder_api.FolderApi("http://localhost:3000/grafana", api_key)

    folder_id = '';
    folder_uid = '';
    folders = folder_api.find_all_folders();

    if len(folders) == 0:
         folder_list = folder_api.create_folder("swagger-fews-datasets")
         folder_uid = folder_list['uid']
         folder_id = folder_list['id']
    else:
        for i  in range(len(folders)):
            folder = folders[i]
            if(folder['title'] == 'swagger-fews-datasets'):
                folder_uid = folder['uid']
                folder_id = folder['id']
                break;
            else:
                if i == len(folders) - 1:
                    folder_api.create_folder("swagger-fews-datasets")
                    folder_list = folder_api.find_all_folders()
                    for folder in folder_list:
                        if(folder['title'] == 'swagger-fews-datasets'):
                            folder_uid = folder['uid']
                            folder_id = folder['id']
                            break;

    path = "D:\workspace\docker-workspace\Grafana-Dashboard-Config\Operation\provisioning\dashboards\swagger"
    dashboard_loader = dashboard_loader.DashBoardLoader(path)
    dict = dashboard_loader.collect_dashboard_json_dict()

    for (p, dashboard_json) in dict.items():
        dashboard_api.create_dashboard(dashboard_json, folderId=folder_id, folderUid=folder_uid)

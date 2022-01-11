from load_dashboard import DashBoardLoader

path = 'D:\intelliJDataSource\Grafana-Dashboard-Config\Operation\provisioning\dashboards\swagger'

loader = DashBoardLoader(path)
json_object_list = loader.get_dashboard_json_list()

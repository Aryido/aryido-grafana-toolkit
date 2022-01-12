from loader import DashBoardLoader
from editor import DashBoardEditor, PanelEditor
from writer import Writer


if __name__ == '__main__':
    
   path = "D:\dataSource\pythontest\swagger"

   dashboard_loader = DashBoardLoader(path)

   dict = dashboard_loader.collect_dashboard_json_dict()

   for (path, dashboard_json) in dict.items():
      # dashboard_json = DashBoardEditor.edit_title(
      #    dashboard_json,
      #    lambda title: "FEWS "+title
      # )

      # dashboard_json = DashBoardEditor.edit_variable( 
      #    dashboard_json,
      #    "dataset",
      #    "variable",
      #    lambda v: "${"+ v +"}"
      # )

      # PanelEditor.edit_dataSource(
      #    dashboard_json, 
      #    "P4A126EC1F9644871", 
      #    "fewstaiwan-dataflow-dataset-service-taichung"
      # )
      
      # Writer.write(path, dashboard_json)
      break

   


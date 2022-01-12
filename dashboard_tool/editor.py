import json

class DashBoardEditor:

    @staticmethod
    def replace_string(dashboard_json:json, old_variable:str, new_variable:str, functional):
        json_string = json.dumps(dashboard_json)
        json_string = json_string.replace(functional(old_variable), functional(new_variable))
        return json.loads(json_string)

    @staticmethod
    def edit_title(dashboard_json:json, functional):
        title = dashboard_json["title"]
        dashboard_json["title"] = functional(title)  
        return dashboard_json
    
    @staticmethod
    def edit_variable(dashboard_json:json, old_variable:str, new_variable:str, functional):
        dashboard_json = DashBoardEditor.__edit_templating_variable(dashboard_json, old_variable, new_variable)
        return DashBoardEditor.replace_string(dashboard_json, old_variable, new_variable, functional)

    @staticmethod
    def __edit_templating_variable(dashboard_json:json, old_variable:str, new_variable:str):
        variableList = dashboard_json["templating"]["list"]
        for variable in variableList:
            if variable["name"] == old_variable:
                variable["name"] = new_variable
        return dashboard_json
    
                   
class PanelEditor:

    @staticmethod
    def edit_title(dashboard_json:json, title:str, type:str, functional):     
        for panel in dashboard_json["panels"]:
            if panel["type"] == "row":
                if(len(panel["panels"]) != 0):
                    for subpanel in panel["panels"]:
                        if subpanel["title"] == title and subpanel["type"] == type:
                            title = dashboard_json["title"]
                            subpanel["title"] = functional(title)

            if panel["title"] == title and panel["type"] == type:
                title = dashboard_json["title"]
                panel["title"] = functional(title)
                    
        return dashboard_json

    @staticmethod
    def edit_dataSource(dashboard_json:json, old_uid:str, new_uid:str):     
        for panel in dashboard_json["panels"]:
            if panel["type"] == "row":
                if(len(panel["panels"]) != 0):
                    for subpanel in panel["panels"]:
                        if "datasource" in subpanel:
                            if subpanel["datasource"]["uid"] == old_uid:
                                subpanel["datasource"]["uid"] = new_uid

            if "datasource" in panel:
                if panel["datasource"]["uid"] == old_uid:
                    panel["datasource"]["uid"] = new_uid
                 
        return dashboard_json
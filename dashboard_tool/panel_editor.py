import json


def edit_title(dashboard_json: json, title: str, type: str, functional) -> json:
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


def edit_dataSource_uid(dashboard_json: json, old_uid: str, new_uid: str) -> json:
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

#deprecate
#need to modify
def edit_row_gridPos(dashboard_json: json, title: str, y: int) -> json:
    for panel in dashboard_json["panels"]:
        if panel["title"] == title and panel["type"] == "row":
            gridPos = panel["gridPos"]
            gridPos["y"] = y;
    return dashboard_json

#deprecate
#need to modify
def add_dataSource_parameter(dashboard_json: json) -> json:
    for panel in dashboard_json["panels"]:
        if panel["type"] == "row" and panel["title"] != "latest" and panel["title"] != "latest with location":
            if(len(panel["panels"]) != 0):
                for subpanel in panel["panels"]:
                    if "Response" in subpanel["title"]:
                        subpanel["targets"][0]["params"].append(["timeZone","${timeZone}"]);
    return dashboard_json

#deprecate
#need to modify
def add_query_parameter_into_content(dashboard_json: json) -> json:
    for panel in dashboard_json["panels"]:
        if panel["type"] == "row" and panel["title"] != "latest" and panel["title"] != "latest with location":
            if(len(panel["panels"]) != 0):
                for subpanel in panel["panels"]:
                    if "Request" in subpanel["title"]:
                        subpanel["options"]["content"] = subpanel["options"]["content"].replace('?', '?timeZone={{variable \"timeZone\"}}&')
                        subpanel["options"]["defaultContent"] = subpanel["options"]["defaultContent"].replace('?', '?timeZone={{variable \"timeZone\"}}&')

    return dashboard_json

#deprecate
#need to modify
def add_query_parameter_into_content2(dashboard_json: json) -> json:
    for panel in dashboard_json["panels"]:
        if panel["type"] == "row" and panel["title"] == "time-zero":
            if(len(panel["panels"]) != 0):
                for subpanel in panel["panels"]:
                    if "Request" in subpanel["title"]:
                        subpanel["options"]["content"] = subpanel["options"]["content"].replace(
                            '{{variable \"from\"}}',
                            '{{variable \"from\"}}?timeZone={{variable \"timeZone\"}}'
                            )
                        subpanel["options"]["defaultContent"] = subpanel["options"]["defaultContent"].replace(
                            '{{variable \"from\"}}',
                            '{{variable \"from\"}}?timeZone={{variable \"timeZone\"}}'
                            )

    return dashboard_json

#deprecate
#need to modify
def edit_panel_title_in_row(dashboard_json: json, row_title: str, title: str, type: str, functional) -> json:
    for panel in dashboard_json["panels"]:
        if panel["type"] == "row" and panel["title"] == row_title:
            if(len(panel["panels"]) != 0):
                for subpanel in panel["panels"]:
                    if subpanel["title"] == title and subpanel["type"] == type:
                        subpanel["title"] = functional(title)

    return dashboard_json
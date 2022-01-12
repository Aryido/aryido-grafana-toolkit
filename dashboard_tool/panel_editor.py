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


def edit_dataSource(dashboard_json: json, old_uid: str, new_uid: str) -> json:
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

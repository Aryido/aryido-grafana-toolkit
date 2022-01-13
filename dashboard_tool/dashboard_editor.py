import json


def replace_string(dashboard_json: json, old_variable: str, new_variable: str, functional) -> json:
    json_string = json.dumps(dashboard_json)
    fo = functional(old_variable)
    fn = functional(new_variable)
    json_string = json_string.replace(fo, fn)
    dashboard_json = json.loads(json_string)
    return dashboard_json


def edit_title(dashboard_json: json, functional):
    title = dashboard_json["title"]
    dashboard_json["title"] = functional(title)
    return dashboard_json


def edit_variable(dashboard_json: json, old_variable: str, new_variable: str, functional) -> json:
    dashboard_json = __edit_templating_variable(
        dashboard_json, old_variable, new_variable)
    return replace_string(dashboard_json, old_variable, new_variable, functional)


def __edit_templating_variable(dashboard_json: json, old_variable: str, new_variable: str) -> json:
    variableList = dashboard_json["templating"]["list"]
    for variable in variableList:
        if variable["name"] == old_variable:
            variable["name"] = new_variable
    return dashboard_json

import os
import json

def load_all_files(path):
    jsonList=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            jsonList.append(os.path.join(root,file))
    return jsonList

def generate_identity_json(jsonList):
    for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)
            str = json.dumps(jsonObject,indent=4)

        with open(json_file_path,"w") as f:
            f.write(str)

def generate_json_change_dashboard_title(jsonList):
    for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)
            jsonObject["title"] = "FEWS "+ jsonObject["title"]
            str = json.dumps(jsonObject,indent=4)

        with open(json_file_path,"w") as f:
            f.write(str)

def generate_json_change_panel_title_name(jsonList, panel_type, panel_title, renameTile):
    for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)
            panels = jsonObject["panels"]
            for panel in panels:
                if panel["type"] == panel_type and panel["title"] == panel_title:
                   if panel["type"] == panel_type and panel["title"] == panel_title:
                        panel["title"] =  renameTile
                
                if panel["type"] == "row" and len(panel["panels"]) != 0:
                   for  subpanel in panel["panels"]:
                    if subpanel["type"] == panel_type and subpanel["title"] == panel_title:
                            subpanel["title"] =  renameTile
                                   
        str = json.dumps(jsonObject,indent=4)   

        with open(json_file_path,"w") as f:
            f.write(str)

def generate_json_replace_variable(jsonList, searchString, newString):
     for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            str = context.replace(searchString,newString)
            jsonObject = json.loads(str)
            str = json.dumps(jsonObject,indent=4)

        with open(json_file_path,"w") as f:
            f.write(str)

def generate_json_change_dashboard_templating_variable(jsonList,searchString, newString):
    for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)
            variableList = jsonObject["templating"]["list"]
            for variable in variableList:
                if variable["name"] == searchString:
                    variable["name"] = newString
            
            str = json.dumps(jsonObject,indent=4)

        with open(json_file_path,"w") as f:
            f.write(str)

location_Table_Json = {
      "datasource": {
        "type": "marcusolsson-json-datasource",
        "uid": "P4A126EC1F9644871"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "align": "center",
            "displayMode": "color-text",
            "filterable": False
          },
          "decimals": 5,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 12,
        "x": 12,
        "y": 1
      },
      "id": 33,
      "options": {
        "footer": {
          "fields": "",
          "reducer": [
            "lastNotNull"
          ],
          "show": False
        },
        "showHeader": True
      },
      "pluginVersion": "8.3.1",
      "targets": [
        {
          "cacheDurationSeconds": 300,
          "datasource": {
            "type": "marcusolsson-json-datasource",
            "uid": "P4A126EC1F9644871"
          },
          "fields": [
            {
              "jsonPath": "$.data.PiTimeSeriesArray[*].Header.LocationId",
              "type": "string"
            },
            {
              "jsonPath": "$.data.PiTimeSeriesArray[*].Header.LocationName",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.data.PiTimeSeriesArray[*].Header.X",
              "language": "jsonpath",
              "name": "",
              "type": "number"
            },
            {
              "jsonPath": "$.data.PiTimeSeriesArray[*].Header.Y",
              "language": "jsonpath",
              "name": "",
              "type": "number"
            }
          ],
          "method": "GET",
          "queryParams": "",
          "refId": "A",
          "urlPath": "/api/v1/datasets/observed/timeseries/${locationType}/${dataset}/latest"
        }
      ],
      "title": "Location Table",
      "type": "table"
    }
def generate_json_add_location_table(jsonList):
    for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)
            panels = jsonObject["panels"]
            
            flag = True
            for panel in panels:
                if panel["title"] in ["Location Table","Panel Title"] and panel["type"] == "table":
                    if panel["title"] == "Panel Title":
                        panel["title"] = "Location Table"
                        gridPos = panel["gridPos"]
                        gridPos["h"] = 5
                        gridPos["w"] = 12
                        gridPos["x"] = 12
                        gridPos["y"] = 1 
                    flag = False
                           
            if flag :
                panels.append(location_Table_Json)
            
            str = json.dumps(jsonObject,indent=4)

        with open(json_file_path,"w") as f:
            f.write(str)

def generate_json_delete_response_with_id_panel_in_row_without_id(jsonList):
  for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)

            panels:list = jsonObject["panels"]
            jsonObject["panels"] = list(filter(lambda panel : panel["title"] != "Responses - ${locationId}" , panels))

            new_panels=[]
            for panel in jsonObject["panels"]:
                if panel["type"] == "row":                 
                    if len( panel["panels"]) != 0:
                        panel["panels"] = list(filter(lambda panel : panel["title"] != "Responses - ${locationId}", panel["panels"]))
                new_panels.append(panel) 

            jsonObject["panels"] = new_panels

        str = json.dumps(jsonObject,indent=4)   
        with open(json_file_path,"w") as f:
            f.write(str)  

row_latest_with_id =  {
      "collapsed": True,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 7
      },
      "id": 42,
      "panels": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "description": "",
          "gridPos": {
            "h": 12,
            "w": 12,
            "x": 0,
            "y": 8
          },
          "id": 43,
          "options": {
            "content": "# Curl\n\n```\ncurl -X 'GET' \\\n  'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/latest?locationId={{variable \"locationId\"}}' \\\n  -H 'accept: application/json'\n\n```\n---\n\n# Request URL\n\n```\n\n'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/latest?locationId={{variable \"locationId\"}}' \n\n\n```\n\n--- \n# Code: 401\n### Error: Unauthorized\n### Response headers\n\n```\n\n cache-control: no-cache,no-store,max-age=0,must-revalidate \n connection: keep-alive \n content-length: 0 \n date: Thu,06 Jan 2022 04:16:59 GMT \n expires: 0 \n pragma: no-cache \n server: nginx/1.20.1 \n strict-transport-security: max-age=31536000 ; includeSubDomains \n vary: Origin,Access-Control-Request-Method,Access-Control-Request-Headers \n www-authenticate: Bearer \n x-content-type-options: nosniff \n x-frame-options: DENY \n x-xss-protection: 1\n\n```\n--- \n# Code: 404\n### Error: \t Not found pi-json from dataflow repository.\n\n--- \n# Code: 404\n### Error: \t Not found pi-json with location id",
            "defaultContent": "# Curl\n\n```\ncurl -X 'GET' \\\n  'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/latest?locationId={{variable \"locationId\"}}' \\\n  -H 'accept: application/json'\n\n```\n---\n\n# Request URL\n\n```\n\n'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/latest?locationId={{variable \"locationId\"}}' \n\n\n```\n\n--- \n# Code: 401\n### Error: Unauthorized\n### Response headers\n\n```\n\n cache-control: no-cache,no-store,max-age=0,must-revalidate \n connection: keep-alive \n content-length: 0 \n date: Thu,06 Jan 2022 04:16:59 GMT \n expires: 0 \n pragma: no-cache \n server: nginx/1.20.1 \n strict-transport-security: max-age=31536000 ; includeSubDomains \n vary: Origin,Access-Control-Request-Method,Access-Control-Request-Headers \n www-authenticate: Bearer \n x-content-type-options: nosniff \n x-frame-options: DENY \n x-xss-protection: 1\n\n```\n--- \n# Code: 404\n### Error: \t Not found pi-json from dataflow repository.\n\n--- \n# Code: 404\n### Error: \t Not found pi-json with location id"
          },
          "targets": [
            {
              "channel": "plugin/testdata/random-flakey-stream",
              "datasource": {
                "type": "datasource",
                "uid": "grafana"
              },
              "filter": {
                "fields": [
                  "Time",
                  "Value"
                ]
              },
              "queryType": "measurements",
              "refId": "A"
            }
          ],
          "title": "Example Request",
          "transformations": [
            {
              "id": "reduce",
              "options": {}
            }
          ],
          "transparent": True,
          "type": "marcusolsson-dynamictext-panel"
        },
        {
          "datasource": {
            "type": "marcusolsson-json-datasource",
            "uid": "P4A126EC1F9644871"
          },
          "gridPos": {
            "h": 12,
            "w": 12,
            "x": 12,
            "y": 8
          },
          "id": 38,
          "options": {
            "seriesCountSize": "sm",
            "showSeriesCount": False,
            "text": "${locationId}"
          },
          "targets": [
            {
              "cacheDurationSeconds": 300,
              "datasource": {
                "type": "marcusolsson-json-datasource",
                "uid": "P4A126EC1F9644871"
              },
              "fields": [
                {
                  "jsonPath": "$"
                }
              ],
              "method": "GET",
              "params": [
                [
                  "locationId",
                  "${locationId}"
                ]
              ],
              "queryParams": "",
              "refId": "A",
              "urlPath": "/api/v1/datasets/observed/timeseries/${locationType}/${dataset}/latest"
            }
          ],
          "title": "API Response Query with ${locationId}",
          "transparent": True,
          "type": "fondus-jsontext-panel"
        }
      ],
      "title": "latest with location",
      "type": "row"
    }
row_timezero_with_range_id = {
      "collapsed": True,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 9
      },
      "id": 45,
      "panels": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "gridPos": {
            "h": 12,
            "w": 12,
            "x": 0,
            "y": 10
          },
          "id": 48,
          "options": {
            "content": "# Curl\n\n```\n\ncurl -X 'GET' \\\n  'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero?from={{variable \"from\"}}&to={{variable \"to\"}}&locationId={{variable \"locationId\"}}' \\\n  -H 'accept: application/json'\n\n```\n---\n\n# Request URL\n\n```\n\n'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero?from={{variable \"from\"}}&to={{variable \"to\"}}&locationId={{variable \"locationId\"}}'\n\n```\n\n\n---\n# Code: 401\n### Error: Unauthorized\n### Response headers\n\n```\n\n cache-control: no-cache,no-store,max-age=0,must-revalidate \n connection: keep-alive \n content-length: 0 \n date: Thu,06 Jan 2022 04:16:59 GMT \n expires: 0 \n pragma: no-cache \n server: nginx/1.20.1 \n strict-transport-security: max-age=31536000 ; includeSubDomains \n vary: Origin,Access-Control-Request-Method,Access-Control-Request-Headers \n www-authenticate: Bearer \n x-content-type-options: nosniff \n x-frame-options: DENY \n x-xss-protection: 1\n\n```\n---\n# Code: 404\n### Error: \t Not found pi-json from dataflow repository.\n\n--- \n# Code: 404\n### Error: \t Not found pi-json with location id",
            "defaultContent": "# Curl\n\n```\n\ncurl -X 'GET' \\\n  'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero?from={{variable \"from\"}}&to={{variable \"to\"}}&locationId={{variable \"locationId\"}}' \\\n  -H 'accept: application/json'\n\n```\n---\n\n# Request URL\n\n```\n\n'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero?from={{variable \"from\"}}&to={{variable \"to\"}}&locationId={{variable \"locationId\"}}'\n\n```\n\n\n---\n# Code: 401\n### Error: Unauthorized\n### Response headers\n\n```\n\n cache-control: no-cache,no-store,max-age=0,must-revalidate \n connection: keep-alive \n content-length: 0 \n date: Thu,06 Jan 2022 04:16:59 GMT \n expires: 0 \n pragma: no-cache \n server: nginx/1.20.1 \n strict-transport-security: max-age=31536000 ; includeSubDomains \n vary: Origin,Access-Control-Request-Method,Access-Control-Request-Headers \n www-authenticate: Bearer \n x-content-type-options: nosniff \n x-frame-options: DENY \n x-xss-protection: 1\n\n```\n---\n# Code: 404\n### Error: \t Not found pi-json from dataflow repository.\n\n--- \n# Code: 404\n### Error: \t Not found pi-json with location id"
          },
          "targets": [
            {
              "channel": "plugin/testdata/random-flakey-stream",
              "datasource": {
                "type": "datasource",
                "uid": "grafana"
              },
              "filter": {
                "fields": [
                  "Time",
                  "Value"
                ]
              },
              "queryType": "measurements",
              "refId": "A"
            }
          ],
          "title": "Example Request",
          "transformations": [
            {
              "id": "reduce",
              "options": {}
            }
          ],
          "transparent": True,
          "type": "marcusolsson-dynamictext-panel"
        },
        {
          "datasource": {
            "type": "marcusolsson-json-datasource",
            "uid": "P4A126EC1F9644871"
          },
          "gridPos": {
            "h": 12,
            "w": 12,
            "x": 12,
            "y": 10
          },
          "id": 39,
          "options": {
            "seriesCountSize": "sm",
            "showSeriesCount": False,
            "text": "Default value of text input option"
          },
          "targets": [
            {
              "cacheDurationSeconds": 300,
              "datasource": {
                "type": "marcusolsson-json-datasource",
                "uid": "P4A126EC1F9644871"
              },
              "fields": [
                {
                  "jsonPath": "$"
                }
              ],
              "method": "GET",
              "params": [
                [
                  "locationId",
                  "${locationId}"
                ],
                [
                  "from",
                  "${from}"
                ],
                [
                  "to",
                  "${to}"
                ]
              ],
              "queryParams": "",
              "refId": "A",
              "urlPath": "/api/v1/datasets/observed/timeseries/${locationType}/${dataset}/time-zero"
            }
          ],
          "title": "API Response Query with ${locationId}",
          "transparent": True,
          "type": "fondus-jsontext-panel"
        }
      ],
      "title": "time-zero with range and location",
      "type": "row"
    }
row_timezero_with_id = {
      "collapsed": True,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 11
      },
      "id": 47,
      "panels": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "gridPos": {
            "h": 12,
            "w": 12,
            "x": 0,
            "y": 12
          },
          "id": 49,
          "options": {
            "content": "# Curl\n\n```\n\ncurl -X 'GET' \\\n  'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero/{{variable \"from\"}}?locationId={{variable \"locationId\"}}' \\\n  -H 'accept: application/json'\n\n```\n---\n\n# Request URL\n\n```\n\n'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero/{{variable \"from\"}}?locationId={{variable \"locationId\"}}' \n\n```\n\n---\n# Code: 401\n### Error: Unauthorized\n### Response headers\n\n```\n\n cache-control: no-cache,no-store,max-age=0,must-revalidate \n connection: keep-alive \n content-length: 0 \n date: Thu,06 Jan 2022 04:16:59 GMT \n expires: 0 \n pragma: no-cache \n server: nginx/1.20.1 \n strict-transport-security: max-age=31536000 ; includeSubDomains \n vary: Origin,Access-Control-Request-Method,Access-Control-Request-Headers \n www-authenticate: Bearer \n x-content-type-options: nosniff \n x-frame-options: DENY \n x-xss-protection: 1\n\n```\n---\n# Code: 404\n### Error: \t Not found pi-json from dataflow repository.\n\n--- \n# Code: 404\n### Error: \t Not found pi-json with location id",
            "defaultContent": "# Curl\n\n```\n\ncurl -X 'GET' \\\n  'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero/{{variable \"from\"}}?locationId={{variable \"locationId\"}}' \\\n  -H 'accept: application/json'\n\n```\n---\n\n# Request URL\n\n```\n\n'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/observed/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero/{{variable \"from\"}}?locationId={{variable \"locationId\"}}' \n\n```\n\n---\n# Code: 401\n### Error: Unauthorized\n### Response headers\n\n```\n\n cache-control: no-cache,no-store,max-age=0,must-revalidate \n connection: keep-alive \n content-length: 0 \n date: Thu,06 Jan 2022 04:16:59 GMT \n expires: 0 \n pragma: no-cache \n server: nginx/1.20.1 \n strict-transport-security: max-age=31536000 ; includeSubDomains \n vary: Origin,Access-Control-Request-Method,Access-Control-Request-Headers \n www-authenticate: Bearer \n x-content-type-options: nosniff \n x-frame-options: DENY \n x-xss-protection: 1\n\n```\n---\n# Code: 404\n### Error: \t Not found pi-json from dataflow repository.\n\n--- \n# Code: 404\n### Error: \t Not found pi-json with location id"
          },
          "targets": [
            {
              "channel": "plugin/testdata/random-flakey-stream",
              "datasource": {
                "type": "datasource",
                "uid": "grafana"
              },
              "filter": {
                "fields": [
                  "Time",
                  "Value"
                ]
              },
              "queryType": "measurements",
              "refId": "A"
            }
          ],
          "title": "Example Request",
          "transformations": [
            {
              "id": "reduce",
              "options": {}
            }
          ],
          "transparent": True,
          "type": "marcusolsson-dynamictext-panel"
        },
        {
          "datasource": {
            "type": "marcusolsson-json-datasource",
            "uid": "P4A126EC1F9644871"
          },
          "gridPos": {
            "h": 12,
            "w": 12,
            "x": 12,
            "y": 12
          },
          "id": 40,
          "options": {
            "seriesCountSize": "sm",
            "showSeriesCount": False,
            "text": "Default value of text input option"
          },
          "targets": [
            {
              "cacheDurationSeconds": 300,
              "datasource": {
                "type": "marcusolsson-json-datasource",
                "uid": "P4A126EC1F9644871"
              },
              "fields": [
                {
                  "jsonPath": "$"
                }
              ],
              "method": "GET",
              "params": [
                [
                  "locationId",
                  "${locationId}"
                ]
              ],
              "queryParams": "",
              "refId": "A",
              "urlPath": "/api/v1/datasets/observed/timeseries/${locationType}/${dataset}/time-zero/${from}"
            }
          ],
          "title": "API Response Query with ${locationId}",
          "transparent": True,
          "type": "fondus-jsontext-panel"
        }
      ],
      "title": "time-zero with location",
      "type": "row"
    }
def generate_json_add_rows(jsonList):
    for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)
            panels = jsonObject["panels"]
            panels.append(row_latest_with_id )
            panels.append(row_timezero_with_range_id)
            panels.append(row_timezero_with_id)
                     
        str = json.dumps(jsonObject,indent=4)   
        with open(json_file_path,"w") as f:
            f.write(str)

def generate_json_adjust_all_dashboard(jsonList):
  for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)
            panels = jsonObject["panels"]
            for panel in panels:
              if panel["title"] == "Metadata" and panel["type"] == "text":
                gridPos = panel["gridPos"]
                gridPos["h"] = 5
                gridPos["w"] = 11
                gridPos["x"] = 0
                gridPos["y"] = 1
                continue
              if panel["title"] == "Location Table" and panel["type"] == "table":
                gridPos = panel["gridPos"]
                gridPos["h"] = 5
                gridPos["w"] = 11
                gridPos["x"] = 12
                gridPos["y"] = 1
                continue

              if panel["title"] == "latest" and panel["type"] == "row":
                modify_panel_layout(panel)
                continue

              if panel["title"] == "latest with location" and panel["type"] == "row":
                modify_panel_layout(panel)
                continue

              if panel["title"] == "time-zero with range" and panel["type"] == "row":
                modify_panel_layout(panel)
                continue

              if panel["title"] == "time-zero with range and location" and panel["type"] == "row":
                modify_panel_layout(panel)
                continue

              if panel["title"] == "time-zero" and panel["type"] == "row":
                modify_panel_layout(panel)
                continue

              if panel["title"] == "time-zero with location" and panel["type"] == "row":
                modify_panel_layout(panel)
                continue
              
                                        
        str = json.dumps(jsonObject,indent=4)   
        with open(json_file_path,"w") as f:
            f.write(str)
def modify_panel_layout(panel):
  subpanel1 = panel["panels"][0]
  subpanel2 = panel["panels"][1]

  gridPos1 = subpanel1["gridPos"]
  gridPos1["h"] = 12
  gridPos1["w"] = 11
  gridPos1["x"] = 0

  gridPos2 = subpanel2["gridPos"]
  gridPos2["h"] = 12
  gridPos2["w"] = 11
  gridPos2["x"] = 12
  gridPos2["y"] = gridPos1["y"]

time_zero = [{
                    "datasource": {
                        "type": "datasource",
                        "uid": "grafana"
                    },
                    "gridPos": {
                        "h": 12,
                        "w": 11,
                        "x": 0,
                        "y": 11
                    },
                    "id": 31,
                    "options": {
                        "content": "# Curl\n\n```\n\ncurl -X 'GET' \\\n  'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/simulated/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero/{{variable \"from\"}}' \\\n  -H 'accept: application/json'\n\n```\n---\n\n# Request URL\n\n```\n\n'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/simulated/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero/{{variable \"from\"}}'\n\n```\n\n---\n# Code: 401\n### Error: Unauthorized\n### Response headers\n\n```\n\n cache-control: no-cache,no-store,max-age=0,must-revalidate \n connection: keep-alive \n content-length: 0 \n date: Thu,06 Jan 2022 04:16:59 GMT \n expires: 0 \n pragma: no-cache \n server: nginx/1.20.1 \n strict-transport-security: max-age=31536000 ; includeSubDomains \n vary: Origin,Access-Control-Request-Method,Access-Control-Request-Headers \n www-authenticate: Bearer \n x-content-type-options: nosniff \n x-frame-options: DENY \n x-xss-protection: 1\n\n```\n---\n# Code: 404\n### Error: \t Not found pi-json from dataflow repository.\n\n--- \n# Code: 404\n### Error: \t Not found pi-json with location id",
                        "defaultContent": "# Curl\n\n```\n\ncurl -X 'GET' \\\n  'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/simulated/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero/{{variable \"from\"}}' \\\n  -H 'accept: application/json'\n\n```\n---\n\n# Request URL\n\n```\n\n'https://gateway.fondus.com.tw/fewstaiwan-dataflow-dataset-service/api/v1/datasets/simulated/timeseries/{{variable \"locationType\"}}/{{variable \"dataset\"}}/time-zero/{{variable \"from\"}}'\n\n```\n\n---\n# Code: 401\n### Error: Unauthorized\n### Response headers\n\n```\n\n cache-control: no-cache,no-store,max-age=0,must-revalidate \n connection: keep-alive \n content-length: 0 \n date: Thu,06 Jan 2022 04:16:59 GMT \n expires: 0 \n pragma: no-cache \n server: nginx/1.20.1 \n strict-transport-security: max-age=31536000 ; includeSubDomains \n vary: Origin,Access-Control-Request-Method,Access-Control-Request-Headers \n www-authenticate: Bearer \n x-content-type-options: nosniff \n x-frame-options: DENY \n x-xss-protection: 1\n\n```\n---\n# Code: 404\n### Error: \t Not found pi-json from dataflow repository.\n\n--- \n# Code: 404\n### Error: \t Not found pi-json with location id"
                    },
                    "targets": [
                        {
                            "channel": "plugin/testdata/random-flakey-stream",
                            "datasource": {
                                "type": "datasource",
                                "uid": "grafana"
                            },
                            "filter": {
                                "fields": [
                                    "Time",
                                    "Value"
                                ]
                            },
                            "queryType": "measurements",
                            "refId": "A"
                        }
                    ],
                    "title": "Example Request",
                    "transformations": [
                        {
                            "id": "reduce",
                            "options": {}
                        }
                    ],
                    "transparent": True,
                    "type": "marcusolsson-dynamictext-panel"
                },
                {
                    "datasource": {
                        "type": "marcusolsson-json-datasource",
                        "uid": "P4A126EC1F9644871"
                    },
                    "gridPos": {
                        "h": 12,
                        "w": 11,
                        "x": 12,
                        "y": 11
                    },
                    "id": 37,
                    "options": {
                        "seriesCountSize": "sm",
                        "showSeriesCount": False,
                        "text": "Default value of text input option"
                    },
                    "targets": [
                        {
                            "cacheDurationSeconds": 300,
                            "datasource": {
                                "type": "marcusolsson-json-datasource",
                                "uid": "P4A126EC1F9644871"
                            },
                            "fields": [
                                {
                                    "jsonPath": "$"
                                }
                            ],
                            "method": "GET",
                            "params": [],
                            "queryParams": "",
                            "refId": "A",
                            "urlPath": "/api/v1/datasets/simulated/timeseries/${locationType}/${dataset}/time-zero/${from}"
                        }
                    ],
                    "title": " API Response",
                    "transparent": True,
                    "type": "fondus-jsontext-panel"
                }]
def generate_json_adjust_timezero(jsonList):
  for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)


            panels = jsonObject["panels"]
            for panel in panels:
              if panel["title"] == "time-zero" and panel["type"] == "row":
                panel["panels"] = time_zero
                continue

            str = json.dumps(jsonObject,indent=4)   

        with open(json_file_path,"w") as f:
            f.write(str)




def generate_json_change_fill_screen(jsonList):
    for json_file_path in jsonList:
       
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)
            panels = jsonObject["panels"]
            for panel in panels:
                if panel["type"] == "text" and panel["title"] == "Metadata":
                    gridPos = panel["gridPos"]
                    gridPos["h"] = 5
                    gridPos["w"] = 12
                    gridPos["x"] = 0
                    gridPos["y"] = 1
                if panel["type"] == "text" and panel["title"] == "Location Table":
                    gridPos = panel["gridPos"]
                    gridPos["h"] = 5
                    gridPos["w"] = 12
                    gridPos["x"] = 12
                    gridPos["y"] = 1
            
            for panel in panels:
                if panel["type"] == "row":
                    if len(panel["panels"]) != 0:
                        i=1
                        for sub_panel in panel["panels"]:
                            gridPos = sub_panel["gridPos"]
                            gridPos["x"] = 12 * (i-1)
                            gridPos["w"] = 12 * i   
                
            str = json.dumps(jsonObject,indent=4)   
        with open(json_file_path,"w") as f:
            f.write(str)
##############################################################

path = 'D:\workspace\Grafana-Dashboard-Config\Operation\provisioning\dashboards\swagger\simulated'
jsonList =load_all_files(path)
#generate_identity_json(jsonList)
#generate_json_change_dashboard_title(jsonList)
#generate_json_change_panel_title_name(jsonList, "marcusolsson-dynamictext-panel", "URL PATH", "Example Request")
#generate_json_change_panel_title_name(jsonList, "fondus-jsontext-panel", "Responses", "API Response")

# generate_json_change_dashboard_templating_variable(jsonList,"dataSet", "locationType")
# generate_json_replace_variable(jsonList, "${dataSet}", "${locationType}")
# generate_json_replace_variable(jsonList, "{{variable \"dataSet\"}}", "${{variable \"locationType\"}}")

# generate_json_change_dashboard_templating_variable(jsonList,"dataMode", "dataset")
# generate_json_replace_variable(jsonList, "${dataMode}", "${dataset}")
# generate_json_replace_variable(jsonList, "{{variable \"dataMode\"}}", "${{variable \"dataset\"}}")

#generate_json_change_panel_title_name(jsonList, "table", "LocationId List", "Location Table")
#generate_json_add_location_table(jsonList)

#generate_json_delete_response_with_id_panel_in_row_without_id(jsonList)

#generate_json_add_rows(jsonList)

#generate_json_change_fill_screen(jsonList)

#generate_json_adjust_all_dashboard(jsonList)
generate_json_adjust_timezero(jsonList)










def generate_json_change_path_to_simulated(jsonList):
    for json_file_path in jsonList:
        str = None
        with open(json_file_path) as f:
            context = f.read()
            jsonObject = json.loads(context)
            panels = jsonObject["panels"] 
            for panel in panels:
              if panel["title"] == "Location Table":

                if "features" in panel["targets"][0]["urlPath"]:
                  continue
                else:
                  panel["targets"][0]["urlPath"] = "/api/v1/datasets/simulated/timeseries/${locationType}/${dataset}/latest" 

            str = json.dumps(jsonObject,indent=4)

        with open(json_file_path,"w") as f:
            f.write(str)



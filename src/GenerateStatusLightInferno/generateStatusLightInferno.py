import json

__author__ = 'philipp'

statusLightWidth=116
statusLightHeight=96

statusLightGroups=5
statusLightsColumns=2
statusLightsRows=3

startXCoordinate=0
startYCoordinate=20

statusLightJsonDict = {
    "schemaVersion": None,
    "dashboardFormatVersion": "3.0",
    "name": "Alternative Gesamtdashboard Audi WebCenter",
    "description": None,
    "properties": None,
    "templateEntityType": "APPLICATION_COMPONENT_NODE",
    "associatedEntityTemplates": None,
    "minutesBeforeAnchorTime": 15,
    "startDate": None,
    "endDate": None,
    "refreshInterval": 120000,
    "backgroundColor": 16777215,
    "color": 16777215,
    "height": 1000,
    "width": 1600,
    "canvasType": "CANVAS_TYPE_ABSOLUTE",
    "layoutType": "",
    "template": False,
    "warRoom": False
}

widgetTemplatesDict = []

widgetTemplateDict = {
    "widgetType": "StatusLightWidget",
    "title": None,
    "height": statusLightHeight,
    "width": statusLightWidth,
    # "x": 116,
    # "y": 41,
    "label": None,
    "description": "Connect Frontend",
    "drillDownUrl": None,
    "useMetricBrowserAsDrillDown": False,
    "backgroundColor": 16777215,
    "backgroundColors": None,
    "backgroundColorsStr": "16777215,16777215",
    "color": 4210752,
    "fontSize": 12,
    "useAutomaticFontSize": False,
    "borderEnabled": True,
    "borderThickness": 3,
    "borderColor": 14408667,
    "backgroundAlpha": 1,
    "showValues": False,
    "compactMode": False,
    "showTimeRange": False,
    "renderIn3D": False,
    "showLegend": None,
    "legendPosition": None,
    "legendColumnCount": None,
    "startTime": None,
    "endTime": None,
    "minutesBeforeAnchorTime": 15,
    "isGlobal": True,
    "propertiesMap": None,
    "dataSeriesTemplates": None,
    "healthRule": {
        "applicationName": "myAudi-All",
        "entityType": "POLICY",
        "entityName": "Gruene Ampel",
        "scopingEntityType": None,
        "scopingEntityName": None,
        "subtype": None
    }
}

def createStatusLight(xcord, ycord):
    statusLight = widgetTemplateDict.copy()
    statusLight["x"] = xcord
    statusLight["y"] = ycord
    return statusLight


groupCounter = 1
columnCounter = 1
rowCounter = 1
while(groupCounter <= statusLightGroups):
    while(rowCounter <= statusLightsRows):
        while(columnCounter <= statusLightsColumns):
            statusLight = widgetTemplateDict.copy()
            statusLight["x"] = startXCoordinate
            statusLight["y"] = startYCoordinate
            widgetTemplatesDict.append(statusLight)
            startXCoordinate = startXCoordinate + statusLightWidth
            columnCounter = columnCounter + 1
            print("Column added")
        columnCounter = 1
        startXCoordinate = groupCounter * columnCounter * statusLightWidth
        startYCoordinate = rowCounter * statusLightHeight
        rowCounter = rowCounter + 1
        print("Row added")
    columnCounter = 1
    rowCounter = 1
    startXCoordinate = (groupCounter * columnCounter * statusLightWidth) + 10
    startYCoordinate = rowCounter * statusLightHeight
    groupCounter = groupCounter + 1
    print("Group added")

# widgetTemplatesDict.append(widgetTemplateDict)
statusLightJsonDict["widgetTemplates"]= widgetTemplatesDict

jsonExportFile = open("out.json", 'w')
jsonExportFile.truncate()
jsonExportFile.write(json.dumps(statusLightJsonDict))
jsonExportFile.close()






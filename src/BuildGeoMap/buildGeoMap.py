#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'philipp'

# import requests
import json
import random
import urllib2, base64
from datetime import datetime

schema = "http"
server= "ivwb3559.app-audi-connect-pro.web.audi.vwg"
port = "8090"
user = "mssc.rest.geo@customer1"
password = "msscRestGeo123"
appId = "28"
# metricPath = "End%20User%20Experience%7CGeo%7C*%7CDevice%7CComputer%7CMac%7CRequests%20per%20Minute"
metricPath = "End%20User%20Experience%7CGeo%7C*%7CDevice%7C*%7C*%7CRequests%20per%20Minute"
lastNMinutes = "5"
restUrl = "/controller/rest/applications/" + appId + "/metric-data?metric-path=" + metricPath + "&time-range-type=BEFORE_NOW&duration-in-mins=" + lastNMinutes + "&output=json"

countryMappingDict = {
    'Germany': ['Deutschland', 50.9364885, 10.5266941],
    'United States': ['USA', 37.6675588, -105.2030111],
    'France': ['Frankreich', 46.9178939,4.1507705],
    'Belgium': ['Belgien', 50.382346,4.8169483],
    'Netherlands': ['Niederlande', 52.258322,5.9819079],
    'Spain': ['Spanien', 40.1848038,-3.706497],
    'Unknown': ['Unbekannt', -57.618702, -141.8951343],
    'Canada': ['Kanada', 57.4276036,-108.7608533],
    'Norway': ['Norwegen', 61.3603913,8.0190606],
    'Switzerland': ['Schweiz', 46.2571631,7.998808],
    'Luxembourg': ['Luxemburg', 49.7859308,5.9970005],
    'Liechtenstein': ['Liechtenstein', 48.425124,9.2509814],
    'Portugal': ['Portugal', 39.7037262,-8.6996738],
    'Romania': ['Rumanien', 46.0005274,23.9948161],
    'Turkey': ['Turkei', 39.4120815,32.3742999],
    'Australia': ['Australien', -25.1551766,129.2306915],
    'Russian Federation': ['Russland', 56.265505,67.7045531],
    'China': ['China', 36.0544428,92.4967605],
    'Slovenia': ['Slovenia', 45.9823937,14.7979175],
    'Italy': ['Italien', 42.3960214,12.6382289],
    'Sweden': ['Schweden', 60.320368,15.6346037],
    'United Kingdom': ['Grossbritannien', 52.4856558,-1.2697902],
    'Brazil': ['Brasilien', -14.7244456,-47.6909171]
}

mapTemplate = "MSSCGeoMap.html.template"
mapOutputFile = "MSSCGeoMap.html"

def getMetrcs():
    # url = schema + "://" + user + ":" + password + "@" + server + ":" + port + restUrl
    # r = requests.get(url)
    # response = r.text
    url = schema + "://" + server + ":" + port + restUrl
    request = urllib2.Request(url.encode("utf-8"))
    base64string = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    r = urllib2.urlopen(request)
    response = r.read()
    return json.loads(response)

timestamp = datetime.now()

json = getMetrcs()
javaScriptString = "var locations = ["
unknownCountries = 0
for metric in json:
    metricName = metric["metricName"]
    if "iOS - iPad" in metricName:
        metricNameArray = metricName.split("|")
        country = metricNameArray[2]
        metricValue = metric["metricValues"][0]["sum"]
        # metricValue = random.randint(1, 20)
        if country in countryMappingDict:
            countryDisplayName = countryMappingDict[country][0]
            latitude = countryMappingDict[country][1]
            longitude = countryMappingDict[country][2]
        else:
            unknownCountries += 1
            countryDisplayName = country
            latitude = countryMappingDict['Unknown'][1]
            longitude = countryMappingDict['Unknown'][2]
            if unknownCountries > 0:
                longitude += unknownCountries * 7
        # print("Country="+str(countryDisplayName)+",metricValue="+str(metricValue))
        javaScriptString = javaScriptString + "['" + str(countryDisplayName) + "'," + str(latitude) + "," + str(longitude) + ", '" + str(metricValue) + "'],"
javaScriptString = javaScriptString + "];"
# print(javaScriptString)

filedata = None
with open(mapTemplate, 'r') as file:
    filedata = file.read()
filedata = filedata.replace('%%LOCATIONS%%', javaScriptString)
filedata = filedata.replace('%%TIMESTAMP%%', timestamp.strftime('%d.%m.%Y, %H:%M:%S'))

with open(mapOutputFile, 'w') as file:
    file.write(filedata)
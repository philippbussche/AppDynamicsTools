__author__ = 'philipp'

import requests
import json

class ControllerHandler:

    def __init__(self, schema, server, port, jsessionid, testmode):
        self.schema = schema
        self.server = server
        self.port = port
        self.jsessionid = jsessionid
        self.testmode = testmode

    urls = {
        'getEumPageList': '/controller/restui/pageList/getEumPageList',
        'renameRequest':  '/controller/restui/pageList/renameRequest',
        'getAnalyticsScheduledQueryReports': '/controller/restui/analyticsMetric/getAnalyticsScheduledQueryReports',
        'createAnalyticsMetric': '/controller/restui/analyticsMetric/create'
    }

    def getAnalyticsScheduledQueryReports(self):
        headers = {
            'Accept': 'application/json'
        }
        cookies = {
            'JSESSIONID': self.jsessionid
        }
        r = requests.get(self.schema + "://" + self.server + ":" + self.port + self.urls['getAnalyticsScheduledQueryReports'],  headers=headers, cookies=cookies)
        response = r.text
        return json.loads(response)

    def createNewAnalyticsMetric(self, name, queryField, queryValue, parentName, parentDescription):
        print "------> Creating new analytics metric: " + name
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=UTF-8'
        }
        cookies = {
             'JSESSIONID': self.jsessionid
        }
        # cookies = {
        #     'JSESSIONID': 'c72e94dc40009b458477c2080c01'
        # }
        payload = {
            "adqlQueryString": "SELECT count(*) FROM logs",
            "eventType": "LOG",
            "enabled": 'true',
            "queryType": "ADQL_QUERY",
            "queryName": "SIMPLE_COUNT2_USER5",
            "queryDescription": "Copied metric from " + parentName + ". Description of parent metric was: " + parentDescription
        }
        payload[queryField] = queryValue
        payload['queryName'] = name
        # print payload
        r = requests.post(self.schema + "://" + self.server + ":" + self.port + self.urls['createAnalyticsMetric'], data=json.dumps(payload), headers=headers, cookies=cookies)
        # r = requests.post('http://docker-machine:8090' + self.urls['createAnalyticsMetric'], data=json.dumps(payload), headers=headers, cookies=cookies)
        response = r.text
        # print response
        # return json.loads(response)
        print "--------> Metric created."
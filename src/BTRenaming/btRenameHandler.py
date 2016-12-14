__author__ = 'philipp'

import requests
import json

class BTRenameHandler:

    def __init__(self, schema, server, port, jsessionid):
        self.schema = schema
        self.server = server
        self.port = port
        self.jsessionid = jsessionid

    urls = {
        'getBTPageList': '/controller/restui/bt/listViewData',
        'renameBT': '/controller/restui/bt/renameBT'
    }

    def getBTPageList(self, application):
        payload = "{\"timeRangeString\": \"last_15_minutes|BEFORE_NOW|-1|-1|15\"}"
        cookies = {
            'JSESSIONID': self.jsessionid
        }
        r = requests.get(self.schema + "://" + self.server + ":" + self.port + self.urls['getBTPageList'] + "/" + application,  params=payload, cookies=cookies)
        response = r.text
        return json.loads(response)

    def renameBT(self, id, newName):
        parameters = { 'id': id }
        payload = newName
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        cookies = {
            'JSESSIONID': self.jsessionid
        }
        r = requests.post(self.schema + "://" + self.server + ":" + self.port + self.urls['renameBT'], params=parameters,data=payload,cookies=cookies, headers=headers)
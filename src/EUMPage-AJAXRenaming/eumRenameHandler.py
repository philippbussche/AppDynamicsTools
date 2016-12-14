__author__ = 'philipp'

import requests
import json

class EUMRenameHandler:

    def __init__(self, schema, server, port, jsessionid, testmode):
        self.schema = schema
        self.server = server
        self.port = port
        self.jsessionid = jsessionid
        self.testmode = testmode

    urls = {
        'getEumPageList': '/controller/restui/pageList/getEumPageList',
        'renameRequest':  '/controller/restui/pageList/renameRequest'
    }

    def getEUMPageList(self, application):
        payload = "{\"applicationId\": " + application + ",\"addId\": null,\"timeRangeString\": \"last_15_minutes|BEFORE_NOW|-1|-1|15\"}"
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        cookies = {
            'JSESSIONID': self.jsessionid
        }
        r = requests.post(self.schema + "://" + self.server + ":" + self.port + self.urls['getEumPageList'],  data=payload, headers=headers, cookies=cookies)
        response = r.text
        return json.loads(response)

    def renamePage(self, id, newName):
        if(self.testmode is False):
            cookies = {
                'JSESSIONID': self.jsessionid
            }
            requests.post(self.schema + "://" + self.server + ":" + self.port + self.urls['renameRequest'] + "/" + str(id) + "/" + newName, cookies=cookies)
        else:
            print "Did not actually rename to " + newName + " since this is just a test."
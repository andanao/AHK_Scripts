import requests
import json
import pprint
import calendar
# import pandas as pd
from datetime import datetime 
from toggl.TogglPy import Toggl #god i love python

toggl = Toggl()
token = "089c874aefeb3e6a4d655c73819949be"
toggl.setAPIKey(token)

def stopRunningEntry():
    toggl.stopTimeEntry(toggl.currentRunningTimeEntry()['data']['id'])

response = toggl.request("https://www.toggl.com/api/v8/clients")

# print the client name and id for each client in the response
# list of returned values can be found in the Toggl docs:
# https://github.com/toggl/toggl_api_docs/blob/master/chapters/clients.md


Projects = {}
for client in response:
    # print("Client name: %s  Client id: %s" % (client['name'], client['id']))
    temp = toggl.getClientProjects(id=client['id'])
    for proj in temp:
        Projects[proj['name']] = proj
        # print("%s \t%s \t%s" % (proj['name'],client['name'],proj['id']))


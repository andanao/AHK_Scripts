import requests
import json
import pprint
import calendar
# import pandas as pd
from datetime import datetime 
from toggl.TogglPy import Toggl as togglpy#god i love python

class Toggl(togglpy):
    toggl = togglpy()
    token = "089c874aefeb3e6a4d655c73819949be"
    toggl.setAPIKey(token)
    Projects = {}
    def __init__(self):
        self.getAllProjects()

    def stopRunningEntry(self):
        self.stopTimeEntry(self.currentRunningTimeEntry()['data']['id'])

    def getAllProjects(self):
        response = self.request("https://www.toggl.com/api/v8/clients")
        for client in response:
            # print("Client name: %s  Client id: %s" % (client['name'], client['id']))
            temp = self.getClientProjects(id=client['id'])
            for proj in temp:
                self.Projects[proj['name']] = proj
                # print("%s \t%s \t%s" % (proj['name'],client['name'],proj['id']))

    def startEntryFromProjectsList(self,input,Shortcuts):
        self.startTimeEntry("Testing Toggl Launcher",self.Projects[input]["id"])
        print("Time entry started for:\n %s" % (input))


    def undoRecentTime(self,time):
        proj = self.currentRunningTimeEntry()['data']
        pprint.pprint(proj,width =2)
        # toggl.createTimeEntry()



toggl = Toggl()
# pprint.pprint(toggl.Projects,width =2)
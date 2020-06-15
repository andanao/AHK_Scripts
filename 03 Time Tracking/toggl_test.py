import requests
import json
import pprint
import calendar
# import pandas as pd
from datetime import datetime 
from toggl.TogglPy import Toggl as togglpy#god i love python
from toggl.TogglPy import Endpoints
from difflib import get_close_matches

class Toggl(togglpy):
    Projects = {}
    def __init__(self,APIKey):
        self.setAPIKey(APIKey)
        # self.getAllProjects()\
        self.loadShortcutsFile('shortcuts.json')

    def loadShortcutsFile(self,dir):
        try:
            with open(dir, encoding ='utf-8') as f:
                self.shortcuts = json.load(f)
        except NotADirectoryError:
            print("file not found")

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

    def editTimeEntry(self):
        print("TODO")

    def undoRecentTime(self,time):
        # proj = self.currentRunningTimeEntry()['data']
        # time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
        # excuse = "Lost focus and started doing other shit"
        # pprint.pprint(proj,width =2)
        # toggl.createTimeEntry()
        print("NotImplemented")

    def updateTimeEntry(self,parameters):
        print("TODO")

    def useShortcut(self,input):
        name =  get_close_matches(input,self.shortcuts,n=1)[0]
        entry = self.shortcuts[name]
        # print(entry)
        
        if entry['command'] == 'start_entry':
            self.startTimeEntry(entry['desc'],entry['id'])
            print('Starting entry:\n\t',entry['desc'])

        elif entry['command'] == 'ask_entry':
            desc = name #entry['desc']# + input("Enter Description:")
            self.startTimeEntry(desc,entry['id'])
            print('Starting entry:\n\t',desc)

        elif entry['command'] == 'stop_entry':
            self.stopRunningEntry()
        

token = "089c874aefeb3e6a4d655c73819949be"
toggl = Toggl(token)

from json import load
from toggl.TogglPy import Toggl as togglpy#god i love python
from toggl.TogglPy import Endpoints
from difflib import get_close_matches

class Toggl(togglpy):
    Projects = {}
    def __init__(self,APIKey):
        self.setAPIKey(APIKey)
        # self.getAllProjects()\
        self.shortcuts_dir='shortcuts.json'
        self.loadShortcutsFile()

    def loadShortcutsFile(self):
        try:
            with open(self.shortcuts_dir, encoding ='utf-8') as f:
                self.shortcuts = load(f)
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

    def useShortcut(self,input):
        try:
            name =  get_close_matches(input,self.shortcuts,n=1)[0]
        except:
            print('No entry found')

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

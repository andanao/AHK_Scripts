from difflib import get_close_matches
from json import load
from toggl.TogglPy import Toggl as togglpy#god i love python
from toggl.TogglPy import Endpoints
from tkinter import *
from tkinter import ttk, filedialog
from datetime import datetime

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
        return self.stopTimeEntry(self.currentRunningTimeEntry()['data']['id'])

    def getAllProjects(self):
        response = self.request("https://www.toggl.com/api/v8/clients")
        for client in response:
            temp = self.getClientProjects(id=client['id'])
            for proj in temp:
                self.Projects[proj['name']] = proj

    def useShortcut(self,input):
        answer = {}
        answer['time'] = datetime.now().strftime("%H:%M")
        try:
            name =  get_close_matches(input,self.shortcuts,n=1)[0]
        except:
            answer['command'] = 'ERROR'
            answer['desc'] = 'Entry Not Found !' 
            answer['time'] = ''
                
        else:
            entry = self.shortcuts[name]

            
            if entry['command'] == 'start_entry':
                response = self.startTimeEntry(entry['desc'],entry['id'])
                answer['desc'] = response['data']['description']


            elif entry['command'] == 'ask_entry':
                desc = name
                response = self.startTimeEntry(desc,entry['id'])
                answer['desc'] = response['data']['description']

            elif entry['command'] == 'stop_entry':
                response = self.stopRunningEntry()
                answer['desc'] = 'jsut work pls'#response['data']['description']

            answer['command'] = entry['command']
            # answer['desc'] = response['data']['description']
        
        return answer


class GUI(object):
    def __init__(self,token):
        self.toggl = Toggl(token)
        self.build_gui()

    def build_gui(self):
        self.root = Tk()
        self.root.title("UCIS to AilaLink UI")
        self.root.resizable(False, False)

        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.attributes("-topmost", True)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.entry_string = StringVar()
        # self.entry_string = ''

        user_entry = ttk.Entry(mainframe,width=60, textvariable=self.entry_string, font='consolas')
        user_entry.grid(column = 1, row=1, columnspan = 3)

        refresh_button = ttk.Button(mainframe, text = u'\u27F3',command=self.refresh, width=10)
        refresh_button.grid(column=4,row=1, columnspan=2,sticky=E)

        self.text_box = Text(mainframe,width=70,height=8, font='consolas',state='disabled', background='black',fg='white')
        self.text_box.grid(column=1,row=4,columnspan=4)

        # pad 5px in all directions
        for child in mainframe.winfo_children(): child.grid_configure(padx=2, pady=2)

        # user_entry.focus()

        #Define keyboard shortcuts while in window
        self.root.bind("<Escape>", self.exit)
        self.root.bind('<Return>',self.run_shortcut)
        self.root.mainloop()
    
    def exit(self, event):
        self.root.destroy()
        
    def refresh(self):
        self.print2gui('\n---\tRefreshing Shortcuts File\t---\n')
        self.toggl.loadShortcutsFile()

    def print2gui(self, string):
        self.text_box.configure(state="normal")
        self.text_box.insert(END,string)
        self.text_box.see(END)
        self.text_box.configure(state="disabled")
    
    def run_shortcut(self,event):
        response = self.toggl.useShortcut(self.entry_string.get())
        self.entry_string.set('')

        self.print2gui("\n---\t"+response['command']+"\t---\n\t")
        self.print2gui(response['desc']+'\n\t'+response['time']+"\n\n")
        

    
token = "089c874aefeb3e6a4d655c73819949be"
gui = GUI(token)

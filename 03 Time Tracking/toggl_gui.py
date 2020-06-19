from difflib import get_close_matches
from json import load
from toggl.TogglPy import Toggl as togglpy#god i love python
from toggl.TogglPy import Endpoints
from tkinter import ttk,N,E,S,W, END,Tk,StringVar, Text, PhotoImage
from datetime import datetime, timedelta
from os import getcwd
from pynput.keyboard import Key, KeyCode, Listener
from sys import exit

class Toggl(togglpy):
    Projects = {}
    # directory = getcwd()
    def __init__(self,APIKey):
        self.setAPIKey(APIKey)
        self.directory = getcwd()
        self.shortcuts_dir=self.directory+'\\shortcuts.json'
        self.loadShortcutsFile()

    def loadShortcutsFile(self): #this loads the predefined shortcuts file
        try:
            with open(self.shortcuts_dir, encoding ='utf-8') as f:
                self.shortcuts = load(f)
        except NotADirectoryError:
            print("file not found")

    def stopRunningEntry(self):
        return self.stopTimeEntry(self.currentRunningTimeEntry()['data']['id'])

    def getAllProjects(self): 
        """
        Get all projects and add it to Projects dictionary within Toggl object
        Will not get tasks in project
        """
        response = self.request("https://www.toggl.com/api/v8/clients")
        for client in response:
            temp = self.getClientProjects(id=client['id'])
            for proj in temp:
                self.Projects[proj['name']] = proj

    def useShortcut(self,input):
        """
        Use a shortcut defined in the shortcuts .json file
        
        Returns: command, description, time 
        """
        answer = {}
        try:
            name =  get_close_matches(input,self.shortcuts,n=1)[0]
        except:
            answer['command'] = 'ERROR'
            answer['desc'] = 'Entry Not Found !' 
            answer['time'] = ''
                
        else:
            entry = self.shortcuts[name]
            answer['time'] = datetime.now().strftime("%H:%M")
            
            if entry['command'] == 'start_entry':
                response = self.startTimeEntry(entry['desc'],entry['id'])
                answer['desc'] = response['data']['description']


            elif entry['command'] == 'ask_entry':
                desc = name
                response = self.startTimeEntry(desc,entry['id'])
                answer['desc'] = response['data']['description']

            elif entry['command'] == 'stop_entry':
                response = self.stopRunningEntry()
                answer['desc'] = response['data']['description']
                answer['dur'] = response['data']['duration']

            answer['command'] = entry['command']
        
        return answer


class GUI:
    def __init__(self,token):
        self.toggl = Toggl(token)
        self.directory = getcwd()
        self.icon = self.directory+'\\toggl-512.png'
        self.build_gui()

    def build_gui(self):
        """
        builds the GUI, you shouldn't need to be calling this other than in thi init
        """
        self.root = Tk()
        self.root.title("Toggl Shortcuts")
        self.root.resizable(False, False)

        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.attributes("-topmost", True)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.iconphoto(True, PhotoImage(file = self.icon))

        self.entry_string = StringVar()

        self.user_entry = ttk.Entry(mainframe,width=60, textvariable=self.entry_string, font='consolas')
        self.user_entry.grid(column = 1, row=1, columnspan = 3)

        refresh_button = ttk.Button(mainframe, text = u'\u27F3',command=self.refresh, width=10)
        refresh_button.grid(column=4,row=1, columnspan=2,sticky=E)

        self.text_box = Text(mainframe,width=70,height=8, font='consolas',state='disabled', background='black',fg='white')
        self.text_box.grid(column=1,row=4,columnspan=4)

        # pad 5px in all directions
        for child in mainframe.winfo_children(): child.grid_configure(padx=2, pady=2)

        #Define keyboard shortcuts while in window
        self.root.bind("<FocusIn>", self.onFocusIn)
        self.root.bind("<FocusOut>", self.onFocusOut)
        self.root.bind("<Escape>", self.exit)
        self.root.bind('<Return>',self.run_shortcut)
        self.root.mainloop()
    
    def onFocusIn(self,event): 
        # self.print2gui('Focus in\n')
        self.user_entry.focus()
        # self.root.focus_force()
        pass
    

    def onFocusOut(self,event):
        # self.print2gui('Focus Out\n')
        # self.root.iconify()
        pass
        

    def exit(self, event):
        # self.root.destroy()
        self.root.iconify()
        
    def refresh(self):
        self.print2gui('\n---\tRefreshing Shortcuts File\t---\n')
        self.toggl.loadShortcutsFile()

    def print2gui(self, string):
        """
        Prints to the GUI large text box
        
        Requires input type string
        """
        self.text_box.configure(state="normal")
        self.text_box.insert(END,string)
        self.text_box.see(END)
        self.text_box.configure(state="disabled")
    
    def run_shortcut(self,event):
        """
        On TTK event:
            Takes entry in GUI text input field as input to toggl.useShortcut
            Clears input field
            Prints response to GUI
        """
        send_string = self.entry_string.get()
        self.entry_string.set('')
        self.print2gui("sent: "+ send_string)
        response = self.toggl.useShortcut(send_string)
        cmd_string = ' '*5+response['command']+' '*(5+(11-len(response['command']))) #it looks like a mess but i just want things to print pretty ok?
        self.print2gui("\n------"+cmd_string+"------\n\n\t")
        self.print2gui(response['desc']+'\n\t'+response['time']+"\n")
        if(response['command']=='stop_entry'):
            self.print2gui('\tDuration:\t'+str(timedelta(seconds=response['dur'])))
        self.print2gui('\n\n')

class Hotkeys:
    # Create a mapping of keys to function (use frozenset as sets/lists are not hashable - so they can't be used as keys)
    # Note the missing `()` after function_1 and function_2 as want to pass the function, not the return value of the function
    def __init__(self,key):
        # self.gui  =  object
        # The currently pressed keys (initially empty)
        self.pressed_vks = set()
        self.token = ''
        self.combination_to_function = {
            frozenset([Key.shift, KeyCode(vk=65)]): self.function_1,  # shift + a
            frozenset([Key.shift, KeyCode(vk=66)]): self.function_2,  # shift + b
            frozenset([Key.alt_l, KeyCode(vk=71)]): self.function_3,  # left alt + g
            frozenset([Key.alt_l, KeyCode(vk=67)]): self.start_gui,  # left alt + c
            # frozenset([Key.alt_l, KeyCode(vk=67), KeyCode(vk=91)]): self.make_gui,  # WIN+ left alt + c
        }

        

    def function_1(self):
        """ One of your functions to be executed by a combination """
        print('Executed function_1')


    def function_2(self):
        """ Another one of your functions to be executed by a combination """
        print('Executed function_2')

    def function_3(self):
        """Quit"""
        print('quitting')
        exit()

    def start_gui(self):
        # if self.gui.toggl:
        if hasattr(self,'gui') :
            print("opening gui")
            self.gui.user_entry.focus()
            pass
            
        else:
            print('starting gui')
            self.gui = GUI(self.token)
            pass
    

    def get_vk(self,key):
        """
        Get the virtual key code from a key.
        These are used so case/shift modifications are ignored.
        """
        return key.vk if hasattr(key, 'vk') else key.value.vk


    def is_combination_pressed(self,combination):
        """ Check if a combination is satisfied using the keys pressed in pressed_vks """
        return all([self.get_vk(self.key) in self.pressed_vks for self.key in combination])


    def on_press(self,key):
        """ When a key is pressed """
        vk = self.get_vk(key)  # Get the key's vk
        self.pressed_vks.add(vk)  # Add it to the set of currently pressed keys

        for combination in self.combination_to_function:  # Loop through each combination
            if self.is_combination_pressed(combination):  # Check if all keys in the combination are pressed
                self.combination_to_function[combination]()  # If so, execute the function


    def on_release(self,key):
        """ When a key is released """
        vk = self.get_vk(key)  # Get the key's vk
        self.pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys

    def start_listener(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
    
token = "089c874aefeb3e6a4d655c73819949be"
# gui = GUI(token)
hotkeys = Hotkeys(token)
# hotkeys.key = tokenA
hotkeys.start_listener()
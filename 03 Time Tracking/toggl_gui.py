from tkinter import *
from tkinter import ttk, filedialog
from toggl_test import Toggl

class GUI:
    def __init__(self,token):
        print('just work please')
        self.build_gui()
        self.toggl = Toggl(token)

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
        # self.root.bind('<Return>',self.next_cell)
        self.root.mainloop()
    
    def exit(self, event):
        self.root.destroy()
        

    def refresh(self):
        self.print2gui('\n\n---\Refreshing Shortcuts File\t---\n')
        self.toggl.loadShortcutsFile()

    def print2gui(self, string):
        self.text_box.configure(state="normal")
        self.text_box.insert(END,string)
        self.text_box.see(END)
        self.text_box.configure(state="disabled")
    
    
token = "089c874aefeb3e6a4d655c73819949be"
gui = GUI(token)
from tkinter import *
from tkinter import ttk, filedialog


class GUI:
    def __init__(self):
        print('just work please')
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

        html_link = StringVar()
        file_name = StringVar()

        user_entry = ttk.Entry(mainframe,width=60, textvariable=html_link, font='consolas')
        user_entry.grid(column = 1, row=1, columnspan = 3)

        refresh_button = ttk.Button(mainframe, text = u'\u27F3',command=self.refresh, width=10)
        refresh_button.grid(column=4,row=1, columnspan=2,sticky=E)

        text_box = Text(mainframe,width=70,height=8, font='consolas',state='disabled', background='black',fg='white')
        text_box.grid(column=1,row=4,columnspan=4)

        # pad 5px in all directions
        for child in mainframe.winfo_children(): child.grid_configure(padx=2, pady=2)

        # user_entry.focus()

        #Define keyboard shortcuts while in window
        self.root.bind("<Escape>", self.exit)
        self.root.bind('<Return>',self.next_cell)
        self.root.mainloop()
    
    def exit(self, event):
        self.root.destroy()

    def next_cell(self, event):
        if not html_link.get():
            user_entry.focus()
        elif html_link.get() and not file_name.get():
            file_entry.focus()
        else:
            convert()
            user_entry.delete('0',END)
            file_entry.delete('0',END)
            user_entry.focus()

    def refresh(self):
        print2gui('\n\n---\tConverting from UCIS to AILA\t---\n')
        fname = file_name.get()
        print2gui("\nlink:\t"+html_link.get()+"\n")
        print2gui("File:\t"+fname+"\n")

        if file_dir_default.get():
            # decided to not print to gui if just using default
            # ucis_2_aila(html_link.get(),fname) 
            pass
        else:
            file_dir = filedialog.askdirectory()
            file_dir = file_dir.replace('/','\\')+'\\'
            print2gui('Output Directory:\t'+file_dir+"\n")
            # ucis_2_aila(html_link.get(),fname,file_dir)
            pass
        print2gui('\n---\tConversion Complete\t---')

    def print2gui(self, string):
        text_box.configure(state="normal")
        text_box.insert(END,string)
        text_box.see(END)
        text_box.configure(state="disabled")
    
    

gui = GUI()
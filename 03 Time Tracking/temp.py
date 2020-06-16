from tkinter import *
from tkinter import ttk, filedialog

def exit(event):
    root.destroy()

def next_cell(event):
    if not html_link.get():
        link_entry.focus()
    elif html_link.get() and not file_name.get():
        file_entry.focus()
    else:
        convert()
        link_entry.delete('0',END)
        file_entry.delete('0',END)
        link_entry.focus()

def convert():
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

def print2gui(string):
    text_box.configure(state="normal")
    text_box.insert(END,string)
    text_box.see(END)
    text_box.configure(state="disabled")

root = Tk()
root.title("UCIS to AilaLink UI")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.attributes("-topmost", True)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

html_link = StringVar()
file_name = StringVar()

link_entry = ttk.Entry(mainframe,width=70, textvariable=html_link, font='consolas')
link_entry.grid(column = 2, row=1, columnspan = 3)

file_entry = ttk.Entry(mainframe, width = 70, textvariable=file_name, font='consolas')
file_entry.grid(column = 2, row=2, columnspan = 3)

file_dir_default = IntVar(value=1)
file_dir_select = ttk.Checkbutton(mainframe, text='Use Default Directory',variable=file_dir_default)
file_dir_select.grid(column=1,row=3, columnspan=2, sticky=W)

# add text to all areas where necessary
ttk.Label(mainframe,text ="Hyperlink").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe,text ="File Name").grid(column=1, row=2, sticky=W)

convert_button = ttk.Button(mainframe, text = 'Convert UCIS',command=convert, width=50)
convert_button.grid(column=3,row=3, columnspan=2,sticky=E)

text_box = Text(mainframe,width=80,height=8, font='consolas',state='disabled', background='black',fg='white')
text_box.grid(column=1,row=4,columnspan=4)

# pad 5px in all directions
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

link_entry.focus()

#Define keyboard shortcuts while in window
root.bind("<Escape>", exit)
root.bind('<Return>',next_cell)
root.mainloop()
import re
from tkinter import*
from tkinter.ttk import*
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog, simpledialog
from tkinter.scrolledtext import ScrolledText

# initializing gui window
# the root widget
root=Tk()
root.title('Sharvari Inamdar Notepad')
root.resizable(0,0)

#creating scrollable notepad window
notepad = ScrolledText(root, width = 100, height = 30)
FileName = ''

#defining file menu:-
# new file 
def cmdNew():
    global FileName
    if len(notepad.get('1.0' , END+'-1c'))>0:
        if messagebox.askyesno("Notepad", "Do you want to save changes?"):
            cmdSave()
        else:
            notepad.delete(0.0, END)
    root.title("Notepad")

# open file 
def cmdOpen():
    fd=filedialog.askopenfile(parent=root, mode ='r')
    t=fd.read()
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)

# save file
def cmdSave():
    fd=filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if fd!=None:
        data = notepad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error",message="Not able to save file!")
    
# exit file 
def cmdExit():
    if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
        root.destroy()

# defining edit menu:- 
# edit file-> cut 
def cmdCut():
    notepad.event_generate("<<Cut>>")

# file edit-> Copy
def cmdCopy():
    notepad.event_generate("<<Copy>>")

# edit file-> paste 
def cmdPaste():
    notepad.event_generate("<<Paste>>")
    
# edit file-> Clear 
def cmdClear():
    notepad.event_generate("<<Clear>>")
    
# edit file-> Find 
def cmdFind():
    notepad.tag_remove("Found", '1.0', END)
    find = simpledialog.askstring("Find", "Find What??:")
    if find: 
        idx = '1.0'
    while 1: 
        idx = notepad.search(find, idx, nocase=1, stopindex=END)
        if not idx: 
            break
        lastidx = '%s+%dc' %(idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx=lastidx
    notepad.tag_config('Found', foreground='white', background='blue')
    notepad.bind("<!>, click")

#handling click event 
def click(event):
    notepad.tag_config('Found', background='white', foreground='black')

#defining help menu:- 
#help menu
def cmdAbout():
    Label=messagebox.showinfo("About Notepad", "Notepad by - \n Sharvari Inamdar \nRoll no: 18")

#adding commands:-
#notepad menu items:
notepadMenu=Menu(root)
root.configure(menu=notepadMenu)

#file menu
fileMenu = Menu(notepadMenu, tearoff=False)
notepadMenu.add_cascade(label='File', menu = fileMenu)

fileMenu.add_command(label = 'New', command=cmdNew)
fileMenu.add_command(label = 'Open...', command=cmdOpen)
fileMenu.add_command(label = 'Save', command=cmdSave)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=cmdExit)

editMenu= Menu(notepad, tearoff=False)
notepadMenu.add_cascade(label='Edit', menu = editMenu)

editMenu.add_command(label='Cut', command=cmdCut)
editMenu.add_command(label='Copy', command=cmdCopy)
editMenu.add_command(label='Paste', command=cmdPaste)
editMenu.add_command(label='Delete', command=cmdClear)
editMenu.add_separator()
editMenu.add_command(label='Find...', command=cmdFind)

helpMenu= Menu(notepadMenu, tearoff=False,)
notepadMenu.add_cascade(label='Help', menu = helpMenu)
helpMenu.add_command(label='About Notepad', command=cmdAbout)

notepad.pack()
root.mainloop()
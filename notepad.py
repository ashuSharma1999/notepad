from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Unitted-Notepad")
    file=NONE
    TextArea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text documents","*.txt")])
    if file=="":
        file=NONE
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file==NONE:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("all files",'*.*'),("Text Document",'*.txt')])

        if file=="":
            file=None
        else:
           f==open(file,"w") 
           f.write(TextArea.get(1.0,END))
           f.close()
           root.title(os.path.basenanme(file)+"-Notepad")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def saveAs():
    global file
    if file==NONE:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("all files",'*.*'),("Text Document",'*.txt')])

        if file=="":
            file=None
        else:
           f==open(file,"w") 
           f.write(TextArea.get(1.0,END))
           f.close()
           root.title(os.path.basenanme(file)+"-Notepad")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def pageSetup():
    pass
def print():
    pass
def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))

def wordWrap():
    pass
def font():
    pass

def viewHelp():
    pass
def about():
    showinfo("Unitted-Notepad","Notepad created by ashuSharma.....")

if __name__=='__main__':
    root=Tk()
    #p1=PhotoImage(file="a.png")
    #root.iconphoto(FALSE,a.png)
    
    root.title("Unitted-Notepad")
    root.geometry("644x434")
    TextArea=Text(root,font="lucida 13")
    file=NONE
    TextArea.pack(expand=TRUE, fill=BOTH)
    MenuBar=Menu(root)

    FileMenu=Menu(MenuBar,tearoff=0)
    FileMenu.add_command(label="New        Ctrl+N",command=newFile)
    FileMenu.add_command(label='Open...   Ctrl+O',command=openFile)
    FileMenu.add_command(label='Save        Ctrl+S',command=saveFile)
    FileMenu.add_command(label="Save As...",command=saveAs)
    FileMenu.add_separator()
    FileMenu.add_command(label="Page Setup...",command=pageSetup)
    FileMenu.add_command(label="Print       Ctrl+P",command=print)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit',command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)

    EditMenu=Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Cut        Ctrl+X",command=cut)
    EditMenu.add_command(label="Copy     Ctrl+C",command=copy)
    EditMenu.add_command(label="paste     Ctrl+V",command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    FormatMenu=Menu(MenuBar,tearoff=0)
    FormatMenu.add_command(label="Word Wrap",command=wordWrap)
    FormatMenu.add_command(label="Font...",command=font)
    MenuBar.add_cascade(label="Format",menu=FormatMenu)
    
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="View Help",command=viewHelp)
    HelpMenu.add_separator()
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    
    root.config(menu=MenuBar)
    
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    root.mainloop()

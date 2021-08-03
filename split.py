import tkinter as tk
from TkinterDnD2 import DND_FILES, TkinterDnD
from tkinter import messagebox
import tkinter.font as font
from pdf_splitter import pdf_splitter as ps

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def b_pressed():
    if listb.size() == 0:
        messagebox.showerror("Failure", "Please add some items to split before pressing the button")
    else:
        for i in listb.get(0,listb.size()):
            ps.Split(i)
        listb.delete(0,listb.size())
    
    



def drop_inside_listbox(event):
    files = root.tk.splitlist(event.data)
    
    for filename in files:
        if filename.endswith(".pdf"):
            listb.insert('end', filename)

    


root = TkinterDnD.Tk()
root.title("PDF-Splitter")
root.geometry("500x290")
root.minsize(500,290)
root.maxsize(500,290)

#Icon
icon = tk.PhotoImage(file="src/icon.png")
root.iconphoto(True, icon)


specialFont = font.Font(family="Tahoma")
contributeFont = font.Font(family="Tahoma", size=7)

listb = tk.Listbox(root, selectmode=tk.SINGLE, bg="gray", fg="#209DE6")
listb.pack(fill=tk.X)
listb.drop_target_register(DND_FILES)
listb.dnd_bind("<<Drop>>",drop_inside_listbox)
listb['font'] = specialFont

b = tk.Button(root, text="Split", command=b_pressed, height=3, bg="#209DE6", fg="#E6E24E")
b['font'] = specialFont
b.pack(fill=tk.X)

l = tk.Label(text='Icon designed by "Those Icons" from Flaticon.                                          V1.0 Made by Johan Jakberger 2021-07-30', bg="black", fg="#E6E24E")
l['font'] = contributeFont
l.pack(fill=tk.X)


root.mainloop()
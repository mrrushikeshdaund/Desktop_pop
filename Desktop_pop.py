from tkinter import *
from tkinter import PhotoImage

base = Tk()
base.title("Desktop pop")
base.geometry("900x900")



def popmenu(e):
    m1.tk_popup(e.x_root, e.y_root)


m2 = Menu(base, tearoff=0)
m2.add_radiobutton(label="Large Icons")
m2.add_radiobutton(label="Small Icons")
m2.add_radiobutton(label="Medium Icons")
m2.add_separator()
m2.add_checkbutton(label="Auto arrange icons")
m2.add_checkbutton(label="Align icons to grid")
m2.add_separator()
m2.add_checkbutton(label="Show desktop icons")

m3 = Menu(base, tearoff=0)
m3.add_command(label="Name")
m3.add_command(label="Size")
m3.add_command(label="Item Type")
m3.add_command(label="Date Modified")

m4 = Menu(base, tearoff=0)
m4.add_command(label="Folder")
m4.add_command(label="Shortcut")
m4.add_separator()
m4.add_command(label="Microsoft Database")
m4.add_command(label="Microsoft Word Document")
m4.add_command(label="Microsoft PowerPoint Presentation")
m4.add_command(label="Text Document")
m4.add_command(label="Microsoft Excel Worksheet")

m1 = Menu(base, tearoff=0)
m1.add_command(label="AMD Radon Setting")
m1.add_separator()
m1.add_cascade(label="View", menu=m2)
m1.add_cascade(label="Sort By", menu=m3)
m1.add_command(label="Refresh")
m1.add_separator()
m1.add_command(label="Open")
m1.add_command(label="Paste")
m1.add_command(label="Paste Shortcut")
m1.add_command(label="Intel Graphics")
m1.add_separator()
m1.add_cascade(label="New", menu=m4)
m1.add_separator()
m1.add_command(label="Display Settings")
m1.add_command(label="Personalize")

base.bind('<Button-3>', popmenu)

base.mainloop()

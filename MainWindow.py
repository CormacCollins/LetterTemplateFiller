from tkinter import Tk, Label, Button, Entry, StringVar


class MyFirstGUI:

    def getText(self, event):
        res = event.widget.get()
        print(res)
        self.label.config(text=res)
             

    def __init__(self, master): 
            
        self.master = master
        sv = StringVar()
        self.sv = sv

        self.label = Label(master, text="Template filler", anchor="e").grid(row=0, column=0)
        #self.label.pack()

        e = Entry(master)
        self.entry = e
        e.bind('<Return>', self.getText)
        e.grid(row=1, column=0)


        e.focus_set()

        self.master.geometry('300x60')

    def greet(self):
        print("Greetings!")

    def addLabelToGrid(self):
        #make adding lables easy to set up in grid pattern

root = Tk()
root.config(background="#a1dbcd")
my_gui = MyFirstGUI(root)
root.mainloop()

text_entered = my_gui.sv.get()
my_gui.label.text = text_entered
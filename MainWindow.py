from tkinter import Tk, Label, Button, Entry, StringVar

entryDictionary = {}

class MyFirstGUI:

    def allFieldsFull(self):
        areAllFilledIn = True
        for field, entry in self.entries.items():
            if(entry.get() == ""):
                areAllFilledIn == False
        
        return areAllFilledIn

    def getText(self, event):
        # key,val is entry, wordField
        print(self.entries)

        for key,val in self.entries.items():
            entryDictionary[key] = val.get()
        
        currentEntry = None
        for key, val in self.entries.items():
            if val is event.widget and key == "patient_DOB":
                if self.allFieldsFull():
                    print("Filling template")
                    print(entryDictionary)
                

    def __init__(self, master): 

        self.currentRow = 0
        self.labels = list()  
        self.entries = {}       
        self.master = master

        self.label = Label(master, text="Template filler", anchor="e").grid(row=0, column=0)
        self.currentRow += 1
        #self.label.pack()

        # e = Entry(master)
        # self.entry = e
        # e.bind('<Return>', self.getText)
        # e.grid(row=1, column=0)
        # e.focus_set()

        #add an entry for a field
        self.addEntryAndLabel("GP surname", "doctor_surname")
        self.addEntryAndLabel("GP surgury", "doctor_surgery")
        self.addEntryAndLabel("patient first name", "patient_first_name")
        self.addEntryAndLabel("patient surname", "patient_surname")
        self.addEntryAndLabel("patient DOB", "patient_DOB")


        self.master.geometry('300x160')

    def greet(self):
        print("Greetings!")

    def addEntryAndLabel(self, entryName, entryFieldId):

        label = Label(self.master, text=entryName, anchor="e").grid(row=self.currentRow, column=0)
        entry = Entry(self.master)
        entry.bind('<Return>', self.getText)
        entry.grid(row=self.currentRow, column=1)
        
        self.labels.append(label)
        self.entries[entryFieldId] = entry

        self.currentRow += 1

        print("Label added")
        #make adding lables easy to set up in grid pattern



root = Tk()
root.config(background="#a1dbcd")
my_gui = MyFirstGUI(root)
root.mainloop()

from tkinter import Tk, Label, Button, Entry, StringVar

from subprocess import call


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
                # if fields are full we can pass them as args to the filling
                if self.allFieldsFull():
                    print("Filling template")
                    print(entryDictionary)
                    out = call(["python", "fillTemplate.py", str(entryDictionary['doctor_surname']), str(entryDictionary['doctor_surgery']), str(entryDictionary['patient_first_name']), str(entryDictionary['patient_surname']), str(entryDictionary['patient_DOB'])])
                    print(out)

    # for putting cursor back to original spot when user returns to window
    def handle_focus(self, event):
        if event.widget == self.master:
            print("I have gained the focus")
            if self.currentFocusEntry:
                self.currentFocusEntry.icursor(0)
            return

        for key, val in self.entries.items():
            if event.widget is val:
                self.currentFocusEntry = val


    def __init__(self, master): 

        self.currentRow = 0
        self.currentFocusEntry = None
        self.labels = list()  
        self.entries = {}       
        self.master = master

        self.label = Label(master, text="Template filler", anchor="e").grid(row=0, columnspan=1, sticky="ew")
        self.currentRow += 1

        #add a 1.) entry 2.)field - the field corresponds to the word field names 
        self.addEntryAndLabel("GP surname", "doctor_surname")
        self.addEntryAndLabel("GP surgury", "doctor_surgery")
        self.addEntryAndLabel("patient first name", "patient_first_name")
        self.addEntryAndLabel("patient surname", "patient_surname")
        self.addEntryAndLabel("patient DOB", "patient_DOB")

        #now set the focus to the frist entry
        self.entries['doctor_surname'].icursor(0)

        self.master.geometry('300x160')
        self.master.bind("<FocusIn>", self.handle_focus)

    def greet(self):
        print("Greetings!")

    def addEntryAndLabel(self, entryName, entryFieldId):

        label = Label(self.master, text=entryName, anchor="w").grid(row=self.currentRow, column=0, sticky="ew")
        entry = Entry(self.master)
        entry.bind('<Return>', self.getText)
        entry.bind("<FocusIn>", self.handle_focus)
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

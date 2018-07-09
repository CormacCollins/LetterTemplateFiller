from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import csv
import tkinter  
import sys
import datetime
from subprocess import call


# populates fields -- needs to change if columns in csv change
def populateDocMergeWithGpDetails(document, row):
        document.merge(
            doctor_firstname=row[1], # 0 is the title - maybe change later
            doctor_surname=row[2],
            doctor_surgery=row[3],
            address_1=row[4],
            address_2=row[5]       
        )

def populateDocMergeWithPatientDetails(document, title, firstName, surname, DOB):
    if "miss" not in title:
        title += "."

    document.merge(
            patient_title=title, # 0 is the title - maybe change later
            patient_first_name=firstName,
            patient_surname=surname,
            patient_DOB=DOB        
        )

# return list of array rows (GP details)
def getGPList(fileName):
    gpList = list()
    with open(fileName, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # print("successfully opened" + str(fileName)    
        
        for row in reader:
            gpList.append(row)

    return gpList

def findGP(name, gpList):
    for row in gpList:
        print(row)
        if(row[2] == name):
            return row

    return None

# ------------------------- Main ----------------------------

gpListFile = 'addresses.csv'
template = "gp_template.docx"
document = MailMerge(template)
print("Fields:")
fields_set = document.get_merge_fields()
print(fields_set)

# get cmd args
argv = sys.argv
gpSurname = argv[1]
gpSurgery = argv[2]
ptTitle = argv[3]
ptFirstName = argv[4]
ptSurname = argv[5]
patientDOB = argv[6]

gpList = getGPList(gpListFile)
gpInfo = findGP(gpSurname, gpList)

print("ARGS, GP LIST AND GP INFO")
print(argv)
print(gpList)
print(gpInfo)

if gpInfo is not None:
    populateDocMergeWithGpDetails(document, gpInfo)
    populateDocMergeWithPatientDetails(document, ptTitle, ptFirstName, ptSurname, patientDOB)

    now = datetime.datetime.now()
    dateToday = now.strftime("%d.%m.%Y")
    documentName = ptFirstName + " " + ptSurname + " Ex Phys GP report " + dateToday + ".docx"
    print("new doc name: " + documentName)
    try:
        
        document.write(documentName)
        print("Document write complete")
    
    except:
        print("Unable to open file")
else:
    print("Could not find specified GP info.")









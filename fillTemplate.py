from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import csv
import tkinter  
import sys


# populates fields -- needs to change if columns in csv change
def populateDocMerge(document, row):
        document.merge(
            doctor_full_name=row[1], # 0 is the title - maybe change later
            doctor_surgery=row[2],
            address_1=row[3],
            address_2=row[4],
            doctor_surname=row[5]        
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


gpName = input()

gpList = getGPList(gpListFile)
gpInfo = findGP(gpName, gpList)

if gpInfo is not None:
    populateDocMerge(document, gpInfo)
    try:
        document.write('test-output.docx')
    
    except:
        print("Unable to open file")
else:
    print("Could not find specified GP info.")









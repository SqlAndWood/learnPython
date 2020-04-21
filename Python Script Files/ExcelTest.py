import tkinter as tk 
from tkinter import filedialog
import pandas as pd

def getExcel ():
        global df
        import_file_path = filedialog.askopenfilename()
        df = pd.read_excel (import_file_path)
        #Convert headings from Number values into String Values. Makes it simpler to reference a String
        df.columns = df.columns.astype(str)        

def LoadExcelIntoDataFrame():

    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
    canvas1.pack()

    browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browseButton_Excel)

    root.mainloop()


def Admissions(row, colA, colB):
    if row[colA] < row[colB]:
        val = 1
    else:
        val = 0

    return val

def Discharges(row, colA, colB):
    if row[colA] > row[colB]:
        val = 1
    else:
        val = 0

    return val   

def IdentifyColumns(aCol, ColumnToIgnore):
    #
    for (columnName, columnData) in df.iteritems():
        if columnName != ColumnToIgnore: #'PSLK':
            aCol.append(columnName)
            #print(columnName)

    return aCol

getExcel = 'false'

if getExcel == 'true':
    LoadExcelIntoDataFrame()

print (df.head(0))

# https://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/

#pip install lxml

import pandas as pd
from bs4 import BeautifulSoup

#I use a file, as we are unable to connect at this point in time. 
with open('C:\\Data\\Python Test Scrape\\FullData.txt', 'r') as file:
    html_content = file.read().replace('\n', '')

# Parse ALL the html content
soup = BeautifulSoup(html_content,  'html.parser')

#Limit the HTML to just the subset of data we would like to parse.
gdp_table = soup.find("table", attrs={"class": "data table olap crosstab default"})

# print(gdp_table.prettify())

#obtain the names for the COlumns.
column_names = []

tableRow = gdp_table.find('tr')
tableHeadings = gdp_table.find_all('th')

for th in tableHeadings:
    if th.get_text().lstrip() != "":
        column_names.append(th.get_text().lstrip())

#@visual observation only
headingValues = ''
for h in column_names:
    headingValues += h.strip() + ','

#not needed. Redundant
n_columns = len(column_names) 
#not needed. Redundant
n_rows = len(gdp_table.find_all('tr')) 

TableBody =gdp_table.find("tbody", attrs={"id": "detailRows"})

RowPosition = 1
columnPosition = 0

ThisRow = headingValues.rstrip(',') + "\r\n"

# Loop all table rows <tr>
for thisField in TableBody.find_all('td'): 
    #each step moves to the next field, a ColumnPosition
    attributes_dictionary = thisField.attrs
     
    if 'data-fieldvalue' in attributes_dictionary:
   
        # ThisRow = ThisRow +  str(RowPosition) + ': ' +  str(columnPosition) + ': '  + str(attributes_dictionary.get("data-fieldvalue")) + ','
        ThisRow = ThisRow + str(attributes_dictionary.get("data-fieldvalue")) + ','

        columnPosition += 1

        if columnPosition >= n_columns  :
            RowPosition += 1
            columnPosition = 0
            ThisRow = ThisRow.rstrip(',') + "\r\n"
             #Lets us track the number of records processed.
            print(RowPosition)

import csv
with open('FullData.csv', 'w', newline='') as file:
    file.write(ThisRow)


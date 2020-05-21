import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content,  'html.parser')
# //print(soup.prettify()) # print the parsed data of html


#print(soup.title)

gdp_table = soup.find("table", attrs={"class": "wikitable"})
gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows

# Get all the headings of Lists
headings = []
for td in gdp_table_data[0].find_all("td"):
    # remove any newlines and extra spaces from left and right
    headings.append(td.b.text.replace('\n', ' ').strip())

#print(headings)

for h in headings:
    print(h)


#need to obtain each sub heading for each item?


#canvasTable

#class "data table olap crosstab default"
print ('done')

data = {}
for table, heading in zip(gdp_table_data[1].find_all("table"), headings):
    # Get headers of table i.e., Rank, Country, GDP.
    t_headers = []

    print ('next')

    for th in table.find_all("th"):
        # remove any newlines and extra spaces from left and right
        t_headers.append(th.text.replace('\n', ' ').strip())

    # Get all the rows of table
    table_data = []
    for tr in table.tbody.find_all("tr"): # find all tr's from table's tbody
        
        t_row = {}
        # Each table row is stored in the form of
        # t_row = {'Rank': '', 'Country/Territory': '', 'GDP(US$million)': ''}

        # find all td's(3) in tr and zip it with t_header
        for td, th in zip(tr.find_all("td"), t_headers): 
            t_row[th] = td.text.replace('\n', '').strip()

        table_data.append(t_row)

    # Put the data for the table with his heading.
    data[heading] = table_data


for th in t_headers:
    print(th)

# print(data)

import csv

for topic, table in data.items():
    # Create csv file for each table
    with open(f"{topic}.csv", 'w') as out_file:
        # Each 3 table has headers as following
        headers = [ 
            "Country/Territory",
            "GDP(US$million)",
            "Rank"
        ] # == t_headers
        writer = csv.DictWriter(out_file, headers)
        # write the header
        writer.writeheader()
        for row in table:
            if row:
                writer.writerow(row)
                # print(row)



import pyodbc 
import pandas as pd 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.\sql2017;'
                      'Database=Monitoring;'
                      'Trusted_Connection=yes;')

#cursor = conn.cursor()
#cursor.execute('SELECT * FROM app.Monitoring')

#for row in cursor:
#   print(row)


df = pd.read_sql_query('SELECT TOP 1 * FROM app.Monitoring', conn)
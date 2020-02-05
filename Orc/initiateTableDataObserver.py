# coding:utf8

"""This is the summary line

This script

This file can also be imported as a module and contains the following
functions:

   
    * initiateTableDataObserver - the main function of the script
    * getTableCount
   
    # hashes = list(map(abs, map(hash, keys)))
    # entries = list(zip(hashes, keys, v1))
    # comb_entries = list(zip(hashes, keys, v1, v2, v3, v4, v5))
   
"""

import pyodbc
from pprint import pprint

class t_sqlDataLoader():

    """Class docstrings go here."""

    __version__ = "0.0.1"
    __author__ = "Andrew Wood"
    __copyright__ = "https://www.python.org/doc/copyright/"
    __credits__ = ["Andrew Wood", "Annabelle"]
    __license__ = "https://docs.python.org/3/license.html"
    __maintainer__ = "Andrew Wood"
    __email__ = "awoody@protonmail.com"
    __status__ = "development: my first ever attempt to write Python code!"
    __comments__ = "Ring finger amputated Sun Nov 17 2019"
    __date__ = 'Fri Nov 22 2019'

    def __init__(self, server_name: str, server_instance_name: str, database_name: str, trusted_connection: str = 'yes'):
        """
        Parameters
        ----------
        server_name : str
            The name of the SQL Server
        server_instance_name : str
            The instance name of the SQL Server
        database_name : str
            The nameof the SQL Server database to review
        trusted_connection : str, optional
            Indicates if this connection is a trusted connection.
        """
        self.server_name: str = server_name
        self.server_instance_name: str = server_instance_name
        self.database_name: str = database_name
        self.trusted_connection: str = trusted_connection.lower()

        self.full_server_instance_name: str = ''

        if self.server_name != '':
            self.full_server_instance_name: str = self.server_name + \
                '\\'+self.server_instance_name
        else:
            self.full_server_instance_name: str = '.\\'+self.server_instance_name

        # 'concatenates a correct connection string: # https://snippets.cacher.io/snippet/e1b29d68e9fb2161e45d'          # <== docstring
        self.connString: str = ';'.join([
                                ''.join(['Driver={SQL Server};Server=',self.full_server_instance_name]) ,
                                ''.join(['Database=',self.database_name]),
                                ''.join(['Trusted_Connection=',self.trusted_connection]),
                                ''.join('')         #blank string forces closing semicollan
                                ])

        return None

    def initiateTableDataObserver(self, schema_name: str, table_name: str, number_records_to_observe: str = '*') -> bool:
        """Class method docstrings go here."""
        self.schema_name: str = schema_name
        self.table_name: str = table_name
        
        # test if a number
        if (int(number_records_to_observe) * 0 ) == 0 :
            self.record_count = int(number_records_to_observe)
            self.SelectStatement =  'SELECT TOP {} * FROM '.format(self.record_count)
            
        else:#anything but a number hasbeen provided,
            self.getTableCount( schema_name, table_name) 
            self.SelectStatement = 'SELECT * FROM '
       
        sqlQuery: str = ''.join([
                                ''.join([self.SelectStatement, schema_name]) ,
                                ''.join(['.', table_name]),
                                ''.join('')         #blank string forces closing semicollan
                                ])
      
        cs = pyodbc.connect(self.connString)
        cursor = cs.cursor()
        cursor.execute(sqlQuery)
        
        self.columns = [column[0] for column in cursor.description]
        self.columnCount = len(self.columns)
        self.columnsmetadata = [column for column in cursor.description]
        
        self.dictresults = []
        self.dataresults = []
        
        for row in cursor.fetchall():
            self.dataresults.append(row)
            self.dictresults.append(dict(zip(self.columns, row)))
        
        cursor.close()
        cs.close()
        
        if len(self.dataresults) == self.record_count:
             return True

        return False    
    
    # @property    
    def getTableCount(self, schema_name: str, table_name: str) -> int:
        """Class method docstrings go here."""
                
        sqlQuery: str = ''.join([
                            ''.join(['SELECT COUNT(*) FROM ', schema_name]) ,
                            ''.join(['.', table_name]),
                            ''.join('')         #blank string forces closing semicollan
                            ])
        
        cs = pyodbc.connect(self.connString)
        cursor = cs.cursor()
        cursor.execute(sqlQuery=sqlQuery)
        
        self.columns = [column[0] for column in cursor.description]
        self.columnCount = len(self.columns)
        self.columnsmetadata = [column for column in cursor.description]
        self.record_count = cursor.fetchone()[0] 
         
        cursor.close()
        cs.close()
        
        return None


obj = t_sqlDataLoader ( server_name=".", server_instance_name="SQL2017", database_name="DataSets", trusted_connection="yes")
g = obj.initiateTableDataObserver(schema_name= "dbo", table_name="History", number_records_to_observe = '2')

print(obj.columnCount, ': ', obj.columns, )
print(obj.columnsmetadata)    

pprint(obj.dataresults)
pprint(obj.dictresults)

import json
print(json.dumps(obj.dictresults))

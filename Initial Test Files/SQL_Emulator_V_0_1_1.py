from SQL_Table_V_1_0_1 import printData

"""
Grant De La Campa
2018
version: 0.1.1 ALPHA

About:
    This program is designed to parse mySQL querys as though you were using an actual database. Loosely based on block chains it stores each table as a block in a chain in order to simulate a databases ability to have multiple tables. Input is parsed for correct syntax by auxilary functions and then passed into the database once verified.
Ues:
    This could be useful to practice your SQL skills or may have some other unintended applications. This was mostly a for fun exercise, as such it may not use the best programing concepts or methodologies. If you see any errors please feel free to let me know at grantdelacampa@gmail.com or fork the project for yourself.
    
New in version:
    -Added error handlers
    -removed test cases
    -removed various erronious print statements
    -log function on shell, gives a log of all entries

Known Bugs:
    -accepts create table without any headers
    -missing some error cases
    -need unified error message system
    -if formatting is verified as incorrect the data is still appened to the database
    -insert may not be designed properly
    -truncate table actually is a table drop in this context, switch keys

Working:
    CREATE TABLE <table_name> (<column_heads>)
    SELECT * FROM *
    SELECT * FROM <table_name>
    DROP DATABASE
    TRUNCATE TABLE <table_name>
    INSERT INTO <table_name> (<column_heads>) VALUES (<column_heads>)*

    
    *Where len(<column_heads>) == len(<column_values>)
Semi-working:
    SELECT <item/s> FROM <table_name>           -> check this later cant remeber if it works
    
adding:
    INSERT <item/s> FROM <table_name>
    DELETE <item/s> FROM <table_name>
    DROP TABLE <table_name>
    DROP COLUMN <column_name>
    DROP ROW <row_name>
    Table dump function to output formatted SQL Queries
    
Possible updates:
    table JOINS

Notes:
    to solve the problem of WHERE use the beging keys to process data and rip the WHERE off the end, process the data as is should be
    send that data packed to a WHERE method to then process that data down more.
    ie SELECT name FROM table WHERE name = john
    process as SELECT name FROM table [WHERE name - john]
    return processed SELECT and [WHERE name = john] to a
    WHERE method finish processing...
"""

"""------------------------------------------------------------------
                Creates the initial table collection
------------------------------------------------------------------"""
class Database():
    def __init__(self):
        self.chain = []

        self.current_transactions = []
        
        
    def new_block(self, name, column, values):

        #Padds the values to ensure proper formatting of a new block
        if (values == []) | (values == None):
            for i in range(len(column)):
                values.append([])

        #print (values)

        #each block is a table in the chain
        block = {
            'index': len(self.chain) + 1,
            'name': name,
            'column': column,
            'values': values,
            }
        self.current_transactions = []

        self.chain.append(block)
        return block

        #passes in the column as a list [], and name as a string
    def search(self, column, name):
        #cond 1: * from *
        #cond 2: * from <table>
        #cond 3: <data> from <table>
        foundIndex = 0
        
        #case 1 all columns from all tables
        if (column == ['*']) & (name == "*"):
            print ("all columns case")
            for item in root.chain:
                if(len(item['column']) > len(item['values'])):
                    #find the difference and pad the data to prevent printing errors
                    dif = len(item['column']) - len(item['values'])
                    for j in range(dif):
                        item['values'].append([])
                printData(item['name'], item['column'], item['values'])
                print ("\n")
                
        #case 2 all columns from this table
        elif (column == ['*']) & (name != "*"):
            for items in self.chain:
                if items['name'] == name:
                    if items['values'] == []:
                        print ("no values stored in table")
                    else:
                        printData(name, items['column'], items['values'])
                else:
                    print ("error: that table does not exist")
            print ('\n')
            
        #case 3 this/these column(s) from table
        #for now only works for singular data ie ONE column from ONE table
        else:
            targetChain = []
            targetIndex = []
            count = 0
            for items in self.chain:
                if items['name'] == name:
                    for headers in items['column']:
                        #cheat way to convert list to string for column value
                        if headers == column[0]:
                            targetIndex.append(items['values'][count])
                        count += 1
                else:
                    print ("error that table doesnt exist")
            printData(name, column, targetIndex)
            print ('\n')
    def delete(self, name):
        #print ("database truncate reached: <{}>".format(name))
        for items in self.chain:
            if items['name'] == name:
                self.chain.pop(items['index']-1)
            else:
                print ("Error on truncate <{}> not found")
    def addData(self, column, name, data):
        """
        Need to handle case of data entered for non specific header.
        Also need to append a blank into the table
        Also need a WHEN implemented but maybe later 
        """
        columnsExist = False
        indexCount = 0
        columnIndexRef =[]
        tableIndex = 0
        if column == []:
            print ("this is a no column case, count table headers and if equal to data append data")
        else:
            if len(column) == len(data):
                for item in self.chain:
                    if item['name'] == name:
                        tableIndex = item['index'] - 1
                        for headers in item['column']:
                            if headers == column[indexCount]:
                                columnsExist = True
                                columnIndexRef.append(indexCount)
                            else:
                                columnsExist = False
                            indexCount += 1
                    else:
                        print ("Error that table doesnt exist")
            else:
                print("error malformed statement")
        if columnsExist == True:
            for i in columnIndexRef:
                print (self.chain[tableIndex]['column'][i])
                self.chain[tableIndex]['values'][i].append(data[i])
            #then perform operations

    def truncate(self, name):
        for item in self.chain:
            if item['name'] == name:
                print (item)
    def tabledrop(self, name):
        print ("Dropped table {}".format(name))
    def databasedrop(self):
        print ("database wiped")
        self.chain = []
    def proofOfAdditions(self, name):
        for items in self.chain:
            if items['name'] == name:
                return False
                break
        return True

#actual database creation
root = Database()
       
"""------------------------------------------------------------------
                        process the querys
------------------------------------------------------------------"""
#splits the input into a list and hands it off for processing
#would act as a inpoint for multifile implementation
#i.e. call to sqlmain() from "SQL_test" will use all other functions from
#SQL_Emulator

def  sqlmain(query):
    splitQ = query.split()
    syntaxprocesser(splitQ)
    
"""------------------------------------------------------------------
                     Query function methods
------------------------------------------------------------------"""
#select, create, insert, delete, _from functions
    #parameter: query -the initial query without the key
    
def select(query):
    targetValues = []
    targetTable = ""
    for item in query:
        if item != "FROM":
            targetValues.append(item)
        elif item == "FROM":
            targetTable = query[len(targetValues) + 1]
            root.search(targetValues, targetTable)

def create(query):
    name = []
    columns = []
    values = []                                 #temp 
    depth = len(query)                          #TODO strip values from query
    #check for table key word                    append to values
    if query[0] == 'TABLE':
        name = query[1]
        if root.proofOfAdditions(name):
            #checks the query for <(column_names)>
            for item in query[2:]:
                if '(' in item:
                    columns.append(item[1:])
                elif ')' in item:
                    columns.append(item[:len(item)-1])
                    break
                else:
                    columns.append(item)
            root.new_block(name, columns, values)
        else:
            print ("Error in input on {} Table already exists".format(query[1]))
    else:
        print ("Error in input on function: <{}>, incorrect syntax".format(query[0]))
"""
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

INSERT INTO table_name
VALUES (value1, value2, value3, ...);
"""
def insert(query):
    print ("this is an insert {}".format(query))
    targetValues = []
    targetNames = []
    targetTable = ""
    valueReached = False
    #verifys correct formatting 
    if query[0] == 'INTO':
        #print ("begin insert of {}".format(query[1:]))
        targetTable = query[1]
        #Verifys formatting
        if (isinstance(targetTable, str)) & ('(' not in targetTable) & (targetTable != 'VALUES'):
            #loops through the remaining query for processing
            for item in query[2:]:
                if '(' in item:
                    if valueReached == True:
                        targetValues.append(item[1:])
                    else:
                        targetNames.append(item[1:])
                elif ')' in item:
                    if valueReached == True:
                        targetValues.append(item[:len(item)-1])
                    else:
                        targetNames.append(item[:len(item)-1])
                elif item == 'VALUES':
                    valueReached = True
                else:
                    if valueReached == True:
                        targetValues.append(item)
                    else:
                        targetNames.append(item)
        else:
            print ("error no table name referenced")
    else:
        print ("error malformed statement {}".format(query))
    root.addData(targetNames,targetTable, targetValues)

"""
DELETE FROM table_name
WHERE condition;
"""
def truncate():
    print ("this is a truncate")
    
"""
DROP DATABASE databasename;
"""
def drop(query):
    if query[0] == 'TABLE':
        root.tabledrop(query[1:])
    elif query[0] == 'DATABASE':
        root.databasedrop()
        
def delete(query):
    if query[0] == 'TABLE':
        #print ("truncate reached on query: {}".format(query))
        root.truncate(query[1])
        

def full():
    pass
def right():
    pass
def left():
    pass
def inner():
    pass
         
"""------------------------------------------------------------------
                    initial input processor
------------------------------------------------------------------"""
#takes the tokenized query and compares it to a database to determine 
#query function, then calls the appropriate function to handle
#the final parsing.
    
def syntaxprocesser(query):
    keyword = query[0]
    trail = query[1:]
    error = -1
    keys = {
        'CREATE': create,
        'SELECT': select,
        'INSERT': insert,
        'DELETE': delete,
        'DROP' : drop,
        'TRUNCATE': truncate,
        'FULL': full,
        'RIGHT': right,
        'LEFT': left,
        'INNER': inner,
        }
    for key in keys:
        if key == keyword:
            keys[key](trail)
            error = 0
    if(error == -1):
        print ("Error in input on function: <{}>, incorrect syntax". format(keyword))

def errorEvent(eventID, location):
    pass
    """ What types of errors do we have?
    type 1: No keyword selected
    type 2: Malformed statement
        -no table name
        -no TABLE key Refer to type 1 error
        -no parantesis
    type 3: some parameter out of bounds ie 5 headings 7 data blocks
    type 4: 
"""


    

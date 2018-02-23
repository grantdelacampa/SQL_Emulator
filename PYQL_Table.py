"""
File: PYQL_Table.py
Name: Grant De La Campa
Date: 2018
Version: 1.2

Desc: Processes data from a simulated database, and prints that data as a table.

Usage: This program accepts formatted data from a database in the form,
        printData(<str:Name>, [<str:header(s)>...], [[<str:data1>],...]
Example:
        Input: printData('test', ['header 1', 'header 2'], [['data 1'],['data 2']])

        Output: Results from database: test
                + --------- + --------- + 
                | header 1  | header 2  | 
                + --------- + --------- + 
                | data 1    | data 2    | 
                + --------- + --------- + 
"""

def printData(name, headers, data):
    #verify the data will be in range of the columns
    #i.e. there isnt 5 sets of data and 3 columns
    print ("Results from database: {}".format(name))
    if len(data) <= len(headers):
        printMatrix = []
        rowLength = 0
        columnLength = 0
        offsetValue = 0
        lineBreak = None
 
        #sets up row and column length parameters 
        #also sets the offsetValue based on headers and data
        headerPointer = 0
        for item in data:
            if(len(headers[headerPointer]) > offsetValue):
                offsetValue = len(headers[headerPointer])
            for tar in item:
                if len(tar) > offsetValue:
                    offsetValue = len(tar)
            if rowLength < len(item):
                rowLength = len(item)
            headerPointer += 1
        columnLength = len(headers)

        #use calculated columnLength & offset to format the break
        lineBreak = tableLineGen(columnLength, offsetValue)        
        
        #builds an invisible matrix of size [columnLength] X [rowLength]
        for i in range (rowLength):
            printMatrix.append([" "] * columnLength)
            
        #access lines using the amount of lists in data
        #use counts to determine positioning of the print matrix
        outerCount = 0
        innerCount = 0
        for  pos in data:
            for item in pos:
                printMatrix[innerCount][outerCount] = data[outerCount][innerCount]
                innerCount += 1
	    #must reset inner count to avoid out of bounds exception
            innerCount = 0
            outerCount += 1
            
        print (lineBreak)
            
        #formats header printing for the column names
        #iterates through and prints the items
        print ("|", end = " ")
        for items in headers:
            if(len(items)<= offsetValue):
                print (items," " * (offsetValue - len(items)), "|", end = " ")
            else:
                print (items,"|", end = " ")
        print ("")
            
        print (lineBreak)
     
        #iterates through the rows in the printMatrix
        for row in printMatrix:
            #iterates through data in the printMatrix rows
            print ("|", end = " ")
            for item in row:
                print (item, end = " ")
                if len(item) <= offsetValue:
                    print (" " * (offsetValue - len(item)), "|", end = " ")
            print ("")
            
        print (lineBreak)
            
    else:
        print ("Error printing data, Data out of bounds")


#creates table break to be saved as String
def tableLineGen(length, offsetValue):
    out = ''
    lineBreak = '-' * (offsetValue + 1)
    out = out + "+ "
    for m in range(length):
        out = out + lineBreak + ' + '
    out = out
    return out
    
    

printData('test', ['header 1', 'header 2'], [['data 1'],['data 2']])



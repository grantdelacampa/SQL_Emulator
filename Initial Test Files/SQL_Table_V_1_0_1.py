"""
Grant De La Campa
2018
V 1.0.1

Formated print for a python based SQL Emulator
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
        lineBreak = ""
        
        #sets up row and column length parameters 
        #also sets the offsetValue based on headers and data
        #TODO move to function
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

        #compute the line break length for later use
        lineBreak = '-' * (offsetValue + 1)
        
        
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

        tableLine(columnLength, lineBreak)
            
        #formats header printing for the column names
        #iterates through and prints the items
        print ("|", end = " ")
        for items in headers:
            if(len(items)<= offsetValue):
                print (items," " * (offsetValue - len(items)), "|", end = " ")
            else:
                print (items,"|", end = " ")
        print ("")
            
        #prints the break between the header items and the rows
        tableLine(columnLength, lineBreak)
     
        #iterates through the rows in the printMatrix
        for row in printMatrix:
            #iterates through data in the printMatrix rows
            print ("|", end = " ")
            for item in row:
                print (item, end = " ")
                if len(item) <= offsetValue:
                    print (" " * (offsetValue - len(item)), "|", end = " ")
            print ("")
        tableLine(columnLength, lineBreak)
            
    else:
        print ("Error printing data, Data out of bounds")

#prints the break between the header items and the rows
def tableLine(length, lineBreak):
    print ("+", end = " ")        
    for m in range(length):
        print (lineBreak, '+', end = " ")
    print ("")

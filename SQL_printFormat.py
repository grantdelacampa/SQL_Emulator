"""
Grant De La Campa
1/28/2018
Version 1.0
SQL_printFormat.py

Data output processing for a SQL emulator written in python. Computes an invisible matrix using the input data. Then uses transformation to place the data vertically on the matrix.

    i.e. data = [[d1, d2, d3], [d4, d5, d6]]
    columnCount = 2
    rowCount = 3
    matrix size is [2]x[3]
        where data[0][0] = d1   pos is mat[0][0]
              data[0][1] = d2          mat[0][1]
              data[0][2] = d3          mat[0][2]
              data[1][0] = d4          mat[1][0]
              data[1][1] = d5          mat[1][1]
              data[1][2] = d6          mat[1][2]
              
    Program does account for missing data.
    
    
    Proper format of input:
        printData(<table_name>, <[column_names]>, <[[data]])
        
    NOTE:
        data format is by row NOT Column
        
    Sample Input:
    printData("Family", ["fname", "age", "association"], [["Larry", "Brandon", "Joe"], ["60", "17", " "], ["Grandpa", "Brother", "step-dad"]])
    
    Sample Output:
    | fname        | age          | association  | 
    + ------------------------------------------ +
    | Larry        | 60           | Grandpa      | 
    | Brandon      | 17           | Brother      | 
    | Joe          |              | step-dad     | 
    
              
"""


def printData(name, headers, data):
    #verify the data will be in range of the columns
    #i.e. there isnt 5 sets of data and 3 columns
    if len(data) <= len(headers):
        printMatrix = []
        rowLength = 0
        columnLength = 0
        offsetValue = 0
        
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
            innerCount = 0
            outerCount += 1
            
        #formats header printing for the column names
        #iterates through a prints the items
        print "|",
        for items in headers:
            if(len(items)<= offsetValue):
                print items," " * (offsetValue - len(items)), "|",
            else:
                print items,"|",
        print ""
            
        #prints the break between the header items and the rows
        #TODO fix this
        print "+", "-" * ((columnLength + 1) * offsetValue), "+"
     
        #iterates through the rows in the printMatrix
        for row in printMatrix:
            #iterates through data in the printMatrix rows
            print "|",
            for item in row:
                print item,
                if len(item) <= offsetValue:
                    print " " * (offsetValue - len(item)), "|",
            print ""
            
    else:
        print "Error printing data, Data out of bounds"
    
#test call:
printData("printTest", ["column1", "column2", "column3"],[["c1_data_1", " ", " "], ["c2_data_1", "c2_data_2", "c2_data_3"],["c3_data_1", " ", "c3_data_2


from SQL_Emulator_V_0_1_1 import *
"""
Grant De La Campa
2018

User endpoint for SQL_Emulator,
    -Asks for and accepts user input
    -Provieds assistance to user via keywords
    -keywords are processed here to prevent unecessary comparisons in the Emulator.
"""
query = ''
log = []


dict = {
    'Emulator Version': "V_0_1_0b",
    'Save' : "Save to a txt file",
    'Out' : "Dumps out SQL querys for current tables",
    'Exit': "Type Exit to close Emulator",
    'Load': "Load <file_name>",
    'Log': "Logs keys strokes and output\n",
    'Querys': "",
    'Select': "SELECT <item(s)> FROM <table_name>",
    'Create': "CREATE TABLE <table_name> (<column_name(s)>)",
    'Drop': "DROP <table_name OR database_name>",
    'Truncate': "TRUNCATE TABLE <table_name>",
    'Insert': "INSERT INTO <table_name> (<column_name>) VALUES (<value(s)>)"
    }

print ("Grant De La Campa @ 2018")
print ("SQL Emulator V:0.1.0")
print ("Use Help for more options")

while (query != 'Exit'):
    query = input("SQL>> ")
    log.append(query)
    #inital case where the query is empty or " "
    if (query == "") | (len(query)==0) | (query[0] == " "):
        print ("error no query")
    #Case 1: returns the help dictionary
        
    elif(query == "Help"):
        for keys in dict:
            print (keys, ":", end = " ")
            for item in dict[keys]:
                print (item, end = "")
            print ("")
    #Prevents the while from sending 'Exit' to sqlmain()
    #A bit of a cheat way to ignore a small bug
    elif(query == 'Exit'):
        pass
    #When implemented will save the current database to a text file 
    elif(query == 'Save'):
        print ("this function does not currently exist in V_0_1_0")
    #When implemented will dump properly formatted SQL querys for the end user
    elif(query == 'Out'):
        print ("this function does not currently exist in V_0_1_0")
        fileName = input("Enter out file name: ")
        if (fileName != "") | (fileName != ""):
            f = open(fileName, "w+")
            for item in log:
              f.write(str(item) + "\n")
            f.close()
        else:
            print ("Error no file name given")
    #When implemented will Load the txt file from the specified user session
    elif(query == 'Load'):
        print ("this function does not currently exist in V_0_1_0")
    #Returns a log from the users session
    elif(query == 'Log'):
        for entry in log:
            print (entry)
    else:
        sqlmain(query)

    

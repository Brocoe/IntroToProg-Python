# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Brooke Biscoe,February 13, 2021,Added code to complete assignment 5
# Brooke Biscoe,February 14, 2021,changed the names of variables to be more descriptive
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
from typing import Any

objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
#### Extra Variables that I added ####
strTask = "" # to capture the task value that is added to my list
strPriority = "" # to capture the priority value that is added to my list

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open("ToDoList.txt",'r')
    for row in objFile:
        strData = row.split(',')
        dicRow = {"Task":strData[0],"Priority":strData[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except:
    objFile = open("ToDoList.txt",'w')
    objFile.close()
    print("TO DO list file created!")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('TASK | PRIORITY')
        for row in lstTable:
            print(row['Task'],' | ',row['Priority'])
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Please enter a task to add to the TO DO List: ")
        strPriority = input("Please enter what priority this task is: ")
        dicRow = {'Task':strTask,'Priority':strPriority}
        lstTable.append(dicRow)
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strMenu = input("Select an item to remove: ")
        for row in lstTable:
           if row['Task'].lower() == strMenu.lower():
               lstTable.remove(row)
               print("'{}' has been removed from the TO DO list".format(strMenu))
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt",'w')
        for row in lstTable:
            objFile.write(row['Task']+','+row['Priority']+'\n')
        objFile.close()
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        #No code necessary
        break  # and Exit the program
    else:
        #Adding a bit of error handling
        print("Please enter a value between 1 and 5")

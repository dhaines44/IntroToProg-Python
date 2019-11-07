# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Daylen Haines>,<11/5/19>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strFile = "ToDoList.txt" # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
lstRow = [] # A row of text from ToDoList file
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # A Task the user inputs
strPriority = "" # A Priority the user assigns to a task

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
open(objFile, "a")
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"task":lstRow[0],"priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show Current Data
    2) Add a New Item
    3) Remove an Existing Item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
 # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Your Current To Do List Items Are:  ')
        for row in lstTable:
            print(row["task"] + ',' + row["priority"])
        continue
# Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("Add a New Item")
        strTask = str(input("Enter a New Task: "))
        strPriority = str(input("Enter the Priority of the New Task: "))
        dicRow = {"task":strTask,"priority":strPriority.strip()}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        rmvTask = input("Would you like to remove your latest entry? Enter 'y' or 'n':  ")
        if rmvTask.lower() == "y":
            del lstTable[len(lstTable)-1]
            print("Latest Task successfully removed")
        else:
            print("No Tasks removed")
        continue
# Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Saving Data to File.")
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["task"] + ',' + row["priority"] + '\n')
        objFile.close()
        continue
# Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("You Have Chosen to Exit the Program, Press Enter to Exit.")
        break  # and Exit the program

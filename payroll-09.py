"""
Author: Ayo Asekun
Date Created: Oct 11th, 2019
Last Date Modified: Oct 12th, 2019
Program Description: Data Mining: Employee hours & Hourly Wages Table
Psuedocode:
<START PROGRAM>
INPUTS: Using provided files; Extract source files & save data to reachable directory
        "path" = file path of data on OS HD

PROCESS: Data cleaning & reorganization required for proper visualization
        Using "import os" to interact with OS:
                #input file path into program
                #Define structure of data output
                #pulling each element every line; data interaction can be made
                #Sort each element into a specified column for proper visualization

OUTPUTS:  Each column should represent extracted data from the provided source files as shhow in below lay out
                "LAST-NAME   |  HOURLY-WAGE  |   HOURS-WORKED"
                " ********   |  **********   |     ********  "
                .
                .
                .

<END PROGRAM>:  End of Pay-roll

"""
import os

path = "data1.txt"
#'path' must be in python directory folder to run above variable; else access location path directory & insert
d1 = open(path, "r+")
LN = "LAST-NAME"
HW = "HOURLY-WAGE"
WH = "HOURS-WORKED"
print("____________________________________________________")
print("%-12s |    %10s   | %15s" % (LN, HW, WH))
print("____________________________________________________")
for x in d1:
    NUM1 = x.split()
    print("%-12s |    %10s    | %11s" % (NUM1[0], NUM1[1], NUM1[2]))

else:
    print(" ")
    print(" ")
    print("End of Pay-roll")

d1.close()















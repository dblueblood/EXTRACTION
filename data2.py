"""
Author: Ayo Asekun
Date Created: Oct 5th, 2019
Last Date Modified: Sept 5th, 2019
Program Description: Create & Read a Text(.txt) File
Algorithm:
<START PROGRAM>
INPUTS: Number range program will be using to build text

PROCESS: Creating a range(which is added to manually coded to program by author), Program will run through range
    adding the below string as a lead concatenate, with every generate range value
                                            "This is number..."
    Using new-line character added to end of string, expressions above will run with new line until range is exhausted

OUTPUTS: "This is number <range-start>
            .
            .
            .
        <range-end>"

<END PROGRAM>
"""
DOC = open("data2.txt", "w+")

for Value in range(1, 11):
    Val1 = str(Value)
    DOC.write("This is number " + Val1 + ".""\n")

DOC.close()
# RETURN TO DIRECTORY TO SEE CREATED FILE

# EXPRESSIONS BELOW; TO VIEW ABOVE CREATED TEXT FILE IN SHELL
DOC = open("data2.txt", "r")
print(DOC.read())
DOC.close()

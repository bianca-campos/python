# exercise 1
# Write a program to read through a file and print the contents of the file (line by line)
# all in upper case. Executing the program will look as follows:
# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500
filename = input("Enter a filename: ") # mbox-short.txt or mbox.txt
try:
    fhand = open(filename, "r")
    for line in fhand:
        line = line.strip()  # correction - strip white spaces
        print(str.upper(line))

except FileNotFoundError:
    print("File cannot be opened:", filename)


# exercise 2
# Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point
# number on the line. Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.
import statistics
list = []
filename = input("Enter a filename: ") # mbox-short.txt or mbox.txt
try:
    ftest = open(filename, "r")
    for line in ftest:
        line = line.strip()     # correction - strip white spaces
        if line.startswith("X-DSPAM-Confidence:"):
            new_line = line.split(":")
            list.append(float(new_line[1]))
    print("Average spam confidence:", statistics.mean(list))

except FileNotFoundError:
    print("File cannot be opened:", filename)




# exercise 3
# Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program
# Modify the program that prompts the user for the file name so that it prints a funny message when the user types in
# the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist.
line = 0
filename = input("Enter a file name: ")
try:
    if filename.lower() == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        fread = open(filename, "r")
        for result in fread:
            line += 1
        print("There were", line, "subject lines in", filename)

except FileNotFoundError:
    print("File cannot be opened:", filename)
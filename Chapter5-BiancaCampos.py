import math
import statistics

#Exercise 1
# Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
# print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.
l = []
# while user types number
while True:
    # get input
    n = input("Enter a number: ")
    if n.isdigit():
        # add it to my list
        l.append(int(n))
    elif n.lower() == "done": #not case sensitive
        print(int(math.fsum(l)), len(l), statistics.mean(l)) #total, count, average
        break
    else:
        print("Invalid input")


#Exercise 2
# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and
# minimum of the numbers instead of the average.
l = []
# while user types number
while True:
    # get input
    n = input("Enter a number: ")
    if n.isdigit():
        # add it to my list
        l.append(int(n))
    elif n.lower() == "done": #not case sensitive
        print(int(math.fsum(l)), len(l), max(l), min(l)) #total, count, max, min
        break
    else:
        print("Invalid input")

# Exercise 1
# Write a function called chop that takes a list and modifies it, removing the first
# and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
def chop(alist):
    alist.remove(alist[0])
    alist.remove(alist[len(alist)-1])
def middle(alist):
    return alist[1:len(alist)-1]

# Exercise 2:
# Figure out which line of the above program is still not properly guarded. See if you can construct a text
# file which causes the program to fail and then modify the program so that the line is properly guarded and test it to
# make sure it handles your new text file.
#Exercise 2
fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != "From": continue
    if len(words) >= 3: continue  # in case, words[2] doesn't exist
    print(words[2])

# Exercise 3:
# Rewrite the guardian code in the above example without two if state- ments. Instead, use a compound logical
# expression using the and logical operator with a single if statement.
fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != "From": continue
    print(words[2])

# Exercise 4
# Download a copy of the file from www.py4e.com/code3/romeo.txt Write a program to open the file romeo.txt and read
# it line by line. For each line,
# split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is not in
# the list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
fhand = open("romeo.txt", "r")
total_words = []
for line in fhand:
    words = line.split()
    for word in words:
        if word not in total_words:
            total_words.append(word)
fhand.close()
total_words.sort()
print(total_words)


# Exercise 5
# Write a program to read through the mail box data and when you find line that starts with “From”, you will split the
# line into words using the split function. We are interested in who sent the message, which is the second word on the From line.
# You will parse the From line and print out the second word for each From line, then you will also count the number of From
# (not From:) lines and print out a count at the end.
filename = input("Enter a file name: ")
fhand = open(filename, "r")
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != "From": continue
    count += 1
    print(words[1])

print("There were {} lines in t he file with From as the first word".format(count))

# Exercise 6
# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers
# at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use
# the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
l = []
while True:
    # get input
    n = input("Enter a number: ")
    if n.isdigit():
        # add it to my list
        l.append(int(n))
    elif n == "done":
        break

maximum = max(l)
minimum = min(l)

print("Maximum:", float(maximum))
print("Minimum:", float(minimum))
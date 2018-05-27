#exercise 6
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into a floating point number.
str = "X-DSPAM-Confidence:0.8475"
find_ini = str.find(":")
find_fin = str[find_ini + 1:]
print(float(find_fin))


#exercise 7
# test = input("Insert the test:")
# print(str.capitalize(test))
# test = input("Insert the test UPPER case:")
# print(str.lower(test))

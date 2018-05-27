#Exercise 2
# Write a program that uses input to prompt a user for their name and then welcomes them.
name = input("Enter your name: ")
print("Hello " + name)


#Exercise 3
# Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
print("Pay:", int(hours) * float(rate))
#or
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print("Pay:", hours * rate)

#Exercise 4
# Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# 1. width//2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5
width = 17
height = 12.0
calc1 = width//2
print("1. ", width//2, type(calc1))
calc2 = width/2.0
print("2. ", calc2, type(calc2))
calc3 = height/3
print("3. ", calc3, type(calc3))
calc4 = ((calc1 + calc2) * 5)
print("4. ", calc4, type(calc4))


#Exercise 5
# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
# and print out the converted temperature.
celcius = input("Enter celcius temperature: ")
fahrenheit = int(celcius) * float(1.8) + int(32)
print("Fahreinheit temperature: ", fahrenheit, "F")


#Exercise 4
# What is the purpose of the “def” keyword in Python?
# a) It is slang that means “the following code is really cool”
# b) It indicates the start of a function
# c) It indicates that the following indented section of code is to be stored for later d) b and c are both true
# e) None of the above
#Answer: b

#Exercise 5
# What will the following Python program print out?
# def fred():
#   print("Zap")
# def jane():
#    print("ABC")
# jane()
# fred()
# jane()
# a) Zap ABC jane fred jane
# b) Zap ABC Zap
# c) ABC Zap jane
# d) ABC Zap ABC
# e) Zap Zap Zap
#Answer: d


#Exercise 6
# Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).
def computepay(hours, rate):

        if hours > 40:
            pay = ((40 * rate) + (hours - 40) * rate * 1.5)
            return pay
        else:
            pay = hours * rate
            return pay

try:
    employe_hours = int(input("Enter Hours: "))
    employe_rate = int(input("Enter Rate: "))
    payment = computepay(employe_hours, employe_rate)
    print("Pay:", payment)
except:
    print("Error, please enter numeric input")

#Exercise 7
# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its
# parameter and returns a grade as a string.
# Score     Grade
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# <0.6        F
def computegrade(score):

         if score > 1 or score < 0:
            return str("Bad score")
         else:
            if score >= 0.9:
             return str("A")
            elif score >= 0.8:
             return str("B")
            elif score >= 0.7:
             return str("C")
            elif score >= 0.6:
             return str("D")
            else:
             return str("F")
try:
    score_student= float(input("Enter score: "))
    final_grade = computegrade(score_student)
    print("Score:", final_grade)
except:
    print("Bad score")
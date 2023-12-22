# Problem #2
# Use switch stmt, think of all possible age as input.
# Print if the user goes to kindergarten (age 3-6), primary school (7-11), ,middle school (12-15),
# highschool (16-19), college (20-24).
# Get users name and age as input.
# Eg input Sam, 10
# Output is Sam goes to primary school


#getting user input
name = input("Enter name : ")
age = int(input("Enter age : "))

#printing as per age
match age :
    case  n if n<0 :
        print("Age cannot be negative")
    case n if n == 0 :
        print("Age cannot be Zero")
    case n if 1 <= n <  3:
        print(name," is not yet eligible for schooling")
    case n if n <=  6:
        print(name," goes to Kindergarden")
    case n if n <= 11:
        print(name," goes to primary school")
    case n if n <= 15:
        print(name," goes to middle school")
    case n if n <= 19:
        print(name," goes to high school")
    case n if n <= 24:
        print(name," goes to college")
    case n if n >= 25:
        print(name," has completed college")
    case _:
        print("Enter a valid age")


# Output :

# Enter name : theepika
# Enter age : 23
# theepika  goes to college 

# Enter name : sendhan amudhan   
# Enter age : 0
# Age cannot be Zero

# Enter name : roja
# Enter age : 30
# roja  has completed college

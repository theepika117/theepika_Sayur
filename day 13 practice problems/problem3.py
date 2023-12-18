# Problem #3
# Use switch stmt (no if stmts) to calculate the grade of the student based on marks
# Grade A = mark >90
# Grade B  between 80 and 90
# Grade C between 60 and 80
# Fail , below 60

#getting user input
mark = int(input("Enter mark : "))

#printing grade as per mark
match mark :
    case  n if n<0 :
        print("Mark cannot be negative")
    case n if n == 0 :
        print("Mark cannot be Zero")
    case n if n < 60 :
        print("Fail")  
    case n if n <= 80 :
        print("Grade C")
    case n if n <= 90 :
        print("Grade B")
    case n if n <= 100 :
        print("Grade A")
    case n if n >= 100 :
        print("Mark cannot be greater than 100") 
    case _:
        print("Enter a valid mark")


# Output :

# Enter mark : 45
# Fail

# Enter mark : 89
# Grade B

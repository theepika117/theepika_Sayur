# Problem #1
# Print the following pattern
# 1
# 212
# 32123
# 4321234
# 543212345
# Get user input for how far to go (up to 0)

n = int(input("Enter a number :"))
#validating input
if n == 1:                                      
    print("1")
elif n==0 or n<0 :
    print("Enter a positive integer ")
else :
    temp = str(1)
    print(temp)                                                 #initialising temp to be 1 and printing it
    for i in range(2,n+1) :
        temp = str(i)+str(temp)+str(i)                          #updating the output in temp
        print(temp)

# Output:
# Enter a number :3
# 1
# 212
# 32123
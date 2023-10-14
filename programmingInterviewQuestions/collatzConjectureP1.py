# 1.Write a program for Collatz_conjecture.
# Collatz_conjecture means -  start with the input number.
# For even number , divide by 2 (n/2)
# For odd number - 3n + 1
# apply the above for the resulting number until the answer is 1.Eg, input is 8
# output 8, 4,2, 1
# input is 9
# output 9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1

#Get two numbers as input. Print the number that has less number of steps to reach 1



def collatzNumber(n) :
             
    count = 0                       #initializing a variable to count the number of iterations
    while(n!= 1) :                  
        if (n%2) == 0 :             #checking for even number
            n //= 2                 #dividing by 2
        
        else :
            n = (3*n)+1             #performing 3*n+1 on odd number

        count += 1                  #increamenting the count

    print(f"The {n} has reached 1 after {count} iterations")

    return count

number = []                                 #empty list to store numbers entered by user
count = []                                  #empty list to store the corresponding count returned by the function
for i in range(2) :
    n = int(input("Enter a number : "))
    number.append(n)                    
    c = collatzNumber(n)                    #function call
    count.append(c)                         

minValue = min(count)                       #finding the minimum of two counts
print(f"The number {number[count.index(minValue)]} has reached 1 with minimum iteration of {minValue}")

#Output:
# Enter a number : 16
# The 1 has reached 1 after 4 iterations
# Enter a number : 4
# The 1 has reached 1 after 2 iterations
# The number 4 has reached 1 with minimum i
# teration of 2
# Problem #1
# Input is a range of numbers as string. Print only the numbers that are palindromes and also the 
# square of that number is also a palindrome.
# eg. 121 is a palindrome and 121 * 121 = 14641 is also a palindrome, so you can print 121
# 131 is a palindrome, but 131*131 = 17161 is not a palindrome,so you can't print it.
# eg input "10", "500"
# Make sure to identify which steps need to be a function, how to avoid unnecessary parsing 
# of numbers. Checking for palidrome or not, should be an efficient code.



import re

#defining a function to check whether the number is palindrome or not
def palindrome (num) :
    
    temp = "".join(reversed(num))                   #reversing the number and storing it in a temprory variable
    if temp == num :                                #if both reversed value and the original values are same the number is palindrome
        isPalindrome = True
    else :
        isPalindrome = False

    return isPalindrome


#main code


userInput = input("Enter a number range : ")                #geting user input
pattern = r'\b\d+\b'                                        #defining a pattern to identify numericals from the given string
numbers = re.findall(pattern,userInput)                     #seperating the range
st_num , end_num = int(numbers[0]) , int(numbers[1])        #setting starting and ending range

#initializing a for loop to identify a palindrome whose square is also a palindrome
for num in range (st_num,end_num+1):
    if num > 10 :                                           #avoing unneccessary parsing of single digit numbers
        num = str(num)
        if num[0] == num[-1] :                              #considering only those numbers whose first and last digits are same to avoid unneccessary parsing
            result = palindrome(num)
            if result == True :
                num = int(num)
                sqr = str(num * num)
                if sqr[0] == sqr[-1] :                      #again considering only those numbers whose first and last digits are same to avoid unneccessary parsing
                    finalResult = palindrome(sqr)
                    if finalResult :
                        print(num)                          #if both the return values are true the the number is the required number


# Output :
# Enter a number range : 10 500
# 11
# 22
# 101
# 111
# 121
# 202
# 212

# problem #4
# write a program to find if two strings are same.
# two string are considered same if both strings have same letters in same order, but from different starting point
# eg abcd is same as bcda (a is moved to the right)
# abcd is same as cdab 
# abcd is  not same as cdba

# 123456 = 456123
# 123456 not = 412356


def findSimilarStrings (inputString1,inputString2) :                    #passing user given strings as arguments
    startingChar = inputString1[0]                                      #determining the starting character of first string
    charIndex = inputString2.find(startingChar)                         #finding start symbol in the second string
    temp = inputString2[charIndex:] + inputString2[:charIndex]          #slicing the string2


    if temp == inputString1 :                                           #checking if newly created string and string 1 are equal
        print("The given strings are Similar strings")
    else :
        print("The given strings are not similar strings")


#main code 
str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")
findSimilarStrings(str1,str2)
# Problem #1
# 1. Check whether the given string input is a valid ip address.
# Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.'
# etc)
# Write all constraints.
# Get an input as string. Return if it is valid or not. 
# Use string functions.


# To check if a string represents a valid IPv4 address, you can follow these general steps:
# 1.Split the string into four parts using the dot ('.') as a delimiter.
# 2.Ensure that there are exactly four parts after splitting. An IPv4 address should consist of four octets.
# 3.For each part, check if it is a valid decimal number and falls within the range 0 to 255 (inclusive).


validity = False 

octets = list()                                     #list to store numbers

userInput = input("Enter a IPV4 address : ")

dotNum = userInput.count('.')                       #counting number of delimiter

if dotNum == 3 :

    validity = True
    
    #initializing a for loop to seperate the numbers
    for i in range(3) :

        temp = userInput.partition(".")             #returns a tuple of elements : 1 - everything before the "match" 2 - the "match" 3 - everything after the "match"

        octets.append(int(temp[0]))                 #appends the element before dot to the octet list

        dot = userInput.find(".")

        userInput = userInput[dot+1:]               #slices the string after dot till the end

    if temp[2] != "" :                              #if the last element is not empty in list,it appends it to octets list
        octets.append(int(temp[2]))

    if (len(octets) == 4 ):

        #for loop to check whether the octet lies in the range
        for number in octets :

            if not (number  >= 0 and number <= 255 ):
               
                print("numbers in octect must be between 0 and 255")
                
                validity = False
                
                break

    else :
        
        print("There must be four octet in the IPV4 address")
        
        validity = False

else :

    print("There must be 3 delimiter and 4 octets")


if validity :
    print("Given address is a valid IPV4 address")

else :
    print("Hence the address is invalid")
        



    
# Output :

# Enter a IPV4 address : 1.23.3.6
# Given address is a valid IPV4 address

# Enter a IPV4 address : 123.2     
# There must be 3 delimiter and 4 octets
# Hence the address is invalid  

# Enter a IPV4 address : 123.456.789.
# There must be four octet in the IPV4 address
# Hence the address is invalid 

# Enter a IPV4 address : 1.2.3.256
# numbers in octect must be between 0 and 255
# Hence the address is invalid



# a = "123.456.789"
# b = a.partition(".")     #('123', '.', '456.789')
# print(b[0],a)            #123 123.456.789
# #print(a.find("."))       #3

# a="123."
# b = a.partition(".")
# print(b[2]=="")          #True


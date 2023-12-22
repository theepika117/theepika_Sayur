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


import re 


validity = False 

userInput = input("Enter a IPV4 address : ")

dotPattern = r'\.'

numbers = r'\b\d{1,3}\b'

delimiter = re.findall(dotPattern,userInput)

octets = re.findall(numbers,userInput)

parts = len(delimiter)
#print(numbers)

if parts == 3 :
    validity = True

    if (len(octets) == 4 ):

    
            for number in octets :

                number = int(number)

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

# Enter a IPV4 address : 1.2.3.4
# Given address is a valid IPV4 address

# Enter a IPV4 address : 256.2.3.5
# numbers in octect must be between 0 and 255
# Hence the address is invalid

# Enter a IPV4 address : 1.2.3
# There must be 3 delimiter and 4 octets
# Hence the address is invalid



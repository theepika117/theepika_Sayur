# Problem #2
# Same as above,but print the list in descending order
# input = [1,2,3,3,3,4,4,7,7,9]
# output = [9,7,4,3,2,1,_,_,_,_]


#getting user input and converting it into a list
userInput = input("Enter numbers in ascending order with duplicates and space between every number : ")
numbers = userInput.split()

duplicateCount = 0                          #initializing count variable

nonDuplicates = list()                      #initializing empty list to append non repeated values

for number in numbers :
    
    if number not in nonDuplicates :
        nonDuplicates.append(number)        #appending non repeated numbers to seperate list
    
    else :
        duplicateCount +=1                  #incrementing the count for every duplicate values encountered

nonDuplicates.sort(reverse = True)          #making the list as desending ordered list

for i in range(duplicateCount):
    nonDuplicates.append("_")               #appending "_" at the end 

print(nonDuplicates)


# Output:
# Enter numbers in ascending order with duplicates and space between every number : 1 2 3 3 3 4 4 7 7 9
# ['9', '7', '4', '3', '2', '1', '_', '_', '_', '_']

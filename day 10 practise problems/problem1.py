# Problem #1
# You have a list of numbers in ascending order, but with duplicates.
# Remove the duplicated, append _ at the end for each duplicate removed 
# eg input = [1,2,3,3,3,4,4,7,7,9]
# output = [1,2,3,4,7,9,_,_,_,_]

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

for i in range(duplicateCount):
    nonDuplicates.append("_")               #appending "_" at the end 

print(nonDuplicates)



#output
# Enter numbers in ascending order with duplicates and space between every number : 1 2 3 3 3 4 4 7 7 9
# ['1', '2', '3', '4', '7', '9', '_', '_', '_', '_']Enter numbers in ascending order with duplicates and space between every number : 1 2 3 3 3 4 4 7 7 9
# ['1', '2', '3', '4', '7', '9', '_', '_', '_', '_']



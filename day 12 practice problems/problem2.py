# Problem #2
# Input is an integer list and another integer k. Output is the k most frequently occuring numbers.
# output can be in any order.
# eg input = [1,1,1,2,2,3,5,5,5,5], k =2
# output [1,5] (top 2 most frequently occuring numbers)
# input = [4,5,4,5,4,5,3,3,3,7,8,1,1,1], k = 4
# output [4,5,3,1]

#getting user input and converting it into a list
userInput = input("Enter integers seperated by blanck space : ")
numbers = userInput.split()

k = int(input("Enter k : "))

uniqueNum = list()                                      #Initializing a list to store elements in the user input without its duplicates
count = list()                                          #initializing a list to store the count of each number    
answer = list()                                         #initializing a  list to store the final answer


#initializing a for loop to calculate the frequency of each unique numbers
for number in numbers :
    if number not in uniqueNum :
        uniqueNum.append(number)                        #appending unrepeated numbers to uniqueNum list
        count.append(numbers.count(number))             #appending its frequency to count list


#initializing a for loop to determine top 'k' number of frequently occured element
for i in range(k):
    maxFreq = max(count)                                #maxFreq contains the current maximum value of count list
    indx = count.index(maxFreq)                         #determining corresponding index of maxFreq in count list
    answer.append(uniqueNum[indx])                      #appending the corresponding element with 'maxfreq' count from uniqueNum on to answer list using its index value
    count.pop(indx)                                     #poping the element and its count from the corresponding lists so that we can easily get the next max count value
    uniqueNum.pop(indx)

#printing the final answer
print("Top ",k," frequently repeated elements are : ",answer)


# Output:
# Enter integers seperated by blanck space : 1 1 2 2 2 3 4 4 4 4 5
# Enter k : 2
# Top  2  frequently repeated elements are :  ['4', '2']

